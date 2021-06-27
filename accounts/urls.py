from django.contrib.auth import login
from django.urls import path
from .views import LoginView,LogOutView,SingupView
app_name='account'
urlpatterns = [
    path('login/',LoginView.as_view(),name='login'),
    path('logout/',LogOutView.as_view(),name='logout'),
    path("register/", SingupView.as_view(), name="register"),
    
]
