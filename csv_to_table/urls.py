

from . import views
from django.contrib.auth import views as auth_views
from django.urls import path


urlpatterns = [ #Kari CSV_TO_TABLE Commit
    path('csv_upload/', views.csv_table, name='csv_table'),
    path('today/', views.today_table, name='today_table'),
    path('search/', views.search, name='search'),
    ]