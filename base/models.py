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
