from django.shortcuts import render,redirect
# from app.forms import QouteForm, client_signup, employee_signup, login_form, manager_signup
from .models import User
from django.views.generic import CreateView
from django.contrib.auth import authenticate,login
from django.contrib import auth
from django.contrib import messages

# Create your views here.
def home(request):
    return render(request,'index.html')

def signup(request):
    return render(request,'register.html' )

class manager_signup_view (CreateView):
    model = User
    form_class = manager_signup
    template_name = 'sign_up.html'

    def get_context_data(self, **kwargs):
        kwargs ['user_type'] = 'manager'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        return redirect('/login')

class employee_signup_view(CreateView):
    model = User
    form_class = employee_signup
    template_name = 'sign_up.html'

    def get_context_data(self, **kwargs):
        kwargs ['user_type'] = 'employee'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        return redirect('/login')
class client_signup_view(CreateView):
    model = User
    form_class = client_signup
    template_name = 'sign_up.html'

    def get_context_data(self, **kwargs):
        kwargs ['user_type'] = 'client'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        return redirect('/login')

def login_view(request):
  form = login_form(request.POST or None)
  if request.method == 'POST':
    if form.is_valid():
      username = form.cleaned_data.get('username')
      password = form.cleaned_data.get('password')
      user = authenticate(username=username,password=password)
      if user is not None and user.is_manager:
        login(request, user)
        return redirect('/')
      elif user is not None and user.is_employee:
        login(request, user)
        return redirect('/')
      elif user is not None and user.is_client:
        login(request, user)
        return redirect('/')
  return render (request, 'login.html',{'form':form})


def logout(request):
    auth.logout(request)
    return redirect ('/')

# def qoutes(request):
#   current_user=request.user

#   if request.method == 'POST':
#     form = QouteForm(request.POST, request.FILES)
#     if form.is_valid():
#       post = form.save(commit=False)
#       post.user = current_user
           
#       post.save()
            

#       messages.success(request, f'Your qoute has been sent.')    
#       return redirect('posts')
#   else:
#     form=QouteForm()
#   return render(request,'qoutes.html',{'form':form})