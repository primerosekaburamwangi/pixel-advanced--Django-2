from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('contact/', views.contact, name='contact'),
    path('emp/', views.create_emp, name='create_emp'),
    path('show/', views.show_employees, name='show_employees'),
    path('edit/<int:id>/', views.edit_employee, name='edit_employee'),
    path('update/<int:id>/', views.update_employee, name='update_employee'),
    path('delete/<int:id>/', views.delete_employee, name='delete_employee'),
]
