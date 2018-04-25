from django import forms

from .models import post

class UploadLayoutForm(forms.Form):
    layout_title = forms.CharField(max_length=50)
    layout_owner = models.CharField(max_length=50)
    layout_image = models.ImageField(label='Select an image', help_text='max. 1000x1000px')
