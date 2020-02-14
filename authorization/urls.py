from . import views
from django.contrib.auth import views as auth_views
from django.urls import path
from .views import ItemInfoUpdate, GroupPaymentsUpdate, CreateNewGroup, CreateNewDaily, ItemGroupsUpdate, DeletePeople, DeleteGroups, DeleteGroup

urlpatterns = [
    path('', views.start, name='start'),
    path('staff/', views.staff, name='staff'),
    path('groups/', views.groups, name='groups'),
    path('groups_payments/', views.groups_payments, name='groups_payments'),
    path('pay_filter/<int:pk>', views.pay_filter, name='pay_filter'),

   


    path('create_group/', CreateNewGroup.as_view(), name='create_group'),
    path('create_daily/', CreateNewDaily.as_view(), name='create_daily'),


    path('item/<int:pk>/group_del', DeleteGroup.as_view(), name='group_delete'),
    path('item/<int:pk>/groups_del', DeleteGroups.as_view(), name='groups_delete'),
    path('item/<int:pk>/item_del', DeletePeople.as_view(), name='group_payments_delete'),
    
    path('item/<int:pk>/item_info', ItemInfoUpdate.as_view(), name='item_info_update'),
    path('item/<int:pk>/group_payments', GroupPaymentsUpdate.as_view(), name='group_payments_update'),
    path('item/<int:pk>/item_groups', ItemGroupsUpdate.as_view(), name='item_groups_update'),


    path('ok/', views.OkView, name='ok_view'),
    path('password_change/', views.ChangePassword, name='password_change'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),


]
