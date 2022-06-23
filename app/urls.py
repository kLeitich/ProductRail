from . import views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

# create url patterns
urlpatterns=[
    path('',views.home,name='home'),
    path('signup', views.signup, name = 'signup'),
    path('manager_signup', views.manager_signup_view.as_view(),name='manager_signup'),
    path('employee_signup', views.employee_signup_view.as_view(),name='employee_signup'),
    path('client_signup', views.client_signup_view.as_view(),name='client_signup'),
    path('login/',views.login_view,name="login_view"),
    path('logout',views.logout,name='logout'),
    path('qoutes',views.qoutes,name='qoutes')
    
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)