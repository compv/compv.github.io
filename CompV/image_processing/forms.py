from django.forms import ModelForm
from django import forms
from image_processing.models import  Users

class RegistrationForm(forms.ModelForm):
    class Meta:
        model = Users
        exclude = ['registration_date', 'status']