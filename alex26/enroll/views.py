from django.shortcuts import render
from .forms import StudentReg
# Create your views here.
def showformdata(request):
    if request.method == "POST":
        fm = StudentReg(request.POST)
        if fm.is_valid():
            name = fm.cleaned_data["name"]
            #agree = fm.cleaned_data["agree"]
            email = fm.cleaned_data["email"]
            #price = fm.cleaned_data["price"]
            #roll_no = fm.cleaned_data["roll_no"]
            #rate = fm.cleaned_data["rate"]
            #comment = fm.cleaned_data["comment"]
            password = fm.cleaned_data["password"]
            print("Name = ",name)
            #print("Agree = ",agree)
            print("Email = ",email)
            print("Password = ",password)
            #print("Roll_No = ",roll_no)
            #print("Price = ",price)
            #print("Rate = ",rate)
            #print("Comment = ",comment)
        else:
            print("INVALID DATA")
    else:
        fm = StudentReg()
    return render(request,"enroll/ureg.html",{"form":fm})
