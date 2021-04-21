from django.shortcuts import render
from .forms import StudentReg
from . models import User
# Create your views here.
def showformdata(request):
    if request.method == "POST":
        fm = StudentReg(request.POST)
        if fm.is_valid():
            nm = fm.cleaned_data["name"]
            em = fm.cleaned_data["email"]
            ps = fm.cleaned_data["password"]
    
            #rpassword = fm.cleaned_data["rpassword"]
            print("Name = ",nm)
            print("Email = ",em)
            print("Password = ",ps)
            reg = User(name=nm,email=em,password=ps)
            reg.save()
            #reg = User(id=2,name=nm,email=em,password=ps)
            #reg.save()
            #reg = User(id=2)
            #reg.delete()
        else:
            print("INVALID DATA")
    else:
        fm = StudentReg()
    return render(request,"enroll/ureg.html",{"form":fm})
