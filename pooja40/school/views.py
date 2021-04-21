from django.shortcuts import render
from . models import Student
# Create your views here.
def home(request):
    #student_data = Student.objects.all()
    #student_data = Student.objects.filter(marks=99)
    student_data = Student.objects.exclude(marks=52)
    #print("return Data",student_data)
    print("Query :",student_data.query)
    context = {
        "students":student_data
    }
    return render(request,"school/home.html",context)