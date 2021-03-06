
from datetime import date

from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    USERNAME_FIELD = 'username'
    is_manager = models.BooleanField('manager status',default = False) 
    is_employee = models.BooleanField('employee status',default = False) 
    is_client = models.BooleanField('client status',default = False) 
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=50)

    def save_user (self) :
        self.save()
    def update_user (self) :
        self.update()
    def delete_user (self) :
        self.delete()
    
class Manager (models.Model) :
    user = models.OneToOneField(User, on_delete=models.CASCADE , primary_key=True,)
    email = models.EmailField(blank=True)
    phone_number = models.CharField(max_length= 13)
    manager_no=models.IntegerField(default=0)

    def __str__(self):
        return f'{self.user}'

    def save_manager (self) :
        self.save()
    def update_manager (self) :
        self.update()
    def delete_manager (self) :
        self.delete()

class Employee (models.Model) :
    user = models.OneToOneField(User, on_delete=models.CASCADE , primary_key=True)
    email = models.EmailField(blank=True)
    phone_number = models.CharField(max_length= 13)
    employee_no = models.IntegerField (default=0)

    def __str__(self):
        return f'{self.user}'

    def save_employee (self) :
        self.save()
    def update_employee (self) :
        self.update()
    def delete_employee (self) :
        self.delete()
class Client (models.Model) :
    user = models.OneToOneField(User, on_delete=models.CASCADE , primary_key=True)
    email = models.EmailField(blank=True)
    phone_number = models.CharField(max_length= 13)
    client_no = models.IntegerField (default=0)

    def __str__(self):
        return f'{self.user}'

    def save_client (self) :
        self.save()
    def update_client (self) :
        self.update()
    def delete_client (self) :
        self.delete()

class Qoute(models.Model):
    location=models.CharField(max_length= 200)
    floor_number=models.IntegerField(default=0)
    business_name=models.CharField(max_length= 150)
    contact_person=models.CharField(max_length= 100)
    contact_no=models.IntegerField(default=+254)
    date_of_site_visit=models.DateField(("Date"), default=date.today)