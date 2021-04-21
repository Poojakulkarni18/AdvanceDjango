from django.core import validators
from django import forms
from .models import User

class StudentReg(forms.ModelForm):
    class Meta:
        model = User
        fields = ["name","email","password"]
        labels = {"name":"Enter Your Name","email":"Enter Your Email","password":"Enter Your Password"}
        error_messages = {
            "name":{"required":"Please Enter Your Name"},
            "email":{"required":"Please Enter Your Email"},
            "password":{"required":"Please Enter Your Password"}
            }

        widgets = {
            'password':forms.PasswordInput,
            'name': forms.TextInput(attrs={'class':'myclass','placeholder':'Enter Name'})
        }
   
        