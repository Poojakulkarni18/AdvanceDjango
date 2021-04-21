from django.shortcuts import render
from .forms import StudentReg
# Create your views here.
def showformdata(request):
    if request.method == "POST":
        fm = StudentReg(request.POST)
        if fm.is_valid():
            name = fm.cleaned_data["name"]
            email = fm.cleaned_data["email"]
            password = fm.cleaned_data["password"]
            #rpassword = fm.cleaned_data["rpassword"]
            
            print("Name = ",name)
            
            print("Email = ",email)
            
        else:
            print("INVALID DATA")
    else:
        fm = StudentReg()
    return render(request,"enroll/ureg.html",{"form":fm})
