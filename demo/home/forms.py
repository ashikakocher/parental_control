from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser



# Parent Signup Form

class ParentSignupForm(UserCreationForm):
    phone = forms.CharField(max_length=15, required=True) # Additional parent field



    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'phone', 'password1', 'password2']



# Child Signup Form

class ChildSignupForm(UserCreationForm):
    age= forms.IntegerField(required=True) # Additional child field

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'age', 'password1', 'password2']



from django.contrib.auth.models import User



class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)

class Meta:
    model = User
    fields = ["username", "email", "password1", "password2"]
