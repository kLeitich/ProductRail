from django import forms
from django.db import transaction
from django.forms import ModelForm
from .models import *
from django.contrib.auth.forms import UserCreationForm 


class manager_signup(UserCreationForm):
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    email_address = forms.EmailField(required=True)
    phone_number = forms.CharField(required=True)
    profile_pic = forms.ImageField()

    class Meta (UserCreationForm.Meta):
        model = User
    @transaction.atomic
    def save(self):
            user = super().save(commit=False)
            user.first_name = self.cleaned_data.get('first_name')
            user.last_name = self.cleaned_data.get('last_name')
            user.is_manager  = True
            user.save()
            manager = Manager.objects.create(user=user)
            manager.email_address = self.cleaned_data.get('email_address')
            manager.phone_number = self.cleaned_data.get('phone_number')
            manager.profile_pic = self.cleaned_data.get('profile_pic')

            return manager
        

class employee_signup(UserCreationForm):
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    email = forms.EmailField()
    registration_no = forms.CharField(required=True)
    phone_number = forms.CharField(required=True)
    profile_pic = forms.ImageField()
    gender = forms.CharField(required=True)

    class Meta(UserCreationForm.Meta):
        model = User

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.first_name = self.cleaned_data.get('first_name')
        user.last_name = self.cleaned_data.get('last_name')        
        user.is_employee = True
        user.save()
        employee = Employee.objects.create(user=user)
        employee.registration_no = self.cleaned_data.get('reg_no')
        employee.email = self.cleaned_data.get('email')
        employee.phone_number = self.cleaned_data.get('phone_number')
        employee.profile_pic = self.cleaned_data.get('profile_pic')
        employee.gender = self.cleaned_data.get('gender')

        return employee

class client_signup(UserCreationForm):
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    email = forms.EmailField()
    registration_no = forms.CharField(required=True)
    phone_number = forms.CharField(required=True)
    profile_pic = forms.ImageField()
    gender = forms.CharField(required=True)

    class Meta(UserCreationForm.Meta):
        model = User

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.first_name = self.cleaned_data.get('first_name')
        user.last_name = self.cleaned_data.get('last_name')        
        user.is_employee = True
        user.save()
        client = Client.objects.create(user=user)
        client.registration_no = self.cleaned_data.get('reg_no')
        client.email = self.cleaned_data.get('email')
        client.phone_number = self.cleaned_data.get('phone_number')
        client.profile_pic = self.cleaned_data.get('profile_pic')
        client.gender = self.cleaned_data.get('gender')

        return client

class login_form(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={"class":"form-control"}
        )
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={"class":"form-control"}
        )
    )