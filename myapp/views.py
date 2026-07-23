from django.shortcuts import render,redirect,get_object_or_404
from myapp.models import Employee
from myapp.forms import EmployeeForm
# Create your views here.
def addemployee(request):
    eform = EmployeeForm()
    if request.method == 'POST':
        eform = EmployeeForm(request.POST)
        if eform.is_valid():
            eform.save(commit=True)
            return redirect('/')
    return render(request,'myapp/add.html',{'form':eform}) 

def getemployees(request):
    employees = Employee.objects.all()
    return render(request, "myapp/employee.html", {"EmpList": employees})

def getemployee(request):
    eid=request.GET.get('id')
    employee = get_object_or_404(Employee,EmployeeId=eid)
    return render(request,'myapp/find.html',{'emps':employee})

def editemployee(request,id):
    employee = get_object_or_404(Employee,EmployeeId=id)
    eform = EmployeeForm(instance=employee)
    if request.method=='POST':
        eform = EmployeeForm(request.POST,instance=employee)
        if eform.is_valid():
            eform.save()
            return redirect('/')
    return render(request,'myapp/edit.html',{'form':eform})

def deleteemployee(request,id):
    employee = get_object_or_404(Employee,EmployeeId=id)
    if request.method =="POST":
        employee.delete()
        return redirect('/')
    return render(request,'myapp/delete.html',{'emps':employee})
