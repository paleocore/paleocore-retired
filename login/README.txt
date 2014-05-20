Author: Andrew Barr

This is a simple app to handle user authentication in views.  It contains a login.html template, and a login view.

This is designed to work with the @permission_required decorator in django.contrib.auth.decorators.  When this decorator
prefaces a view, any user that doesn't pass the permission test gets directed to /login/
Note also that the destination page is automatically included as a url parameter ?next

example
####
####

from django.contrib.auth.decorators import @permission_required

@permission_required("app.add_MyModel")
def someView(request):
    return("You have permissions to add to MyModel!")

####
####
Any user that doesn't have auth permissions
