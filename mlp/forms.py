from django import forms


class UploadKMLForm(forms.Form):
    kmlfileUpload = forms.FileField(
        label='Upload a kml file, *.kml',
    )

class DownloadKMLForm(forms.Form):
    FILE_TYPE_CHOICES = (('1', 'KML',), ('2', 'KMZ',))
    kmlfileDownload = forms.ChoiceField(
        required=False,
        widget=forms.RadioSelect,
        choices=FILE_TYPE_CHOICES,
        label="File Type: "
    )

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