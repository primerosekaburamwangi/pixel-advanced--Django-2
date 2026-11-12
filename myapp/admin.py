from django.contrib import admin

from .models import Contact, Employee

from .models import User

admin.site.register(User)


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email', 'subject', 'created_at')


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'created_at')
