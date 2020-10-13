from django.forms import ModelForm
from .models import Stat
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class StatForm(ModelForm):
    class Meta:
        model = Stat
        fields = ['date', 'goals', 'assists',
                  'clean_sheets', 'shots']


# class SignupForm(UserCreationForm):
#     first_name = forms.CharField(max_length=30)
#     last_name = forms.CharField(max_length=30)
#     email = forms.EmailField(max_length=254)
#     team =
