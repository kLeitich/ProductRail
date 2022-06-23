from django.db import models

# Create your models here.
class User (AbstractUser):
    USERNAME_FIELD = 'username'
    is_matron = models.BooleanField('matron status',default = False) 
    is_student = models.BooleanField('student status',default = False) 
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)

    def save_user (self) :
        self.save()
    def update_user (self) :
        self.update()
    def delete_user (self) :
        self.delete()
    
class Matron (models.Model) :
    user = models.OneToOneField(User, on_delete=models.CASCADE , primary_key=True,)
    profile_pic = CloudinaryField ('image')
    email = models.EmailField(blank=True)
    phone_number = models.CharField(max_length= 13)

    def __str__(self):
        return f'{self.user}'

    def save_matron (self) :
        self.save()
    def update_matron (self) :
        self.update()
    def delete_matron (self) :
        self.delete()

class Student (models.Model) :
    user = models.OneToOneField(User, on_delete=models.CASCADE , primary_key=True)
    profile_pic = CloudinaryField ('image')
    email = models.EmailField(blank=True)
    phone_number = models.CharField(max_length= 13)
    registration_no = models.CharField (max_length=20)

    def __str__(self):
        return f'{self.user}'

    def save_student (self) :
        self.save()
    def update_student (self) :
        self.update()
    def delete_student (self) :
        self.delete()
