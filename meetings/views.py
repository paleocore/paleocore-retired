# Create your views here.
# Using class based views.

from django.shortcuts import get_object_or_404
from django.views import generic
from models import *
from django.core.urlresolvers import reverse
from fiber.views import FiberPageMixin

class IndexView(FiberPageMixin, generic.ListView):
    template_name = 'meetings/abstracts.html'
    context_object_name = 'abstracts'

    def get_queryset(self):
        # build a query set of abstracts for a given meeting. The meeting_name is passed from meetings/urls.py
        self.meeting = get_object_or_404(Meeting, title=self.kwargs["meeting_name"])

        """Return a list of abstracts for the current meeting"""
        return Abstract.objects.filter(meeting=self.meeting)

    def get_fiber_page_url(self):
        return reverse('meetings:index', args=[self.meeting])