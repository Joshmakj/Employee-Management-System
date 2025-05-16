from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView
from django.urls import reverse_lazy

urlpatterns = [
    path('', views.home_view, name='home'),
    path('login/', views.login_view, name='login'),
    path('accounts/login/', views.login_view, name='accounts_login'),  # Add this line
    path('admin-dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('add-employee/', views.add_employee, name='add-employee'),
    path('employees/', views.employee_list, name='employee_list'),
    path('approve_leave/', views.approve_leave_view, name='approve_leave'),
    # path('/leave/<int:leave_id>/<str:new_status>/', views.change_leave_status, name='change_leave_status'),
    path('salary-management/', views.salary_management, name='salary-management'),
    path('update-salary/<int:employee_id>/', views.update_salary, name='update-salary'),
    path('id-cards/', views.id_cards, name='id-cards'),
    path('generate-id-card/<int:employee_id>/', views.generate_id_card, name='generate-id-card'),
    path('employee-dashboard/', views.employee_dashboard, name='employee_dashboard'),
    path('about/', views.about_view, name='about'),
    path('services/', views.services_view, name='services'),
    path('contact/', views.contact_view, name='contact'),
   


]