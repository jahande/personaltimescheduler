from schedulerApp.models import Profile

__author__ = 'rj'
from django import forms

class WorkSheetForm(forms.Form):
    name = forms.CharField()

class ProfileForm(forms.Form):
    class Meta:
        model = Profile
        exclude = ('user')
    image = forms.ImageField()
class RegistrationForm(forms.Form):
    username = forms.CharField(max_length=30)
    password = forms.CharField(widget=forms.PasswordInput())
    confirm_password = forms.CharField(widget=forms.PasswordInput())
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)
    image = forms.ImageField()
    email = forms.EmailField()
