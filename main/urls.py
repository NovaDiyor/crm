from django.urls import path
from .views import *

urlpatterns = [
    path('404', error_view, name='error'),
    path('', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('dashboard/', dashboard_view, name='dashboard'),
    path('role/', role_view, name='role'),
    path('staff/users/', users_view, name='users'),
    path('staff/', staff_view, name='staff'),
    path('staff/add/', add_staff, name='add-staff'),
    path('staff/user/add/', add_user, name='add-user'),
    path('role/delete/<int:pk>/', delete_role, name='delete-role'),
    path('users/delete/<int:pk>/', delete_user, name='delete-user'),
]
