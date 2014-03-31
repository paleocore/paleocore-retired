from django.contrib import admin
from models import *  # import database models from models.py
from django.forms import TextInput, Textarea  # import custom form widgets
from django.http import HttpResponse
import unicodecsv
from django.core.exceptions import ObjectDoesNotExist

import csv,cStringIO, codecs

###################
## Biology Admin ##
###################

biology_fieldsets = (
('Taxonomy', {
'fields': (('tax_class',),('tax_order',),('family',),('subfamily',),('tribe',),('genus','specificepithet'),("id"))
}),
)


class biologyInline(admin.TabularInline):
    model = drp_biology
    extra = 0
    readonly_fields = ("id",)
    fieldsets = biology_fieldsets


class biologyAdmin(admin.ModelAdmin):
    list_display = ("id","occurrence","tax_class","tax_order","family","subfamily","tribe","genus","specificepithet","lowest_level_identification")
    list_filter = ("family",)
    search_fields = ("lowest_level_identification",)
    readonly_fields = ("id",)
    fieldsets = biology_fieldsets


#####################
## Hydrology Admin ##
#####################

class hydrologyAdmin(admin.ModelAdmin):
    list_display = ("id","size")
    search_fields = ("id",)
    list_filter = ("size",)


#####################
## Locality Admin ##
#####################

class localityAdmin(admin.ModelAdmin):
    list_display = ("collectioncode","paleolocalitynumber","paleosublocality")
    list_filter = ("collectioncode",)
    search_fields = ("paleolocalitynumber",)


######################
## Occurrence Admin ##
######################

occurrence_fieldsets =(
('Curatorial', {
'fields': (('barcode','catalognumber'),
           ("id",'fieldnumber','yearcollected',"datelastmodified"),
           ("collectioncode","paleolocalitynumber","itemnumber","itempart"))
}),

('Occurrence Details', {
'fields': (('basisofrecord','itemtype','disposition','preparationstatus'),
           ('itemdescription','itemscientificname'),
           ('remarks'))
}),
('Provenience', {
'fields': (("strat_upper","distancefromupper"),
           ("strat_lower","distancefromlower"),
           ("strat_found","distancefromfound"),
           ("strat_likely","distancefromlikely"),
           ("analyticalunit","analyticalunit2","analyticalunit3"),
           ("insitu","ranked"),
           ("stratigraphicmember",),
           ("point_X","point_Y"),
           ('geom'))
}),
)


class occurrenceAdmin(admin.ModelAdmin):
    list_display = ('id', 'stratigraphicmember', "catalognumber", "barcode", 'basisofrecord', 'itemtype',
                    'collector', "itemscientificname", "itemdescription", "point_X", "point_Y", "yearcollected",
                    "fieldnumber", "datelastmodified")

    #note: autonumber fields like id are not editable, and can't be added to fieldsets unless specified as read only.
    #also, any dynamically created fields (e.g. point_X) in models.py must be declared as read only to be included in fieldset or fields
    readonly_fields = ("id", "fieldnumber", "point_X", "point_Y", "catalognumber", "datelastmodified")

    list_filter = ["basisofrecord","yearcollected","stratigraphicmember","collectioncode","itemtype"]
    search_fields = ("id","itemscientificname","barcode","catalognumber")
    inlines = (biologyInline,)
    fieldsets = occurrence_fieldsets
    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'size':'25'})},
        models.TextField: {'widget': Textarea(attrs={'rows':4, 'cols':40})},
    }
    #change_form_template = "occurrence_change_form.html"
    actions = ["move_selected", "get_nearest_locality"]
    actions = ["get_nearest_locality", "create_data_csv"]

    #admin action to download data in csv format
    def create_data_csv(self, request, queryset):
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="DRP_data.csv"'
        writer = unicodecsv.writer(response)
        o = drp_occurrence()  # create an empty instance of an occurrence object
        b = drp_biology()  # create an empty instance of a biology object

        """
        For now this method handles all occurrences and corresponding
        data from the biology table for faunal occurrences.
        """
        writer.writerow(o.__dict__.keys()+b.__dict__.keys())  # fetch field names and write to the first row

        for occurrence in queryset.all():  # iterate through the occurrence instances selected in the admin
            try:  # try writing drp_occurrence values and associated drp_biology values
                writer.writerow(occurrence.__dict__.values()+occurrence.drp_biology.__dict__.values())
            except ObjectDoesNotExist:  # Django specific exception
                writer.writerow(occurrence.__dict__.values())  # add only drp_occurrence values)
            except:
                writer.writerow(occurrence.__dict__.values())  # add only drp_occurrence values

        return response

    create_data_csv.short_description = "Download Selected to .csv"

    #admin action to get nearest locality
    def get_nearest_locality(self,request, queryset):
        #first make sure we are only dealing with one point
        if queryset.count()>1:
            self.message_user(request,"You can't get the nearest locality for multiple points at once. Please select a single point.",level='error')
            return
        #check if point is within any localities
        matching_localities = []
        for locality in drp_locality.objects.all():
            if locality.geom.contains(queryset[0].geom):
                matching_localities.append(str(locality.collectioncode) + "-" + str(locality.paleolocalitynumber))
        if matching_localities:
            #warning to user if the point is within multiple localities
            if len(matching_localities)>1:
                self.message_user(request,"The point falls within multiple localities (localities %s). Please consider redifining your localities so they don't overlap."% str(matching_localities).replace("[",""))
                return
            #Message user with the nearest locality
            self.message_user(request,"The point is in %s" %(matching_localities[0]))

        #if the point is not within any locality, get the nearest locality
        distances={}#dictionary which will contain {<localityString>:key} entries
        for locality in drp_locality.objects.all():
            locality_name=str(locality.collectioncode) + "-" + str(locality.paleolocalitynumber)
            #how are units being dealt with here?
            locality_distance_from_point = locality.geom.distance(queryset[0].geom)
            distances.update({locality_name:locality_distance_from_point})
            closest_locality_key=min(distances,key=distances.get)
        self.message_user(request,"The point is %d meters from locality %s" %(distances.get(closest_locality_key),closest_locality_key))


    #admin action to move points to specified x and y coordinates
    def move_selected(self,request,queryset):
        returnURL="/admin/drp/drp_occurrence/"
        def render_move_form():
            t=loader.get_template("move_points.html")
            c = RequestContext(request, {'returnURL':returnURL,'selectedPoints':queryset, 'action_checkbox_name': helpers.ACTION_CHECKBOX_NAME,})
            return HttpResponse(t.render(c))

        if "apply" in request.POST:#if move form has been completed
            if request.POST["NewX"]:
                if request.POST["NewY"]:
                    for point in queryset:
                        point.geom.x=float(request.POST["NewX"])
                        point.geom.y=float(request.POST["NewY"])
                        point.save()
                        self.message_user(request,"Point Succesfully Moved")
                else:
                    return render_move_form()
            else:
                return render_move_form()
        else:#if move form has NOT been completed
            return render_move_form()
    move_selected.short_description = "Move the selected points."


#####################
## Taxonomy Admin  ##
#####################

class taxonomyAdmin(admin.ModelAdmin):
    list_display = ("id","rank","tax_class","tax_order","family","subfamily","tribe","genus")
    search_fields = ("tax_class","tax_order","family","subfamily","tribe","genus")
    list_filter = ("rank",)


############################
## Register Admin Classes ##
############################

admin.site.register(drp_biology, biologyAdmin)
admin.site.register(drp_hydrology, hydrologyAdmin)
admin.site.register(drp_locality, localityAdmin)
admin.site.register(drp_occurrence, occurrenceAdmin)
admin.site.register(drp_taxonomy, taxonomyAdmin)