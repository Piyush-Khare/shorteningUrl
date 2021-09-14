from django import forms
from django.db.models import fields
from . import models
from django import forms

class ModalForm(forms.ModelForm):
    long_url = forms.URLField(widget=forms.URLInput(attrs={"class": "form-control form-control-lg", "placeholder": "Your URL to shorten"}))


    class Meta:
        model = models.ShortUrl
        fields = ['long_url']