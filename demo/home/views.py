from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login, authenticate, logout
from .forms import ParentSignupForm, ChildSignupForm,CustomUserCreationForm
from .models import CustomUser
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from .models import ScreenTime
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import check_password


class CustomLoginView(LoginView):
    template_name = 'login.html'

# Homepage
def index(request):
    return render(request, 'index.html')

def home(request):
    return render(request, 'home.html')

def contact(request):
    return render(request, 'contact.html')

# Login Choice Page
def login_choice(request):
    return render(request, 'login_choice.html')

def child_login(request):
    return render(request, 'child_login.html')

def parent_login(request):
    return render(request, 'parent_login.html')

# def parental_signup(request):
#     return render(request, 'parental_signup.html')

# Parent Signup View
def parent_signup(request):
    if request.method == 'POST':
        form = ParentSignupForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.role = 'parent'  # Assign role
            user.set_password(form.cleaned_data['password1'])  # Hash password
            user.save()
            login(request, user)  # Auto login
            return redirect('parents_dashboard')  # Redirect parent after signup
    else:
        form = ParentSignupForm()
    return render(request, 'parent_login.html', {'form': form})

# Child Signup View
def child_signup(request):
    if request.method == 'POST':
        form = ChildSignupForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.role = 'child'  # Assign role
            user.set_password(form.cleaned_data['password1'])  # Hash password
            user.save()
            login(request, user)  # Auto login
            return redirect('child_dashboard')  # Redirect child after signup
    else:
        form = ChildSignupForm()
    return render(request, 'child_login.html', {'form': form})

# Login View (Django Built-in)
from django.contrib.auth.views import LoginView

class CustomLoginView(LoginView):
    template_name = 'login.html'

# Role-Based Redirection
# def role_based_redirect(request):
#     if request.user.is_authenticated:
#         if request.user.role == 'parent':
#             return redirect('parent_dashboard')
#         elif request.user.role == 'child':
#             return redirect('child_dashboard')
#     return redirect('index')  # Default redirection for unauthenticated users

# Parent Dashboard
# def parents_dashboard(request):
#     return render(request, 'parents_dashboard.html')


# Child Dashboard
def child_dashboard(request):
    return render(request, 'child_dashboard.html')

# Parent Settings Page
def parent_settings(request):
    return render(request, 'parentsettings.html')

# Logout View
from django.contrib.auth import logout

def user_logout(request):
    logout(request)
    return redirect('login_choice')  # Redirect to login choice after logout

# Additional Static Pages
def about(request):
    return HttpResponse("This is the About page")

def service(request):
    return HttpResponse("This is the Service page")

def register(request):
    return render(request, 'register.html')
def learnmore(request):
    return render(request, 'learnmore.html')

def set_screen_time(request):
    return render(request, "set_screen_time.html")

def set_usage_control(request):
    return render(request, "set_usage_control.html")

@login_required
def view_screen_time(request):
    screen_time = ScreenTime.objects.filter(child=request.user).first()
    return render(request, "child_dashboard.html", {"screen_time": screen_time})
import mysql.connector as sql
fn=''
ln=''
s=''
em=''
pwd=''

# Create your views here.
from django.shortcuts import render, redirect
from .models import Parent  # Ensure this model exists
from django.contrib import messages

from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password
from django.contrib import messages
from home.models import Parent  # Ensure this model is correctly imported
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.hashers import make_password, check_password  # Import hashing functions
from .models import Parent  # Import your Parent model
from django.contrib.auth.hashers import make_password  # Ensure this is imported

def parental_signup(request):
    if request.method == "POST":
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        sex = request.POST.get("sex")
        email = request.POST.get("email")
        password = request.POST.get("password")

        if not all([first_name, last_name, sex, email, password]):
            messages.error(request, "All fields are required.")
            return redirect("parental_signup")

        if Parent.objects.filter(email=email).exists():
            messages.error(request, "Email is already registered.")
            return redirect("parental_signup")

        try:
            parent = Parent.objects.create(
                first_name=first_name,
                last_name=last_name,
                sex=sex,
                email=email,
                password=make_password(password.strip()),  # Hash password before saving
            )
            messages.success(request, "Signup successful! Please sign in.")
            return redirect("parental_signin")  # Redirect to login
        except Exception as e:
            print(f"Signup Error: {e}")  # Log error instead of exposing it
            messages.error(request, "An error occurred. Please try again.")
            return redirect("parental_signup")

    return render(request, "parental_signup.html")

from django.contrib.auth import authenticate, login
from django.contrib.auth.hashers import check_password
from django.contrib import messages

def parental_signin(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")

        try:
            parent = Parent.objects.get(email=email)
            print("DEBUG: Parent found in DB:", parent.email)

            if check_password(password, parent.password):
                print("DEBUG: Password matched!")
                request.session["parent_id"] = parent.id
                request.session.set_expiry(3600)
                messages.success(request, "Login successful!")
                return redirect("parents_dashboard")
            else:
                print("DEBUG: Password mismatch!")
                messages.error(request, "Invalid email or password.")
                return redirect("parental_signin")
        except Parent.DoesNotExist:
            print("DEBUG: Parent does not exist")
            messages.error(request, "Invalid email or password.")
            return redirect("parental_signin")

    return render(request, "parent_login.html")


def parents_dashboard(request):
    if "parent_id" not in request.session:
        messages.error(request, "You must be logged in.")
        return redirect("parental_signin")  # Fixed redirect

    try:
        parent = Parent.objects.get(id=request.session["parent_id"])  # Get parent object
        return render(request, "parents_dashboard.html", {"parent": parent})  # Pass parent data
    except Parent.DoesNotExist:
        # Handle the case where the parent is no longer in the database
        del request.session["parent_id"]  # Clear invalid session
        messages.error(request, "Parent account not found.")
        return redirect("parental_signin")