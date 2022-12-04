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
    path('users/delete/<int:pk>/', delete_user, name='delete-user'),
    path('role/delete/<int:pk>/', delete_role, name='delete-role'),
    path('staff/delete/<int:pk>/', delete_staff, name='delete-staff'),
    path('category/delete/<int:pk>/', delete_category, name='delete-user'),
    path('info/delete/<int:pk>/', delete_info, name='delete-info'),
    path('food/delete/<int:pk>/', delete_food, name='delete-food'),
    path('menu/delete/<int:pk>/', delete_menu, name='delete-menu'),
    path('images/delete/<int:pk>/', delete_images, name='delete-image'),
    path('rooom/delete/<int:pk>/', delete_room, name='delete-room'),
    path('description/delete/<int:pk>/', delete_des, name='delete-des'),
    path('order/delete/<int:pk>/', delete_order, name='delete-order'),
    path('ads/delete/<int:pk>/', delete_ads, name='delete-ads'),
    path('hotel/delete/<int:pk>/', delete_hotel, name='delete-hotel'),
]
