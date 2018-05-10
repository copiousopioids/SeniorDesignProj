from django import forms
from .models import Layout

# from .models import post

class UploadLayoutForm(forms.Form):
    layout_title = forms.CharField(label='Layout Title', max_length=50)
    layout_owner = forms.CharField(label='Layout Owner', max_length=50)
    layout_image = forms.FileField(label='Select an image', help_text='<br>(max. 2000x2000px)')
    # class Meta:
    #     model = Layout
    #     fields = ('layout_title', 'layout_owner', 'layout_image')
