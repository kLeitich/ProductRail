from . import views
from django.urls import path

# create url patterns
urlpatterns=[
    path('',views.home,name='home')
]