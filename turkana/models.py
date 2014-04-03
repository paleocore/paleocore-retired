from django.db import models


class Turkana(models.Model):
    museum = models.CharField(max_length=200, blank=True, null=True)
    specimen_prefix = models.CharField(max_length=200, blank=True, null=True)
    specimen_number = models.IntegerField(blank=True, null=True)
    specimen_suffix = models.CharField(max_length=200, blank=True, null=True)
    field_number = models.CharField(max_length=200, blank=True, null=True)
    record_number = models.IntegerField(blank=True, null=True)
    year_found = models.IntegerField(blank=True, null=True)
    study_area = models.CharField(max_length=200, blank=True, null=True)
    collecting_area = models.CharField(max_length=200, blank=True, null=True)
    locality = models.CharField(max_length=200, blank=True, null=True)
    air_photo = models.CharField(max_length=200, blank=True, null=True)
    x_coordinate = models.DecimalField(max_digits=50, decimal_places=20, blank=True, null=True)
    y_coordinate = models.DecimalField(max_digits=50, decimal_places=20, blank=True, null=True)
    gps_datum = models.DecimalField(max_digits=50, decimal_places=20, blank=True, null=True)
    latitude = models.DecimalField(max_digits=50, decimal_places=20, blank=True, null=True)
    longitude = models.DecimalField(max_digits=50, decimal_places=20, blank=True, null=True)
    formation = models.CharField(max_length=200, blank=True, null=True)
    member = models.CharField(max_length=200, blank=True, null=True)
    level = models.CharField(max_length=200, blank=True, null=True)
    stratigraphic_unit = models.CharField(max_length=200, blank=True, null=True)
    stratigraphic_code = models.CharField(max_length=200, blank=True, null=True)
    excavation = models.CharField(max_length=200, blank=True, null=True)
    square_number = models.CharField(max_length=200, blank=True, null=True)
    age_estimate = models.IntegerField(blank=True, null=True)
    age_max = models.IntegerField(blank=True, null=True)
    age_min = models.IntegerField(blank=True, null=True)
    matrix = models.CharField(max_length=200, blank=True, null=True)
    weathering = models.CharField(max_length=200, blank=True, null=True)
    surface = models.CharField(max_length=200, blank=True, null=True)
    color = models.CharField(max_length=200, blank=True, null=True)
    identifier = models.CharField(max_length=200, blank=True, null=True)
    year_identified = models.IntegerField(blank=True, null=True)
    publication_author = models.CharField(max_length=200, blank=True, null=True)
    year_published = models.IntegerField(blank=True, null=True)
    year_published_suffix = models.CharField(max_length=200, blank=True, null=True)
    class_field = models.CharField("class", max_length=200, blank=True, null=True)
    order = models.CharField(max_length=200, blank=True, null=True)
    family = models.CharField(max_length=200, blank=True, null=True)
    family_code = models.IntegerField(blank=True, null=True)
    subfamily = models.CharField(max_length=200, blank=True, null=True)
    tribe = models.CharField(max_length=200, blank=True, null=True)
    tribe_code = models.IntegerField(blank=True, null=True)
    genus_qualifier = models.CharField(max_length=200, blank=True, null=True)
    genus = models.CharField(max_length=200, blank=True, null=True)
    genus_code = models.IntegerField(blank=True, null=True)
    species_qualifier = models.CharField(max_length=200, blank=True, null=True)
    species = models.CharField(max_length=200, blank=True, null=True)
    body_element = models.CharField(max_length=200, blank=True, null=True)
    body_element_code = models.IntegerField(blank=True, null=True)
    part_description = models.CharField(max_length=200, blank=True, null=True)
    side = models.CharField(max_length=200, blank=True, null=True)
    sex = models.CharField(max_length=200, blank=True, null=True)
    age = models.IntegerField(blank=True, null=True)
    body_size = models.CharField(max_length=200, blank=True, null=True)
    remarks = models.CharField(max_length=500, blank=True, null=True)
    date_entered = models.IntegerField(blank=True, null=True)
    signed = models.CharField(max_length=200, blank=True, null=True)
    storage_location = models.CharField(max_length=200, blank=True, null=True)
    li1 = models.CharField(max_length=1, blank=True, null=True)
    li2 = models.CharField(max_length=1, blank=True, null=True)
    li3 = models.CharField(max_length=1, blank=True, null=True)
    lc = models.CharField(max_length=1, blank=True, null=True)
    lp1 = models.CharField(max_length=1, blank=True, null=True)
    lp2 = models.CharField(max_length=1, blank=True, null=True)
    lp3 = models.CharField(max_length=1, blank=True, null=True)
    lp4 = models.CharField(max_length=1, blank=True, null=True)
    lm1 = models.CharField(max_length=1, blank=True, null=True)
    lm2 = models.CharField(max_length=1, blank=True, null=True)
    lm3 = models.CharField(max_length=1, blank=True, null=True)
    ui1 = models.CharField(max_length=1, blank=True, null=True)
    ui2 = models.CharField(max_length=1, blank=True, null=True)
    ui3 = models.CharField(max_length=1, blank=True, null=True)
    uc = models.CharField(max_length=1, blank=True, null=True)
    up1 = models.CharField(max_length=1, blank=True, null=True)
    up2 = models.CharField(max_length=1, blank=True, null=True)
    up3 = models.CharField(max_length=1, blank=True, null=True)
    up4 = models.CharField(max_length=1, blank=True, null=True)
    um1 = models.CharField(max_length=1, blank=True, null=True)
    um2 = models.CharField(max_length=1, blank=True, null=True)
    um3 = models.CharField(max_length=1, blank=True, null=True)
    ldi1 = models.CharField(max_length=1, blank=True, null=True)
    ldi2 = models.CharField(max_length=1, blank=True, null=True)
    ldi3 = models.CharField(max_length=1, blank=True, null=True)
    ldc = models.CharField(max_length=1, blank=True, null=True)
    ldp1 = models.CharField(max_length=1, blank=True, null=True)
    ldp2 = models.CharField(max_length=1, blank=True, null=True)
    ldp3 = models.CharField(max_length=1, blank=True, null=True)
    ldp4 = models.CharField(max_length=1, blank=True, null=True)
    udi1 = models.CharField(max_length=1, blank=True, null=True)
    udi2 = models.CharField(max_length=1, blank=True, null=True)
    udi3 = models.CharField(max_length=1, blank=True, null=True)
    udc = models.CharField(max_length=1, blank=True, null=True)
    udp1 = models.CharField(max_length=1, blank=True, null=True)
    udp2 = models.CharField(max_length=1, blank=True, null=True)
    udp3 = models.CharField(max_length=1, blank=True, null=True)
    udp4 = models.CharField(max_length=1, blank=True, null=True)
    area_modifier = models.CharField(max_length=200, blank=True, null=True)

    @staticmethod
    def fields_to_display():
        fields = ('year_found', 'study_area', 'formation', 'member', 'genus', 'species', 'body_element')
        return fields

    def __unicode__(self):
        return str(self.museum) + "-" +  str(self.specimen_prefix) + "-" +  str(self.specimen_number)
