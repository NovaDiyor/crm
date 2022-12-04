from django.urls import path
from .views import *

urlpatterns = [
    path('404', error_view, name='error'),
    path('', login_view, name='login'),
    path('dashboard/', dashboard_view, name='dashboard'),
]
