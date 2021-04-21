from django.shortcuts import render
from . forms import StudentReg
from django.http import HttpResponseRedirect
# Create your views here.
def sreg(request):
    return render(request,"enroll/pass.html")
def showformdata(request):
    if request.method == 'POST':
        fm = StudentReg(request.POST)
        print("POST METHOD")
        if fm.is_valid():
            name = fm.cleaned_data["name"]
            email = fm.cleaned_data["email"]
            password = fm.cleaned_data["password"]
            print("Name = ",name)
            print("Email = ",email)
            print("Password = ","password")
            return HttpResponseRedirect("/enroll/pass")
            #return render(request,"enroll/pass.html",{"nm":name})
        else:
            print("INVALID DATA")
    else:
        print("GET METHOD")
        fm = StudentReg()
    return render(request,"enroll/userreg.html",{"form":fm})