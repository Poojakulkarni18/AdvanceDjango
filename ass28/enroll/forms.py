from django.core import validators
from django import forms


class StudentReg(forms.Form):
    eid = forms.CharField(error_messages={"required":"Enter your name"})
    ename = forms.CharField(error_messages={"required":"Enter your name"})
    designation = forms.CharField(error_messages={"required":"Enter your designation"})
    salary = forms.CharField(error_messages={"required":"Enter your salary"})
   
    