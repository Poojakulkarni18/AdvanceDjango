from django import forms
class StudentReg(forms.Form):
    #name = forms.CharField(initial='abc')
    name = forms.CharField(widget=forms.TextInput(attrs={'class':'somecss'}))
    #name = forms.CharField(widget=forms.Select)
    #name = forms.CharField(widget=forms.FileInput)
    #name = forms.CharField(widget=forms.CheckboxInput)
    #name = forms.CharField(widget=forms.Textarea)
    #name = forms.CharField(widget=forms.PasswordInput)
    #email = forms.EmailField()
    #first_name = forms.CharField(required=False,help_text="Limit 50")
    #key = forms.CharField(widget=forms.HiddenInput())