from django import forms
from django.forms import widgets
from Join.models import Join


class Form(forms.ModelForm):
    class Meta:
        model = Join
        fields = [
            'FirstName',
            'LastName',
            'RegNo',
            'Year',
            'DateOfBirth',
            'Department',
            'MobileNumber',
            'AreaOfInterest'
        ]
