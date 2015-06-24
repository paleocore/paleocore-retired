from django import forms
from standard.models import Project, TermCategory

SHOW_COLUMNS = (
    ('definition','Field Definitions'),
    ('type','Field Types'),
)

class TermViewForm(forms.Form):
    baseProject = forms.ModelChoiceField(Project.objects.all(), label="Base Project:")
    showColumns = forms.MultipleChoiceField(required=False,label="Show Columns:", widget=forms.CheckboxSelectMultiple(), choices=SHOW_COLUMNS,)
    showProjects = forms.ModelMultipleChoiceField(Project.objects.all(), label="Show Projects:", widget=forms.CheckboxSelectMultiple())
    showCategories = forms.ModelMultipleChoiceField(TermCategory.objects.all(), required=False, label="Show Categories:", widget=forms.CheckboxSelectMultiple())


# class RelateProjectsForm(forms.Form):
#     firstProjectList = forms.ModelChoiceField(Project.objects.all(), label="Project One:")
#     secondProjectList = forms.ModelChoiceField(Project.objects.all(), label="Project Two:")

# class RelateTermsForm(forms.Form):
#
#     def __init__(self, firstProject, secondProject, *args, **kwargs):
#         super(RelateTermsForm, self).__init__(*args, **kwargs)
#
#         self.fields['firstProjectTerms'] = forms.ModelMultipleChoiceField(firstProject.term_set.all())
#         self.fields['secondProjectTerms'] = forms.ModelMultipleChoiceField(secondProject.term_set.all())