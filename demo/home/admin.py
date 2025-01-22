from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import CustomUser, ParentProfile, ChildProfile

@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'is_parent', 'is_child')

admin.site.register(ParentProfile)
admin.site.register(ChildProfile)
