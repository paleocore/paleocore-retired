from django import forms


class UploadKMLForm(forms.Form):
    kmlfileUpload = forms.FileField(
        label='Upload a kml file, *.kml',
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