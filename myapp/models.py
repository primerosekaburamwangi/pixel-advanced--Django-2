from django.db import models


class Contact(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.full_name


class Employee(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class User(models.Model):
    name = models.CharField(max_length=30)
    photo = models.ImageField(upload_to="uploads", default="a.png")
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)
    mobile_number = models.CharField(max_length=15)
    date_of_birth = models.DateField()

    def __str__(self):
        return self.name
