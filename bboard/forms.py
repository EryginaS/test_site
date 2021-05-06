from django.forms import ModelForm
from django import forms




class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class ApplicationForm(forms.Form):
    aplicate = forms.CharField()
    story = forms.CharField()
    priority = forms.IntegerField()
    type_app =forms.IntegerField()

    