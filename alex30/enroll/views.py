from django.shortcuts import render

# Create your views here.
def show_details(request,my_id):
    student = {}
    if my_id == 1:
        student = {'id':my_id,'name':'Alex'}
    if my_id == 2:
        student = {'id':my_id,'name':'Appu'}
    if my_id == 3:
        student = {'id':my_id,'name':'Pooja'}

    return render(request,"enroll/show.html",student)

def home(request):
    return render(request,"enroll/home.html")