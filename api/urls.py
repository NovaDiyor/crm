from api.views import *
from django.urls import path

urlpatterns = [
    path("register/", Register),
    path("sign_in/", Sign_in),
    path("logout/", LogOut),
    path("change_password/", Change_password),
    path("Role", RoleView.as_view({'get': 'list'})),
    path("Staff", StaffView.as_view({'get': 'list'})),
    path("Category", CategoryView.as_view({'get': 'list'})),
    path("Info", InfoView.as_view({'get': 'list'})),
    path("Food", FoodView.as_view({'get': 'list'})),
    path("Restaurant", RestaurantView.as_view({'get': 'list'})),
    path("Rooms", RoomsView.as_view({'get': 'list'})),
    path("Ads", AdsView.as_view({'get': 'list'})),
    path("Hotel", HotelView.as_view({'get': 'list'})),
]