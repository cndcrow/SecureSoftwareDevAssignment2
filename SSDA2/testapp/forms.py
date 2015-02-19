from django import forms
from testapp.models import User
from django.core.validators import validate_email

class register_form(forms.ModelForm):
    fname = forms.CharField(max_length=200, help_text="First Name: ")
    lname = forms.CharField(max_length=200, help_text="Last Name: ")
    email = forms.EmailField(max_length=255, help_text="Email: ")
    passwd = forms.CharField(widget=forms.PasswordInput(), max_length=100, help_text="Password: ")
    rpasswd = forms.CharField(widget=forms.PasswordInput(), max_length=100, help_text="Re-Type Password: ")

    class Meta:
	model = User

def clean_email(self):
    email = self.cleaned_data['email']
    if validate_email(email):
	raise ValidationError("Email is not valid")
    if User.objects.filter(email=email).exists():
	raise ValidationError("Email already exists.")

def clean(self):
    form_data = self.cleaned_data
    if form_data['passwd'] != form_data['rpasswd']:
    	raise ValidationError("Passwords do not match.")
