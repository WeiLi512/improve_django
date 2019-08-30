from django import forms
from django.forms.extras.widgets import SelectDateWidget

from .models import Menu, Item, Ingredient


class MenuForm(forms.ModelForm):
    class Meta:
        model = Menu
        exclude = ('created_date',)

    expiration_date = forms.DateField(widget=SelectDateWidget(years=range(2017, 2030)))
