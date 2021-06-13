from django.forms import ModelForm
from django import forms
from .models import Applications




class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class ApplicationForm(forms.ModelForm):
    model=Applications
    aplicate=forms.CharField()
    story=forms.CharField()
    priority=forms.IntegerField()
    type_app=forms.IntegerField()

    


class ReportForm(ApplicationForm):
    done_work=forms.CharField(max_length=1000)
    

    