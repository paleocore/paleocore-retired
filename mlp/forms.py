from django import forms


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