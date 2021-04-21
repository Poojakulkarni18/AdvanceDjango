from django.shortcuts import render
from . forms import StudentReg
# Create your views here.
def showformdata(request):
    #fm = StudentReg(auto_id=True,label_suffix='=',initial={'name':'abc','email':'abc@gmail.com'})
    fm = StudentReg()
    #fm.order_fields(field_order=['email','first_name','name'])
    return render(request,"enroll/userreg.html",{"form":fm})