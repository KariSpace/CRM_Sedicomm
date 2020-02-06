from . import views
from django.contrib.auth import views as auth_views
from django.urls import path
from .views import ItemInfoUpdate, ItemPaymentsUpdate, CreateNewGroup, CreateNewDaily, ItemGroupsUpdate

urlpatterns = [
    path('', views.start, name='start'),
    path('staff/', views.staff, name='staff'),
    path('groups/', views.groups, name='groups'),
    path('groups_payments/', views.groups_payments, name='groups_payments'),
    path('ok/', views.OkView, name='ok_view'),
    path('create_group/', CreateNewGroup.as_view(), name='create_group'),
    path('create_daily/', CreateNewDaily.as_view(), name='create_daily'),
    path('item/<int:pk>/item_info', ItemInfoUpdate.as_view(), name='item_info_update'),
    path('item/<int:pk>/item_payments', ItemPaymentsUpdate.as_view(), name='item_payments_update'),
    path('item/<int:pk>/item_groups', ItemGroupsUpdate.as_view(), name='item_groups_update'),
    path('password_change/', views.ChangePassword, name='password_change'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),

]
