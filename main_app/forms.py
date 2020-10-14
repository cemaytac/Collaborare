from django.forms import ModelForm
from .models import Stat, Team
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms


class StatForm(ModelForm):
    class Meta:
        model = Stat
        fields = ['date', 'goals', 'assists',
                  'clean_sheets', 'shots']


class SignupForm(UserCreationForm):
    username = forms.CharField(
        max_length=50, required=True, help_text='Required')
    email = forms.EmailField(
        max_length=254, required=True, help_text='Required')
    first_name = forms.CharField(
        max_length=30, required=True, help_text='Required')
    last_name = forms.CharField(max_length=30)

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name')
