from django import forms
from . models import User

class StudentReg(forms.ModelForm):
    class Meta:
        model = User
        fields = ['student_name','email','password']


class TeacherReg(StudentReg):
    class Meta(StudentReg.Meta):
        fields = ['teacher_name','email','password']
