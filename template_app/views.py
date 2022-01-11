from django.shortcuts import render,redirect
from django.http import HttpResponse
from template_app.form import EmpForm,StudentForm
from django.contrib import messages
from .models import *

def index(request):
    return render(request,'dashboard/index.html')

def dashboard(request):
    return render(request,'dashboard/dash.html')

def show(request):
    emp = EmpForm()  
    return render(request,"dashboard/show.html",{'form':emp})

def student(request):  
    student = StudentForm()  
    return render(request,"dashboard/show.html",{'form':student})  

def add_employee(request):
    return render(request,"dashboard/add_employee.html")


def insert_employee(request):
    if request.method=="POST":
        eid=request.POST['eid']
        ename=request.POST['ename']
        econtact=request.POST['econtact']
        item=Employee(eid=eid,ename=ename,econtact=econtact)
        item.save()
        messages.info(request,"Employee Details Add Succesfully")
    else:
        pass 
    return redirect(list_employee)
   

def delete_employee(request,myid):
    item=Employee.objects.get(id=myid)
    item.delete()
    messages.info(request,"Employee Details Deleted Succesfully")
    return redirect(list_employee)

def edit_employee(request,myid):
    get_val=Employee.objects.get(id=myid)
    context={
        'employee_detail':get_val,
        } 
    return render(request,'dashboard/edit_employee.html',context)

def update_employee(request,myid):
    if request.method=="POST":
        item=Employee.objects.get(id=request.POST['id'])
        item.eid=request.POST['eid']
        item.ename=request.POST['ename']
        item.econtact=request.POST['econtact']
        item.save()
        messages.info(request,"Employee Details update Succesfully")
    else:
        pass
    return redirect(list_employee)


def list_employee(request):
    context={'employee_list':Employee.objects.all()} 
    return render(request, 'dashboard/list_employee.html',context)