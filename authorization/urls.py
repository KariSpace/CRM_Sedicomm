from . import views
from django.contrib.auth import views as auth_views
from django.urls import path
from .views import ItemInfoUpdate

urlpatterns = [
    path('', views.start, name='start'),
    path('staff/', views.staff, name='staff'),
    path('groups/', views.groups, name='groups'),
    path('ok/', views.OkView, name='ok_view'),
    path('item/<int:pk>/item_info', ItemInfoUpdate.as_view(), name='item_info_update'),
    path('password_change/', views.ChangePassword, name='password_change'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),

    #Kari CSV_TO_TABLE Commit
    path('csv_upload/', views.csv_table, name='csv_table'),
    path('today/', views.today_table, name='today_table'),
]
