from django.contrib import admin
from .models import CustomUser, ParentProfile, ChildProfile, ScreenTime  # Import other models

admin.site.register(CustomUser)
admin.site.register(ParentProfile)
admin.site.register(ChildProfile)
admin.site.register(ScreenTime)