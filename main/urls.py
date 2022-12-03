from django.urls import path
from .views import *

urlpatterns = [
    path('', error_view, name='error'),
    path('login/', login_view, name='login'),
    path('dashboard/', dashboard_view, name='dashboard'),
]
