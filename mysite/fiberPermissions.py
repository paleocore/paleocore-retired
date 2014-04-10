"""
    >>> from django.contrib.auth.models import User
    >>> u = User.objects.get(username='example-user')
    >>> from fiber.models import Page
    >>> p = Page.objects.get(title='A')
"""

from django.contrib.auth.models import User
from fiber.permissions import Permissions
from fiber.models import Image, File, Page, PageContentItem, ContentItem


class FiberPermissions(Permissions):

    def is_fiber_editor(self, user):
        """
        Determines if the user is allowed to see the Fiber admin interface.
        """
        return user.is_superuser
