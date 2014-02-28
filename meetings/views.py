

# Create your views here.
# Create your views here.
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic
from django.utils import timezone

from models import Poll, Choice



class IndexView(generic.ListView):
    template_name = 'meetings/index.html'
    context_object_name = 'latest_poll_list'

    def get_queryset(self):
        """Return the last five published polls."""
        return Poll.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')[:5]