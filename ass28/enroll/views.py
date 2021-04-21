from django.shortcuts import render
from .forms import StudentReg
from . models import Employee
# Create your views here.
def showformdata(request):
    if request.method == "POST":
        fm = StudentReg(request.POST)
        if fm.is_valid():
            ids = fm.cleaned_data["eid"]
            nm = fm.cleaned_data["ename"]
            ds = fm.cleaned_data["designation"]
            sl = fm.cleaned_data["salary"]
            #insert
            #reg = Employee(eid=ids,ename=nm,designation=ds,salary=sl)
            #reg.save()
            #update
            #reg = Employee(id=6,eid=ids,ename=nm,designation=ds,salary=sl)
            #reg.save()
            #Delete
            reg = Employee(id=5)
            reg.delete()
        
        else:
            print("INVALID DATA")
    else:
        fm = StudentReg()
    return render(request,"enroll/ureg.html",{"form":fm})
