from django.contrib import admin
from origins.models import *
from base.admin import DGGeoAdmin
from django.core.urlresolvers import reverse
from django.utils.html import format_html
from django.contrib.gis.measure import Distance


@staticmethod
def get_latitude(obj):
    if obj.geom:
        return obj.geom.y
    else:
        return None

@staticmethod
def get_longitude(obj):
    if obj.geom:
        return obj.geom.x
    else:
        return None


class ReferenceAdmin(admin.ModelAdmin):
    list_display = ['id', 'reference_no', 'author1last', 'reftitle']
    search_fields = ['reference_no', 'author1init', 'author1last', 'author2init', 'author2last',
                     'otherauthors', 'pubyr', 'reftitle', 'pubtitle', 'editors', 'pubvol', 'publication_type']
    list_filter = ['publication_type']
    list_per_page = 200


class ContextInline(admin.TabularInline):
    model = Context
#    fields = ['id', 'collection_name', 'collection_subset', 'collection_aka', 'n_occs', 'formation', 'member',
#              'max_ma', 'min_ma']


class SiteAdmin(DGGeoAdmin):
    list_display = ['id', 'name', 'verbatim_collection_name', 'verbatim_early_interval',
                    'verbatim_late_interval', 'verbatim_max_ma', 'verbatim_min_ma', 'verbatim_reference_no']
    readonly_fields = ['get_latitude', 'get_longitude']
    search_fields = list_display
    list_filter = ['mio_plio']
    list_per_page = 500
    # inlines = [ContextInline]

    fieldsets = [
        ('Occurrence Details', {
            'fields': [('name', 'source', 'mio_plio')],
        }),
        ('Verbatim', {
            'fields': ['verbatim_collection_no', 'verbatim_record_type', 'verbatim_formation',
                       'verbatim_lng', 'verbatim_lat', 'verbatim_collection_name', 'verbatim_collection_subset',
                       'verbatim_collection_aka', 'verbatim_n_occs', 'verbatim_early_interval',
                       'verbatim_late_interval', 'verbatim_max_ma', 'verbatim_min_ma', 'verbatim_reference_no'],
            'classes': ['collapse'],
        }),
        ('Location', {
            'fields': [('get_latitude', 'get_longitude'), ('geom',)]
        }),
    ]

    @staticmethod
    def get_latitude(obj):
        if obj.geom:
            return obj.geom.y
        else:
            return None

    @staticmethod
    def get_longitude(obj):
        if obj.geom:
            return obj.geom.x
        else:
            return None


class ContextAdmin(DGGeoAdmin):
    list_display = ['id', 'name', 'site_link', 'geological_formation', 'geological_member',
                    'older_interval', 'younger_interval', 'max_age', 'min_age', 'best_age']
    search_fields = ['id', 'name', 'geological_formation', 'geological_member',
                    'older_interval', 'younger_interval', 'max_age', 'min_age', 'best_age']
    list_filter = ['mio_plio']
    list_per_page = 500
    fieldsets = [
        ('Context Details', {
            'fields': [('name', 'site', 'mio_plio', 'source')],
        }),
        ('Stratigraphy', {
            'fields': [('geological_formation', 'geological_member',)],
        }),
        ('Geochronology', {
            'fields': [('older_interval', 'younger_interval',),
                       ('max_age', 'min_age', 'best_age'),
                       ('mio_plio')],
        }),
        ('Verbatim', {
            'fields': ['verbatim_collection_no', 'verbatim_record_type', 'verbatim_formation',
                       'verbatim_lng', 'verbatim_lat', 'verbatim_collection_name', 'verbatim_collection_subset',
                       'verbatim_collection_aka', 'verbatim_n_occs', 'verbatim_early_interval',
                       'verbatim_late_interval', 'verbatim_max_ma', 'verbatim_min_ma', 'verbatim_reference_no'],
            'classes': ['collapse'],
        }),
        ('Location', {'fields': ['geom']})
    ]

    def site_link(self, obj):
        if obj.site:
            url = reverse('admin:origins_site_change', args=(obj.site.id,))
            return format_html('<a href={}>{}</a>'.format(url, obj.site))
        else:
            return None
    site_link.admin_order_field = 'context'
    site_link.short_description = 'Site'

    def get_form(self, request, obj=None, **kwargs):
        if obj:
            self.current_obj = obj
        return super(ContextAdmin, self).get_form(request, obj, **kwargs)

    def formfield_for_foreignkey(self, db_field, request=None, **kwargs):
        """
        Simplify choice list for context to only those context objects occurring at the site.
        :param db_field:
        :param request:
        :param kwargs:
        :return:
        """

        if db_field.name == "site":
            kwargs["queryset"] = Site.objects.filter(geom__distance_lte=(self.current_obj.geom, Distance(m=10000)))
        return super(ContextAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)


class FossilElementInline(admin.TabularInline):
    model = FossilElement
    fields = ['skeletal_element', 'skeletal_element_subunit', 'skeletal_element_subunit_descriptor',
              'skeletal_element_side', 'skeletal_element_position', 'skeletal_element_complete',
              'skeletal_element_class']
    extra = 0


class ReferenceInline(admin.TabularInline):
    model = Reference.fossil.through
    extra = 1


class PhotosInline(admin.StackedInline):
    model = Photo
    extra = 0
    readonly_fields = ('thumbnail',)
    fieldsets = [
              ('Photos', {
                 'fields': [('image', 'thumbnail')]})]


class FossilAdmin(admin.ModelAdmin):
    list_display = ['id', 'catalog_number', 'verbatim_Locality', 'context__site', 'context_link', 'context__formation',
                    'country', 'nickname', 'context__max_age', 'context__min_age', 'context__best_age']
    list_filter = ['origins', 'continent', 'holotype']
    list_display_links = ['id', 'catalog_number']
    search_fields = ['place_name', 'country', 'locality',
                     'fossil_element__skeletal_element']
    readonly_fields = ['element_count', 'aapa', 'id']
    #fields = ['id', 'catalog_number', 'nickname', 'place_name', 'verbatim_HomininElementNotes', 'country',
    #          'locality', 'continent', 'context']
    list_per_page = 200
    inlines = [
        # ReferenceInline, # the number of references significantly slows page loads
        FossilElementInline,
        PhotosInline
    ]

    fieldsets = [
        ('Fossil Details', {
            'fields': [('id', 'catalog_number', 'guid', 'uuid', 'organism_id'),
                       ('nickname', 'place_name'),
                       ('holotype', 'lifestage', 'sex'),
                       ('origins')],
        }),
        ('Verbatim', {
            'fields': [('verbatim_PlaceName', 'verbatim_HomininElement'),
                       ('verbatim_HomininElementNotes',),
                       ('verbatim_SkeletalElement', 'verbatim_SkeletalElementSubUnit',
                        'verbatim_SkeletalElementSubUnitDescriptor'),
                       ('verbatim_SkeletalElementSide',
                        'verbatim_SkeletalElementPosition', 'verbatim_SkeletalElementComplete',
                        'verbatim_SkeletalElementClass'),
                       ('verbatim_Locality', 'verbatim_Country')
                       ],
            'classes': ['collapse'],
        }),
        ('Location', {
            'fields': [('locality', 'country', 'continent', 'context')]
        }),
        ('Image', {
            'fields': [('image')]
        })
    ]

    def context__formation(self, obj):
        """
        Function to get the formation from via the context
        :param obj:
        :return:
        """
        if obj.context:
            return obj.context.geological_formation
        else:
            return None
    context__formation.admin_order_field = 'context'
    context__formation.short_description = 'Geo formation'

    def context_link(self, obj):
        if obj.context:
            url = reverse('admin:origins_context_change', args=(obj.context.id,))
            return format_html('<a href={}>{}</a>'.format(url, obj.context))
        else:
            return None
    context_link.admin_order_field = 'context'
    context_link.short_description = 'Context'

    def context__site(self, obj):
        """
        Function to get site information via the context. Returns a link to the site change detail page.
        :param obj:
        :return:
        """
        if obj.context and obj.context.site:
            site_url = reverse('admin:origins_site_change', args=(obj.context.site.id,))
            return format_html('<a href={}>{}</a>'.format(site_url, obj.context.site))
        else:
            return None
    context__site.admin_order_field = 'context'
    context__site.short_description = 'Site'

    def context__max_age(self, obj):
        """
        Function to get age via context.
        :param obj:
        :return:
        """
        if obj.context and obj.context.max_age:
            return obj.context.max_age
        else:
            return None
    context__max_age.short_description = "Max age"

    def context__min_age(self, obj):
        """
        Function to get age via context.
        :param obj:
        :return:
        """
        if obj.context and obj.context.min_age:
            return obj.context.min_age
        else:
            return None
    context__min_age.short_description = "Min age"

    def context__best_age(self, obj):
        """
        Function to get age via context.
        :param obj:
        :return:
        """
        if obj.context and obj.context.best_age:
            return obj.context.best_age
        else:
            return None
    context__min_age.short_description = "Best age"

    def get_form(self, request, obj=None, **kwargs):
        self.current_obj = None
        if obj:
            self.current_obj = obj
        return super(FossilAdmin, self).get_form(request, obj, **kwargs)

    def formfield_for_foreignkey(self, db_field, request=None, **kwargs):
        """
        Simplify choice list for context to only those context objects occurring at the site.
        :param db_field:
        :param request:
        :param kwargs:
        :return:
        """
        if db_field.name == "context":
            if self.current_obj:
                if self.current_obj.context and self.current_obj.context.site:
                    kwargs["queryset"] = Context.objects.filter(site=self.current_obj.context.site)
            else:
                kwargs["queryset"] = Context.objects.all()
            # If ever I add geom for fossil specimens, then query below useful to find closest context objects
            # nearby = Context.objects.filter(geom__distance_lte=(self.geom, D(m=10000)))[:5]
        return super(FossilAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)


# Register your models here.
admin.site.register(Context, ContextAdmin)
admin.site.register(Reference, ReferenceAdmin)
admin.site.register(Fossil, FossilAdmin)
#admin.site.register(Fossil, CleanerAdmin)
admin.site.register(Site, SiteAdmin)
