from django import forms
from django.forms.extras.widgets import SelectDateWidget

from .models import Menu, Item, Ingredient


class MenuForm(forms.ModelForm):
    class Meta:
        model = Menu
        exclude = ('created_date',)

    expiration_date = forms.DateField(widget=SelectDateWidget(years=range(2017, 2030)))

    def clean_season(self):
        season = self.cleaned_data.get('season')
        if len(season) < 3:
            raise forms.ValidationError('Season must be 3 characters or longer')
        if season.isnumeric():
            raise forms.ValidationError('Season can not be only digits.')
        return season
