from . import views
from django.contrib.auth import views as auth_views
from django.urls import path

urlpatterns = [
    path('', views.start, name='start'),
    path('staff/', views.staff, name='staff'),
    path('password_change/', views.ChangePassword, name='password_change'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    
]
