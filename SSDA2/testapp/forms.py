from django import forms
<<<<<<< HEAD
from testapp.models import User
=======
#from testapp.models import User
from django.contrib.auth.models import User
>>>>>>> 440f7c66630d25ea23bbd3c9c129a0969c172541
from django.core.validators import validate_email

class register_form(forms.ModelForm):
    fname = forms.CharField(max_length=200, help_text="First Name: ")
    lname = forms.CharField(max_length=200, help_text="Last Name: ")
<<<<<<< HEAD
    email = forms.EmailField(max_length=255, help_text="Email: ")
=======
    email = forms.CharField(max_length=255, help_text="Email: ")
>>>>>>> 440f7c66630d25ea23bbd3c9c129a0969c172541
    passwd = forms.CharField(widget=forms.PasswordInput(), max_length=100, help_text="Password: ")
    rpasswd = forms.CharField(widget=forms.PasswordInput(), max_length=100, help_text="Re-Type Password: ")

    class Meta:
	model = User

<<<<<<< HEAD
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
=======
>>>>>>> 440f7c66630d25ea23bbd3c9c129a0969c172541
