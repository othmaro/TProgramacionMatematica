from django import forms
from django.forms import Widget
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _

class registro(forms.Form):
    your_name = forms.CharField(label='Nombre', max_length=100)
    apellido = forms.CharField(label='Apellido', max_length=100)
    user_name = forms.EmailField(label='Email', max_length=100)
    password = forms.CharField(widget=forms.PasswordInput())
