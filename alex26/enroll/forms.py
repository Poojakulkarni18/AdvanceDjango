from django import forms
from django.core import validators
class StudentReg(forms.Form):
    #name = forms.CharField()
    #name = forms.CharField(min_length=5,max_length=8,strip=False)
    #name = forms.CharField(min_length=5,max_length=8,empty_value="Django")
    #name = forms.CharField(min_length=5,max_length=8)
    #name = forms.CharField(error_messages={"required":"Complete this"})
    #roll_no = forms.IntegerField(min_value=5)
    ##rate = forms.FloatField()
    #comment = forms.SlugField()
    #email = forms.EmailField()
    #website = forms.URLField()
    #password = forms.CharField(widget=forms.PasswordInput)
    #description = forms.CharField(widget=forms.Textarea(attrs={'rows':3,'cols':50}))
    #agree = forms.BooleanField(label="I Agree",label_suffix='')
    name = forms.CharField(validators=[validators.MaxLengthValidator(8)])
    email = forms.EmailField()
    password = forms.PasswordInput()

    # def clean_name(self):
    #     valname = self.cleaned_data["name"]
    #     if len(valname) < 4:
    #         raise forms.ValidationError("Enter More Than Or Equal To 4 Characters")
    #     return valname
        
        
    