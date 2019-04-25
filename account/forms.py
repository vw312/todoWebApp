from django import forms
from django.contrib.auth.forms import AuthenticationForm,PasswordChangeForm,UserCreationForm
from .models import myUser

from timezone.models import timezone

class CustomModelChoiceField(forms.ModelChoiceField):
     def label_from_instance(self, obj):
         return "%s" % (obj.timezone)

class accountCreateForm(UserCreationForm):
    timezone = CustomModelChoiceField(queryset=timezone.objects.all())
    class Meta:
        model=myUser
        fields=[
            'username',
            'email',
            'timezone',
            'password1',
            'password2',
        ]

class accountLoginForm(AuthenticationForm) :
    pass

class passwordChangeForm(PasswordChangeForm):
    pass

class accountEditForm(forms.ModelForm):
    class Meta:
        model=myUser
        fields=[
            'email'
        ]
