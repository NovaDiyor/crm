from api.views import *
from django.urls import path

urlpatterns = [
    path("register/", Register),
    path("sign_in/", Sign_in),
    path("logout/", LogOut),
    path("change_password/", Change_password),
    path("role/", RoleView.as_view({'get': 'list'})),
    path("staff/", StaffView.as_view({'get': 'list'})),
    path("category/", CategoryView.as_view({'get': 'list'})),
    path("info/", InfoView.as_view({'get': 'list'})),
    path("food/", FoodView.as_view({'get': 'list'})),
    path("menu/", MenutView.as_view({'get': 'list'})),
    path("rooms/", RoomsView.as_view({'get': 'list'})),
    path("ads/", AdsView.as_view({'get': 'list'})),
    path("hotel/", HotelView.as_view({'get': 'list'})),
]
