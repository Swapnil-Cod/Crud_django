from django import forms
from employee.models import Employee
from django import forms

class EmployeeForm(forms.Form):
    id=forms.CharField(max_length=10,label='Enter ID:')
    name=forms.CharField(max_length=30,label='Enter Name:')
    email=forms.EmailField(label='Enter email')
    contact=forms.CharField(label='Enter Contact')

    class Meta:  
        model = Employee  
        fields = "__all__"  
    