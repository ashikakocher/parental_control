from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings  # Import AUTH_USER_MODEL dynamically

# User Roles
USER_ROLE_CHOICES = (
    ('parent', 'Parent'),
    ('child', 'Child'),
)

class CustomUser(AbstractUser):  
    role = models.CharField(max_length=10, choices=USER_ROLE_CHOICES, default='parent')  # ✅ Set a valid default
    is_parent = models.BooleanField(default=False)
    is_child = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.username} ({self.role})"

class ParentProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)  
    phone = models.CharField(max_length=15, blank=True, null=True)  

    def __str__(self):
        return f"Parent Profile: {self.user.username}"
    
class ChildProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)  
    age = models.PositiveIntegerField()

    def __str__(self):
        return f"Child Profile: {self.user.username} (Age: {self.age})"

class ScreenTime(models.Model):
    child = models.ForeignKey(ChildProfile, on_delete=models.CASCADE)  # ✅ Link to ChildProfile instead of AUTH_USER_MODEL
    daily_limit = models.IntegerField(default=60)  
    time_used = models.IntegerField(default=0)  
    last_updated = models.DateField(auto_now=True)  

    def remaining_time(self):
        return max(0, self.daily_limit - self.time_used)

    def __str__(self):
        return f"{self.child.user.username} - {self.remaining_time()} min left"
from django.db import models

class Parent(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    sex = models.CharField(max_length=10)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)  # Use Django's authentication system in real projects

    class Meta:
        db_table = "users"  # This tells Django to use "users" instead of "home_parent"

    def __str__(self):
        return self.first_name + " " + self.last_name