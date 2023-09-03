from django import forms
from .models import CrudModel


class CrudForm(forms.ModelForm):
    class Meta:
        model = CrudModel
        fields = ['name', 'date_added', 'ready_to']
