from django.contrib import admin
from taxonomy.models import Taxon, TaxonRank, IdentificationQualifier

class TaxonAdmin(admin.ModelAdmin):
    list_display = ('__unicode__', 'rank', 'full_name')

admin.site.register(TaxonRank)
admin.site.register(Taxon, TaxonAdmin)
admin.site.register(IdentificationQualifier)
