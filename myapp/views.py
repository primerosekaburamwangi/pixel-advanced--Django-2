from django import forms
from django.contrib import messages
from django.contrib.auth.models import User
from django.shortcuts import redirect, render

from .models import Contact, Employee


class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['name', 'email', 'phone']


def home(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        secret = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        if not username or not email or not secret or not confirm_password:
            messages.error(request, 'Please fill in all fields.')
            return redirect('home')

        if secret != confirm_password:
            messages.error(request, 'Passwords do not match.')
            return redirect('home')

        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already exists.')
            return redirect('home')

        if User.objects.filter(email=email).exists():
            messages.error(request, 'Email already exists.')
            return redirect('home')

        user = User.objects.create_user(username=username, email=email)
        user.set_password(secret)
        user.save()
        messages.success(request, 'User created successfully.')
        return redirect('home')

    return render(request, 'home.html')


def contact(request):
    if request.method == 'POST':
        full_name = request.POST.get('full_name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        if not all([full_name, email, subject, message]):
            messages.error(request, 'Please fill in all contact fields.')
            return redirect('contact')

        contact_record = Contact(full_name=full_name, email=email, subject=subject, message=message)
        contact_record.save()
        messages.success(request, 'Thank you for contacting us.')
        return redirect('contact')

    return render(request, 'contact.html')


def create_emp(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Employee created successfully.')
            return redirect('show_employees')
    else:
        form = EmployeeForm()

    return render(request, 'index.html', {'form': form})


def show_employees(request):
    employees = Employee.objects.all()
    return render(request, 'show.html', {'employees': employees})


def edit_employee(request, id):
    employee = Employee.objects.get(id=id)
    form = EmployeeForm(instance=employee)
    return render(request, 'edit.html', {'employee': employee, 'form': form})


def update_employee(request, id):
    employee = Employee.objects.get(id=id)
    if request.method == 'POST':
        form = EmployeeForm(request.POST, instance=employee)
        if form.is_valid():
            form.save()
            messages.success(request, 'Employee updated successfully.')
            return redirect('show_employees')
    else:
        form = EmployeeForm(instance=employee)
    return render(request, 'edit.html', {'employee': employee, 'form': form})


def delete_employee(request, id):
    employee = Employee.objects.get(id=id)
    employee.delete()
    messages.success(request, 'Employee deleted successfully.')
    return redirect('show_employees')

