from django.conf import settings
from django.conf.urls.static import static
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

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


# app - urls.py

from django.urls import path
from . import views

urlpatterns = [
    path("", views.user_list),
    path("Add/", views.AddUser),
    path("Edit/<id>", views.EditUser),
    path("Delete/<eid>", views.DeleteUser),
    path("View/<eid>", views.ViewUser),
]
