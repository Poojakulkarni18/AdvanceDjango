from django.core import validators
from django import forms

# def start_with_s(value):
#     #if value[0] != 's':
#     if not(value[0] == 's' or value[0] == 'S'):
#         raise forms.ValidationError("Name should start with s")

# class StudentReg(forms.Form):
#     name = forms.CharField(validators=[start_with_s])
#     email = forms.EmailField()

class StudentReg(forms.Form):
    name = forms.CharField(error_messages={"required":"Enter your name"})
    email = forms.EmailField(error_messages={"required":"Enter your email"})
    password = forms.CharField(widget=forms.PasswordInput,error_messages={"required":"Enter your password"},min_length=5)
    #password = forms.CharField(widget=forms.PasswordInput,error_messages={"required":"Enter your password"})
    #rpassword = forms.CharField(label = "Re-enter",widget=forms.PasswordInput)

    # def clean(self):
    #     cleaned_data = super().clean()
    #     valpwd = cleaned_data["password"]
    #     valrpwd = cleaned_data["rpassword"]
    #     if valpwd != valrpwd:
    #         raise forms.ValidationError("Password does not match")