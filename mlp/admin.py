from django.contrib import admin
from models import Occurrence
from django.forms import TextInput, Textarea  # import custom form widgets
from django.contrib.gis.db import models

# Register your models here.


occurrence_fieldsets =(
('Curatorial', {
'fields': (('barcode','catalognumber'),
           ("objectid",'fieldnumber','yearcollected',"datelastmodified"),
           ("collectioncode","paleolocalitynumber","itemnumber","itempart"))
}),

('Occurrence Details', {
'fields': (('basisofrecord','itemtype','disposition','preparationstatus'),
           ('itemdescription','itemscientificname'),
           ('remarks'))
}),
('Provenience', {
'fields': (#("strat_upper","distancefromupper"),
           #("strat_lower","distancefromlower"),
           #("strat_found","distancefromfound"),
           #("strat_likely","distancefromlikely"),
           ("analyticalunit","analyticalunit2","analyticalunit3"),
           ("insitu","ranked"),
           ("stratigraphicmember",),
           ("point_x","point_y"),
           ('shape'))
}),
)

class occurrenceAdmin(admin.ModelAdmin):
    list_display = ('objectid', 'stratigraphicmember', "catalognumber", "barcode", 'basisofrecord', 'itemtype',
                    'collector', "itemscientificname", "itemdescription", "point_x", "point_y", "yearcollected",
                    "fieldnumber", "datelastmodified")

    #note: autonumber fields like objectid are not editable, and can't be added to fieldsets unless specified as read only.
    #also, any dynamically created fields (e.g. point_X) in models.py must be declared as read only to be included in fieldset or fields
    readonly_fields = ("objectid", "fieldnumber", "point_x", "point_y", "catalognumber", "datelastmodified")

    list_filter = ["basisofrecord","yearcollected","stratigraphicmember","collectioncode","itemtype"]
    search_fields = ("objectid","itemscientificname","barcode","catalognumber")
    #inlines = (biologyInline,) - no biology table...yet  TODO Add biology table
    fieldsets = occurrence_fieldsets
    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'size': '25'})},
        models.TextField: {'widget': Textarea(attrs={'rows': 4, 'cols': 40})},
    }


############################
## Register Admin Classes ##
############################
admin.site.register(Occurrence, occurrenceAdmin)
