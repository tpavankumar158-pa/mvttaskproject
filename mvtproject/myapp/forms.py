from django import forms
from myapp.models import Employee

class EmployeeForm(forms.ModelForm):
    EmployeeId = forms.IntegerField()
    EmployeeName = forms.CharField(max_length=50)
    EmployeeSalary = forms.IntegerField()
    class Meta:
        model = Employee
        fields ='__all__'
        
        

        