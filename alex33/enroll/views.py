from django.shortcuts import render
from . forms import StudentReg
from django.contrib import messages

# Create your views here.
def regi(request):
    if request.method == 'POST':
        fm = StudentReg(request.POST)
        if fm.is_valid():
            fm.save()
            messages.add_message(request,messages.SUCCESS,"Your Account Has Been Created")
            #messages.success(request,"Account Created")

    else:
        fm = StudentReg()
    return render(request,"enroll/userreg.html",{'form':fm})