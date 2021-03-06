from django import forms
from django.contrib.auth.models import User
from django.core.validators import validate_email

class register_form(forms.ModelForm):
    username = forms.CharField(max_length=200, help_text="Username: ")
    fname = forms.CharField(max_length=200, help_text="First Name: ")
    lname = forms.CharField(max_length=200, help_text="Last Name: ")
    email = forms.CharField(max_length=255, help_text="Email: ")
    remail = forms.CharField(max_length=255, help_text="Re-Type Email: ")
    passwd = forms.CharField(widget=forms.PasswordInput(), max_length=100, help_text="Password: ")
    rpasswd = forms.CharField(widget=forms.PasswordInput(), max_length=100, help_text="Re-Type Password: ")

    class Meta:
	model = User
	fields = ()
