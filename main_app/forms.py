from django.forms import ModelForm
from .models import Stat


class StatForm(ModelForm):
    class Meta:
        model = Stat
        fields = ['date', 'goals', 'assists',
                  'clean_sheets', 'shots']
