from django import forms

class productinstanceform(forms.Form):
    camera_mode = forms.CharField(max_length=100)
    count = forms.CharField(max_length=100)