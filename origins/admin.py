from django.contrib import admin
from origins.models import *
from base.admin import DGGeoAdmin


class ReferenceAdmin(admin.ModelAdmin):
    list_display = ['id', 'reference_no', 'author1last', 'reftitle']
    search_fields = ['reference_no', 'author1init', 'author1last', 'author2init', 'author2last',
                     'otherauthors', 'pubyr', 'reftitle', 'pubtitle', 'editors', 'pubvol', 'publication_type']
    list_filter = ['publication_type']
    list_per_page = 200


class SiteAdmin(DGGeoAdmin):
    list_display = ['id', 'collection_no', 'collection_name', 'collection_aka',
                    'early_interval', 'late_interval', 'max_ma', 'min_ma', 'reference_no']
    search_fields = list_display
    list_filter = ['mio_plio']
    list_per_page = 500


class ContextAdmin(DGGeoAdmin):
    list_display = ['id', 'collection_no', 'collection_name', 'formation', 'collection_aka', 'n_occs',
                    'early_interval', 'late_interval', 'max_ma', 'min_ma', 'reference_no']
    search_fields = list_display
    list_filter = ['mio_plio']
    list_per_page = 500


class FossilElementAdmin(admin.ModelAdmin):
    list_display = ['id', 'PlaceName', 'Country', 'Locality', 'HomininElement', 'SkeletalElement']
    list_filter = ['continent', 'Country', 'SkeletalElement']
    search_fields = ['PlaceName', 'Country', 'Locality', 'HomininElement', 'SkeletalElement']

    list_per_page = 200


class FossilElementInline(admin.TabularInline):
    model = FossilElement
    fields = ['SkeletalElement', 'SkeletalElementSubUnit', 'SkeletalElementSubUnitDescriptor', 'SkeletalElementSide',
              'SkeletalElementPosition', 'SkeletalElementComplete', 'SkeletalElementClass']
    extra = 0


class ContextInline(admin.TabularInline):
    model = Context
#    fields = ['id', 'collection_name', 'collection_subset', 'collection_aka', 'n_occs', 'formation', 'member',
#              'max_ma', 'min_ma']


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
    list_display = ['id', 'locality', 'country', 'catalog_number', 'nickname',
                    'element_count', 'context', 'aapa', 'holotype']
    list_filter = ['continent', 'Country', 'Locality', 'holotype']
    search_fields = ['PlaceName', 'Country', 'Locality', 'HomininElement', 'SkeletalElement']
    readonly_fields = ['element_count', 'aapa', 'id']
    fields = ['id', 'catalog_number', 'nickname', 'PlaceName', 'HomininElement', 'HomininElementNotes', 'Country',
              'Locality', 'continent', 'context']
    list_per_page = 200
    inlines = [
        ReferenceInline,
        FossilElementInline,
        PhotosInline
    ]


class CleanerAdmin(FossilAdmin):
    def formfield_for_foreignkey(self, db_field, request=None, **kwargs):
        if db_field.name == "context":
            request_path = request.path
            fossil_id = request_path.split('/')[-2]
            fossil = Fossil.objects.get(pk=fossil_id)
            kwargs["queryset"] = Context.objects.filter(collection_name__contains=fossil.Locality)
        return super(FossilAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)


# Register your models here.
admin.site.register(Context, ContextAdmin)
admin.site.register(Reference, ReferenceAdmin)
admin.site.register(Fossil, FossilAdmin)
# admin.site.register(Fossil, CleanerAdmin)
admin.site.register(Site, SiteAdmin)
