from django import forms
from .models import FileUploadModel


#class UploadFileForm(forms.ModelForm):
#    title = forms.CharField(max_length=50)
#    file = forms.FileField()
class FileUploadForm(forms.ModelForm):
    class Meta:
        model = FileUploadModel
        fields = [
            'name',
            'file_upload'
        ]
