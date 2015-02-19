from django import forms
from testapp.models import User

class register_form(forms.ModelForm):
    fname = forms.CharField(max_length=200, help_text="First Name: ")
    lname = forms.CharField(max_length=200, help_text="Last Name: ")
    email = forms.CharField(max_length=255, help_text="Email: ")
    passwd = forms.CharField(max_length=100, help_text="Password: ")
    rpasswd = forms.CharField(max_length=100, help_text="Re-Type Password: ")

    class Meta:
	model = User
