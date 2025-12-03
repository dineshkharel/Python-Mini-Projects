from django.shortcuts import render,redirect
from .models import Employee
from .forms import EmployeeForm

# Create your views here.

def employee_list(request):
    employees = Employee.objects.all()
    return render(request,'employees/employee_list.html',{'employees':employees})

def add_employee(request):
    if request.method =="POST":
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('employee_list')
    else:
        form = EmployeeForm()
    return render(request,'employees/add_employee.html',{'form':form})


def update_employee(request,id):
    employee= Employee.objects.get(id=id)

    if request.method =="POST":
        employee.full_name = request.POST.get("full_name")
        employee.email = request.POST.get("email")
        employee.age = request.POST.get("age")
        employee.salary = request.POST.get("salary")
        employee.save()

        return redirect('employee_list')

    return render(request,'employees/update_employee.html',{"employee":employee})


def delete_employee(request,id):
    employee = Employee.objects.get(id=id)
    employee.delete()
    
    return redirect('employee_list')