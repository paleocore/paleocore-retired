from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response, RequestContext
from tastypie.models import ApiKey

@login_required(login_url="/login/")
def get_or_create_API_key(request):
    try:
        api_key = ApiKey.objects.get(user=request.user)
        api_key.key = None
        api_key.save()
        ##note, setting key to None and then saving creates a new key
    except ApiKey.DoesNotExist:
        api_key = ApiKey.objects.create(user=request.user)

    return render_to_response('getAPIkey.html',
                                {"api_key":api_key.key},
                                RequestContext(request))
