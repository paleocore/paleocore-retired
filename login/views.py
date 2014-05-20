from django.contrib.auth import authenticate,login
from django.contrib import messages
from django.http import HttpResponse, HttpResponseForbidden, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.shortcuts import render_to_response
from django.template import RequestContext


def user_login(request):

    if request.POST:
        username = request.POST['username']
        password = request.POST['password']
        nextURL = request.POST['nextURL']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(nextURL)  # return 200 with the url to redirect
            else:
                messages.add_message(request, messages.INFO,
                                     'Your account is not active. Please contact an administrator')
                return HttpResponseRedirect(reverse("login:user_login") + "?next=" + nextURL)
        else:
            messages.add_message(request, messages.INFO,
                                     'Incorrect username and/or password.')
            return HttpResponseRedirect(reverse("user_login:user_login") + "?next=" + nextURL)
    else:
        nextURL = request.GET.get("next")
        return render_to_response('login.html',
                                  {"nextURL": nextURL},
                                  RequestContext(request))

