from django.shortcuts import redirect, render
import employee
from employee.forms import EmployeeForm
from employee.models import Employee

# Create your views here.
def emp(request):
    context={}
    context['form']=EmployeeForm
    if request.method =="POST":
        form = EmployeeForm(request.POST)
        if form.is_valid():
            id=form.cleaned_data['id']
            name=form.cleaned_data['name']
            email=form.cleaned_data['email']
            contact=form.cleaned_data['contact']
            em=Employee.objects.create(eid=id,ename=name,eemail=email,econtact=contact)
            return redirect('/show')
    return render(request,'index.html',context) 

def show(request):
    employee = Employee.objects.all()
    return render(request,'show.html',{'employee':employee})

def edit(request,id):
    employee = Employee.objects.get(id=id) 
    return render(request,'edit.html',{'employee':employee})

def update(request,id):
    employee = Employee.objects.get(id=id) 
    form = EmployeeForm(request.POST,instance=employee)
    if form.is_valid():
        form.save()
        return redirect('/show')
    return render(request,'update.html',{'employee':employee})

def destroy(request,id):
    employee = Employee.objects.get(id=id) 
    employee.delete()
    return redirect('/show')

    


