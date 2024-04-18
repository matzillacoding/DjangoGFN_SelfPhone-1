from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms


class EigeneUserCreationForm(UserCreationForm):

    first_name = forms.CharField(
        max_length=100, required=False, help_text='Optional.')
    last_name = forms.CharField(
        max_length=100, required=False, help_text='Optional.')

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name',
                  'email', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'class': 'form'})
        self.fields['username'].label = 'Benutzername'
        self.fields['first_name'].widget.attrs.update({'class': 'form'})
        self.fields['first_name'].label = 'Vorname'
        self.fields['last_name'].widget.attrs.update({'class': 'form'})
        self.fields['last_name'].label = 'Nachname'
        self.fields['password1'].widget.attrs.update({'class': 'form'})
        self.fields['password1'].label = 'Passwort'
        self.fields['password2'].widget.attrs.update({'class': 'form'})
        self.fields['password2'].label = 'Passwort wiederholen'
        self.fields['email'].widget.attrs.update({'class': 'form'})
        self.fields['email'].label = 'Email'
