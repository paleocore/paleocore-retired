from django.db import models
from django.contrib.auth.models import User

############################################
# PaleoCoreUser
############################################
class PaleocoreUser(models.Model):
    """
    This class "extends" the default Django user class. It adds Paleocore
    specific fields to the user database, allowing us to use the auth
    system to track and manage paleocore users rather than constructing a separate
    membership database.

    This class is coupled with a custom PaleoCoreUserAdmin module in base.admin.py
    """
    user = models.OneToOneField(User)

    # other fields
    institution = models.CharField(max_length=255, null=True, blank=True)
    department = models.CharField(max_length=255, null=True, blank=True)
    send_emails = models.BooleanField(default=True)

    def __unicode__(self):
        return self.user.first_name + " " + self.user.last_name

    class Meta:
        db_table = "paleocore_user"
        verbose_name_plural = "User Info"
        verbose_name = "User Info"
        ordering= ["user__last_name",]


class TaxonRank(models.Model):
    name = models.CharField(null=False, blank=False, max_length=50, unique=True)
    plural = models.CharField(null=False, blank=False, max_length=50, unique=True)
    ordinal = models.IntegerField(null=False, blank=False, unique=True)

    def __unicode__(self):
        return str(self.name)

    class Meta:
        abstract = True
        verbose_name = "Taxon Rank"


class Taxon(models.Model):
    name = models.CharField(null=False, blank=False, max_length=255, unique=False)
    # can't inlcude foreign key to an abstract model

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

    def full_lineage(self):
        """
        Get a list of taxon object representing the full lineage hierarchy
        :return: list of taxon objects ordered highest rank to lowest
        """
        if self.parent is None:
            return [self]
        if self.parent.parent is None:
            return [self]
        else:
            return self.parent.full_lineage()+[self]

    def __unicode__(self):
        if self.rank.name == 'Species' and self.parent:
            return "[" + self.rank.name + "] " + self.parent.name + " " + self.name
        else:
            return "[" + self.rank.name + "] " + str(self.name)

    class Meta:
        abstract = True
        verbose_name = "LGRP Taxon"
        verbose_name_plural = "taxa"
        ordering = ['rank__ordinal', 'name']


class IdentificationQualifier(models.Model):
    name = models.CharField(null=False, blank=True, max_length=15, unique=True)
    qualified = models.BooleanField()

    def __unicode__(self):
        return self.name

    class Meta:
        abstract = True