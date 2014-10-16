from django import forms


class UploadKMLForm(forms.Form):
    kmlfileUpload = forms.FileField(
        label='Upload a kml/kmz file, *.kml or *.kmz ',
    )

# class DownloadKMLForm(forms.Form):
#     FILE_TYPE_CHOICES = ('KML', 'KMZ')
#     kmlfileDownload = forms.MultipleChoiceField(
#         required=False,
#         widget=forms.CheckboxSelectMultiple,
#         choices=FILE_TYPE_CHOICES
#     )

class UploadForm(forms.Form):
    shapefileUpload = forms.FileField(
        label='Upload a shape file, *.shp',
    )
    shapefileIndexUpload = forms.FileField(
        label='Upload a shape file index, *.shx',
    )
    shapefileDataUpload = forms.FileField(
        label='Upload shape file data, *.dbf',
    )