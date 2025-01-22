from django.contrib import admin
from django.urls import path
from home import views
urlpatterns = [
    path("", views.index,name="home"),
    path("login/", views.login_choice,name="login_choice"),
    path("child_login/", views.child_login,name="child_login"),
    path("parent_login/", views.parent_login,name="parent_login"),
    path('redirect/', views.role_based_redirect, name='role_based_redirect'),
    path("parents_dashboard/", views.parents_dashboard,name="parents_dashboard"),
    path("parentsettings/", views.parentsettings,name="parentsettings"),
    path("about", views.about,name="about"),
    path("service", views.service,name="service"),
    path("contact", views.contact,name="contact")
]
