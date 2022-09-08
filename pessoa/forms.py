from django import forms
from django.forms import fields, models
from .models import Contact, People

class FormPeople(forms.ModelForm):
    birthday = forms.DateField(
        widget=forms.TextInput(
            attrs={"type": "date"}
        )
    )
    class Meta:
        model = People
        fields = [ 'full_name', 'birthday', 'active' ]

class FormContact(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name','email','telephone']