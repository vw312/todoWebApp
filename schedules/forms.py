from django import forms

from . import models

class scheduleCreateForm(forms.ModelForm):
    """Used for creating and deleting schedules"""
    class Meta:
        model=models.Schedules
        fields=[
            'what_todo',
            'description',
            'date_time',
        ]
        widgets = {
            'date_time':forms.TextInput(attrs={'placeholder': 'YYYY-MM-DD HH:MM'})
        }

class scheduleEditForm(forms.ModelForm):
    """Used for creating and deleting schedules"""
    class Meta:
        model=models.Schedules
        fields=[
            'what_todo',
            'description',
            'date_time',
            'state_user',
        ]
        widgets = {
            'date_time':forms.TextInput(attrs={'placeholder': 'YYYY-MM-DD HH:MM'})
        }
