from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import Employee
from .models import LeaveRequest
from django.views.decorators.csrf import csrf_protect

def home_view(request):
    return render(request, 'home.html')

def about_view(request):
    return render(request, 'about.html')

def services_view(request):
    return render(request, 'services.html')

def contact_view(request):
    return render(request, 'contact.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # Check if user is admin (staff) or employee
            if user.is_staff:
                return redirect('admin_dashboard')
            else:
                return redirect('employee_dashboard')
        else:
            messages.error(request, 'Invalid username or password.')
    return render(request, 'login.html')

def is_admin(user):
    return user.is_authenticated and user.is_staff

@login_required
@user_passes_test(is_admin)
def admin_dashboard(request):
    return render(request, 'admin_dashboard.html')


def add_employee(request):
    if request.method == 'POST':
        messages.success(request, "Employee added successfully!")
        return redirect('admin_dashboard')  
    return render(request, 'add-employee.html')

def employee_list(request):
    employees = Employee.objects.all().order_by('empName')
    return render(request, 'employee_list.html', {'employees': employees})

def approve_leave_view(request):
    return render(request, 'approve_leave.html')

def salary_management(request):
    employees = Employee.objects.all()
    return render(request, 'salary_management.html', {'employees': employees})

@csrf_protect
def update_salary(request, employee_id):
    employee = get_object_or_404(Employee, id=employee_id)

    if request.method == 'POST':
        hike_percent = request.POST.get('hike')
        try:
            hike_percent = float(hike_percent)
            if hike_percent < 0:
                messages.error(request, "Hike percentage cannot be negative.")
            else:
                new_salary = employee.current_salary + (employee.current_salary * hike_percent / 100)
                employee.current_salary = new_salary
                employee.save()
                messages.success(request, f"Salary updated successfully to {new_salary:.2f}")
                return redirect('salary-management')
        except ValueError:
            messages.error(request, "Please enter a valid number for hike percentage.")

    context = {
        'employee': employee,
    }
    return render(request, 'update_salary.html', context)

def id_cards(request):
    employees = Employee.objects.all()
    return render(request, 'id_cards.html', {'employees': employees})

def generate_id_card(request, employee_id):
    employee = get_object_or_404(Employee, id=employee_id)
    return render(request, 'generate_id_card.html', {'employee': employee})

@login_required
def employee_dashboard(request):
    return render(request, 'employee_dashboard.html')