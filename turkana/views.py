from django.shortcuts import render_to_response
from django.template import RequestContext


def turkana_home(request):

     return render_to_response('turkana_home.html',
                                {},
                                context_instance=RequestContext(request))

