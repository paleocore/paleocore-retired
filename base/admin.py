from django.contrib import admin
from base.models import PaleocoreUser
from django.template import loader, RequestContext
from django.contrib.admin import helpers
from django.http import HttpResponse
from django.core.mail import send_mass_mail


class PaleocoreUserAdmin(admin.ModelAdmin):
    def email(self):
        return self.user.email
    def last_name(self):
        return self.user.last_name
    def first_name(self):
        return self.user.first_name
    list_filter = ['send_emails','institution']
    search_fields = ('last_name','first_name')
    list_display = [first_name,last_name,email,"send_emails"]
    actions = ['send_emails']

    def send_emails(self, request, queryset):
        """
        A function that defines a custom admin action to send bulk emails to selected users. The function calls a
        custom template called email.html
        """
        returnURL="/admin/paleoschema/paleocoreuser/"
        if 'apply' in request.POST: # check if the email form has been completed
            # code to send emails. We use send_mass_email, which requires a four-part tuple
            # containing the subject, message, from_address and a list of to addresses.
            if 'subject' in request.POST:
                if request.POST["subject"] == '':
                    self.message_user(request, "Message is missing a subject")
                    t = loader.get_template("base/templates/email.html")
                    c = RequestContext(request, {'returnURL':returnURL,'emails':queryset, 'action_checkbox_name': helpers.ACTION_CHECKBOX_NAME,})
                    return HttpResponse(t.render(c))
                else:
                    subject = request.POST["subject"]
            if 'message' in request.POST:
                if request.POST["message"] == '':
                    self.message_user(request, "Message is empty")
                    t = loader.get_template("base/templates/email.html")
                    c = RequestContext(request, {'returnURL':returnURL,'emails':queryset, 'action_checkbox_name': helpers.ACTION_CHECKBOX_NAME,})
                    return HttpResponse(t.render(c))
                message = request.POST["message"]
            from_address = 'paleocore@paleocore.org'
            messages_list = []
            # build the to list by iterating over records in queryset from selected records
            for i in queryset:
                if i.user.email:
                    to_address = [i.user.email]
                    message_tuple = (subject,message,from_address,to_address)
                    messages_list.append(message_tuple)
            #slice off the first element of tuple which is empty
            messages_tuple = tuple(messages_list)
            send_mass_mail(messages_tuple,fail_silently=False)

            self.message_user(request, "Mail sent successfully ")
        else:
            t = loader.get_template("base/templates/email.html")
            c = RequestContext(request, {'returnURL':returnURL,'emails':queryset, 'action_checkbox_name': helpers.ACTION_CHECKBOX_NAME,})
            return HttpResponse(t.render(c))
    send_emails.short_description = "Send an email to selected members"

admin.site.register(PaleocoreUser, PaleocoreUserAdmin)