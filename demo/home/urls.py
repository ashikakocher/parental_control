from django.contrib import admin
from django.urls import path
from home import views
from django.contrib.auth.views import LogoutView
from django.urls import path,include
from .views import set_screen_time, view_screen_time
from .views import CustomLoginView


urlpatterns = [
    path("", views.index, name="home"),
    path('', views.index, name='index'), 
    path("login_choice/", views.login_choice, name="login_choice"),
    path("home/", views.home, name="home"),
    path("contact/", views.contact, name="contact"),
    path("learnmore/", views.learnmore, name="learnmore"),
    path("child_login/", views.child_login, name="child_login"),
    path("parent_login/", views.parent_login, name="parent_login"),
    # path('redirect/', views.role_based_redirect, name='role_based_redirect'),
    path("parents_dashboard/", views.parents_dashboard, name="parents_dashboard"),
    path("child_dashboard/", views.child_dashboard, name="child_dashboard"),
    path("parentsettings/", views.parent_settings, name="parentsettings"),
    path("set_screen_time/", views.set_screen_time, name="set_screen_time"),
    path("set_usage_control/", views.set_usage_control, name="set_usage_control"),
    path("view-screen-time/", view_screen_time, name="view_screen_time"),
    path('accounts/', include('django.contrib.auth.urls')),
    path('login/', CustomLoginView.as_view(template_name="parent_login.html"), name='login'),  # Explicit template
    path('logout/', LogoutView.as_view(next_page='login_choice'), name='logout'),  # Redirect to login choice
    path('parental_signup/',views.parental_signup, name='parental_signup'),
    path("parental_signin/", views.parental_signin, name="parental_signin"), 
]