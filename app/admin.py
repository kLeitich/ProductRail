from django.contrib import admin

from app.models import Client, Employee, Manager, Qoute, User

# Register your models here.
admin.site.register(User)
admin.site.register(Manager)
admin.site.register(Employee)
admin.site.register(Client)
admin.site.register(Qoute)