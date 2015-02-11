from django import forms


class SiteSearch(forms.Form):
    site_name = forms.CharField(label="Search for a site ",max_length=80)