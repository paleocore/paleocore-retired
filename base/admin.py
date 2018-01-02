from django.contrib import admin
from base.models import PaleocoreUser
from django.template import loader, RequestContext
from django.contrib.admin import helpers
from django.contrib.gis.db import models
from django.http import HttpResponse
from django.core.mail import send_mass_mail
from django.forms import TextInput, Textarea  # import custom form widgets
from django.contrib.gis.admin import OSMGeoAdmin


class DGGeoAdmin(OSMGeoAdmin):
    """
    Modified Geographic Admin Class using Digital Globe basemaps
    GeoModelAdmin -> OSMGeoAdmin -> DGGeoAdmin
    """
    map_template = 'gis/admin/bing.html'


class PaleocoreUserAdmin(admin.ModelAdmin):
    def email(self):
        return self.user.email

    def last_name(self):
        return self.user.last_name

    def first_name(self):
        return self.user.first_name

    list_filter = ['send_emails', 'institution']
    search_fields = ('last_name', 'first_name')
    list_display = [first_name, last_name, email, 'send_emails']
    actions = ['send_emails']

    def send_emails(self, request, queryset):
        """
        A function that defines a custom admin action to send bulk emails to selected users. The function calls a
        custom template called email.html
        """
        return_url = "/admin/paleoschema/paleocoreuser/"
        if 'apply' in request.POST:  # check if the email form has been completed
            # code to send emails. We use send_mass_email, which requires a four-part tuple
            # containing the subject, message, from_address and a list of to addresses.
            if 'subject' in request.POST:
                if request.POST["subject"] == '':
                    self.message_user(request, "Message is missing a subject")
                    t = loader.get_template("base/email.html")
                    c = RequestContext(request, {'returnURL': return_url, 'emails': queryset,
                                                 'action_checkbox_name': helpers.ACTION_CHECKBOX_NAME, })
                    return HttpResponse(t.render(c))
                else:
                    subject = request.POST["subject"]
            if 'message' in request.POST:
                if request.POST["message"] == '':
                    self.message_user(request, "Message is empty")
                    t = loader.get_template("base/email.html")
                    c = RequestContext(request, {'returnURL': return_url, 'emails': queryset,
                                                 'action_checkbox_name': helpers.ACTION_CHECKBOX_NAME, })
                    return HttpResponse(t.render(c))
                message = request.POST["message"]
            from_address = 'paleocore@paleocore.org'
            messages_list = []
            # build the to list by iterating over records in queryset from selected records
            for i in queryset:
                if i.user.email:
                    to_address = [i.user.email]
                    message_tuple = (subject, message, from_address, to_address)
                    messages_list.append(message_tuple)
            # slice off the first element of tuple which is empty
            messages_tuple = tuple(messages_list)
            send_mass_mail(messages_tuple, fail_silently=False)

            self.message_user(request, "Mail sent successfully ")
        else:
            t = loader.get_template('base/email.html')
            c = RequestContext(request, {'returnURL': return_url, 'emails': queryset,
                                         'action_checkbox_name': helpers.ACTION_CHECKBOX_NAME, })
            return HttpResponse(t.render(c))
    send_emails.short_description = "Send an email to selected members"


####################################
# PaleoCore Default Admin Settings #
####################################

default_list_display = ('barcode', 'field_number', 'catalog_number', 'basis_of_record', 'item_type',
                        'collecting_method', 'collector', 'item_scientific_name', 'item_description', 'year_collected',
                        'in_situ', 'problem', 'easting', 'northing')
default_list_per_page = 1000
default_read_only_fields = ('id', 'point_x', 'point_y', 'easting', 'northing', 'date_last_modified')
default_admin_fieldsets = (
    ('Curatorial', {
        'fields': [('barcode', 'catalog_number', 'id'),
                   ('field_number', 'year_collected', 'date_last_modified'),
                   ('collection_code', 'item_number', 'item_part')]
    }),

    ('Occurrence Details', {
        'fields': [('basis_of_record', 'item_type', 'disposition', 'preparation_status'),
                   ('collecting_method', 'finder', 'collector', 'individual_count'),
                   ('item_description', 'item_scientific_name', 'image'),
                   ('problem', 'problem_comment'),
                   ('remarks', )],
    }),
    ('Taphonomic Details', {
        'fields': [('weathering', 'surface_modification')],
    }),
    ('Provenience', {
        'fields': [('analytical_unit',),
                   ('in_situ',),
                   # The following fields are based on methods and must be included in the read only field list
                   ('point_x', 'point_y'),
                   ('easting', 'northing'),
                   ('geom', )],
    })
)
default_list_filter = ['basis_of_record', 'year_collected', 'item_type', 'collector', 'problem', 'field_number',
                       'disposition']
default_list_editable = ['problem', 'disposition']
default_search_fields = ('id', 'item_scientific_name', 'item_description', 'barcode', 'catalog_number',
                         'finder', 'collector')
default_list_display_links = ['barcode']

default_biology_inline_fieldsets = (

    ('Element', {
        'fields': (('side',), )
    }),

    ('Taxonomy', {
        'fields': (('taxon',), ("id",))
    }),
)

default_biology_admin_fieldsets = (
    ('Taxonomy', {
        'fields': (('taxon', 'identification_qualifier'),)
    }),
)


class PaleoCoreBiologyAdmin(DGGeoAdmin):
    list_display = default_list_display
    list_per_page = default_list_per_page
    list_display_links = default_list_display_links
    list_filter = default_list_filter
    search_fields = default_search_fields+('taxon__name',)
    readonly_fields = default_read_only_fields
    fieldsets = default_admin_fieldsets+default_biology_admin_fieldsets
    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'size': '25'})},
        models.TextField: {'widget': Textarea(attrs={'rows': 4, 'cols': 40})},
    }

    def get_search_results(self, request, queryset, search_term):
        # search_term is what you input in admin site
        # queryset is search results
        queryset, use_distinct = super(PaleoCoreBiologyAdmin, self).get_search_results(request, queryset, search_term)

        try:
            search_term_as_int = int(search_term)
        except ValueError:
            pass
        else:
            queryset |= self.model.objects.filter(barcode=search_term_as_int)
        return queryset, use_distinct


class PaleoCoreOccurrenceAdmin(DGGeoAdmin):
    list_display = default_list_display
    list_display_links = default_list_display_links
    list_filter = default_list_filter
    search_fields = default_search_fields
    readonly_fields = default_read_only_fields
    fieldsets = default_admin_fieldsets
    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'size': '25'})},
        models.TextField: {'widget': Textarea(attrs={'rows': 4, 'cols': 40})},
    }

    def get_search_results(self, request, queryset, search_term):
        # search_term is what you input in admin site
        # queryset is search results
        queryset, use_distinct = super(PaleoCoreOccurrenceAdmin, self).get_search_results(request,
                                                                                          queryset, search_term)

        try:
            search_term_as_int = int(search_term)
        except ValueError:
            pass
        else:
            queryset |= self.model.objects.filter(barcode=search_term_as_int)
        return queryset, use_distinct


class PaleoCoreLocalityAdmin(DGGeoAdmin):
    list_display = ("collection_code", "paleolocality_number", "paleo_sublocality")
    list_filter = ("collection_code",)
    search_fields = ("paleolocality_number",)


class TaxonomyAdmin(admin.ModelAdmin):
    list_display = ('__unicode__', 'rank', 'full_name')
    readonly_fields = ['id']
    fields = ['id', 'name', 'parent', 'rank']
    search_fields = ['name']
    list_filter = ['rank']


class IDQAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'qualified']


class TaxonRankAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'ordinal']


##################
# Register Admins #
###################
admin.site.register(PaleocoreUser, PaleocoreUserAdmin)
