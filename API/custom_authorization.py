from tastypie.authorization import DjangoAuthorization
from tastypie.exceptions import Unauthorized

class CustomDjangoAuthorization(DjangoAuthorization):

    #deal with keyword arguments getting passed
    def __init__(self, **kwargs):
        self.appname = kwargs["appname"]
        self.modelname = kwargs["modelname"]

    def read_detail(self, object_list, bundle):
        #first get the result of the standard read_detail method
        result = super(CustomDjangoAuthorization, self).read_detail(object_list, bundle)

        # now we check here for specific permission
        if not bundle.request.user.has_perm('{app}.add_{model}'.format(app = self.appname, model = self.modelname)):
            raise Unauthorized("You are not allowed to access that resource.")

        #if user is authorized, return the standard result
        return True

    def read_list(self, object_list, bundle, **kwargs):
        #first get the result of the standard read_list method
        result = super(CustomDjangoAuthorization, self).read_list(object_list, bundle)

        # now we check here for specific permission
        if not bundle.request.user.has_perm('{app}.add_{model}'.format(app = self.appname, model = self.modelname)):
            raise Unauthorized("You are not allowed to access that resource.")

        #if user is authorized, return the standard result
        return result