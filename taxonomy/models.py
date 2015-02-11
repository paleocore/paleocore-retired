from django.contrib.gis.db import models

class TaxonRank(models.Model):
    name = models.CharField(null=False, blank=False, max_length=50, unique=True)
    plural = models.CharField(null=False, blank=False, max_length=50, unique=True)
    ordinal = models.IntegerField(null=False, blank=False, unique=True)

    def __unicode__(self):
        return str(self.name)

    class Meta:
        verbose_name = "Taxon Rank"

class IdentificationQualifier(models.Model):
    name = models.CharField(null=False, blank=True, max_length=15, unique=True)
    qualified = models.BooleanField()

class Taxon(models.Model):
    name = models.CharField(null=False, blank=False, max_length=255, unique=False)
    parent = models.ForeignKey('self', null=True, blank=True)
    rank = models.ForeignKey(TaxonRank)

    def parent_rank(self):
        return self.parent.rank.name

    def rank_ordinal(self):
        return self.rank.ordinal

    def parent_name(self):
        if self.parent is None:
            return "NA"
        else:
            return self.parent.name

    def full_name(self):
        if self.parent is None:
            return self.name
        elif self.parent.parent is None:
            return self.name
        else:
            return self.parent.full_name() + ", " + self.name

    def __unicode__(self):
        if self.rank.name == 'Species':
            return "[" + self.rank.name + "] " + self.parent.name + " " + self.name
        else:
            return "[" + self.rank.name + "] " + str(self.name)

    class Meta:
        verbose_name = "Taxon"
        verbose_name_plural = "taxa"
        ordering = ['rank__ordinal', 'name']