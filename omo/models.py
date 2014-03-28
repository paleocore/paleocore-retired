from django.db import models

class omo(models.Model):
    locality_letter = models.CharField(max_length=200, blank=True, null=True)
    locality_number = models.CharField(max_length=200, blank=True, null=True)
    locality_number_sub = models.CharField(max_length=200, blank=True, null=True)
    specimen_number = models.IntegerField(blank=True, null=True)
    specimen_number_sub = models.CharField(max_length=200, blank=True, null=True)
    excavation_number = models.CharField(max_length=200, blank=True, null=True)
    is_excavation = models.CharField(max_length=200, blank=True, null=True)
    year_recovered = models.IntegerField(blank=True, null=True)
    formation = models.CharField(max_length=200, blank=True, null=True)
    member = models.CharField(max_length=200, blank=True, null=True)
    unit = models.IntegerField(blank=True, null=True)
    upper_error = models.CharField(max_length=200, blank=True, null=True)
    lower_error = models.CharField(max_length=200, blank=True, null=True)
    family_code = models.CharField(max_length=200, blank=True, null=True)
    genus_qualifier = models.CharField(max_length=200, blank=True, null=True)
    genus = models.CharField(max_length=200, blank=True, null=True)
    tribe_genus_code = models.IntegerField(blank=True, null=True)
    side = models.CharField(max_length=200, blank=True, null=True)
    body_element = models.CharField(max_length=200, blank=True, null=True)
    body_element_code = models.CharField(max_length=200, blank=True, null=True)
    identifier = models.CharField(max_length=200, blank=True, null=True)
    year_identified = models.CharField(max_length=200, blank=True, null=True)
    location = models.CharField(max_length=200, blank=True, null=True)
    sent_to_addis = models.CharField(max_length=200, blank=True, null=True)
    individual = models.CharField(max_length=200, blank=True, null=True)
    individual_number = models.CharField(max_length=200, blank=True, null=True)
    sex = models.CharField(max_length=200, blank=True, null=True)
    sector_number = models.IntegerField(blank=True, null=True)
    remarks = models.CharField(max_length=200, blank=True, null=True)
    species = models.CharField(max_length=200, blank=True, null=True)
    species_qualifier = models.CharField(max_length=200, blank=True, null=True)
    element_part = models.CharField(max_length=200, blank=True, null=True)
    subunit = models.CharField(max_length=200, blank=True, null=True)

    @staticmethod
    def fields_to_display():
        fields = ('year_recovered', 'body_element', 'genus', 'species')
        return fields

    def __unicode__(self):
        return str(self.body_element)