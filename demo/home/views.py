from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User

from django.contrib.auth import login, authenticate
from .forms import ParentSignupForm, ChildSignupForm
from .models import CustomUser

# Create your views here.
def index (request):
    return render(request, 'index.html')
def login_choice(request):
    return render(request, 'login_choice.html')



# Parent signup view
def parent_signup(request):
    if request.method == 'POST':
        form = ParentSignupForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_parent = True
            user.set_password(form.cleaned_data['password'])  # Save hashed password
            user.save()
            return redirect('login_choice')  # Redirect to login choice page after signup
    else:
        form = ParentSignupForm()
    return render(request, 'home/parent_login.html', {'form': form})

# Child signup view
def child_signup(request):
    if request.method == 'POST':
        form = ChildSignupForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_child = True
            user.set_password(form.cleaned_data['password'])  # Save hashed password
            user.save()
            return redirect('login_choice')  # Redirect to login choice page after signup
    else:
        form = ChildSignupForm()
    return render(request, 'home/child_login.html', {'form': form})

# Role-based redirection view
def role_based_redirect(request):
    if request.user.is_authenticated:
        if request.user.is_parent:
            return redirect('parent_dashboard')
        elif request.user.is_child:
            return redirect('child_dashboard')
    return redirect('index')  # Default redirection to index if not authenticated


def child_login(request):
    return render(request, 'child_login.html')

def parent_login(request):
    return render(request, 'parent_login.html')


def parents_dashboard(request):
    return render(request, 'parents_dashboard.html')

def parentsettings(request):
    return render(request, 'parentsettings.html')

def logout(request):
    return render(request, 'login_choice.html')
    
    
def about (request):
    return HttpResponse("this is about page")

def service (request):
    return HttpResponse("this is service page")

def contact (request):
    return HttpResponse("this is contact page")