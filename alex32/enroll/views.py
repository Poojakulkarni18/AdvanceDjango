from django.shortcuts import render
from . forms import StudentReg, TeacherReg
# Create your views here.

def student_form(request):
    if request.method == 'POST':
        fm = StudentReg(request.POST)
        if fm.is_valid():
            fm.save()

    else:
        fm = StudentReg()
    return render(request,"enroll/student.html",{'form':fm})


def teacher_form(request):
    if request.method == 'POST':
        fm = TeacherReg(request.POST)
        if fm.is_valid():
            fm.save()

    else:
        fm = TeacherReg()
    return render(request,"enroll/teacher.html",{'form':fm})