from api.serializer import *
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import login, logout, authenticate
from rest_framework.authentication import BasicAuthentication, SessionAuthentication
from rest_framework.decorators import permission_classes, authentication_classes, api_view

@api_view(["POST"])
def Register(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        colum_password = request.POST['colum_password']
        if password == colum_password:
            user = User.objects.create_user(username=username, password=password)
            login(request, user)
            return Response({"username": username, "password": password})
        return Response({"error": "password error"})
    return Response("Error")


@api_view(["POST"])
def Sign_in(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = User.objects.get(username=username)
        if user is not None:
            usr = authenticate(username=username, password=password)
            if usr is not None:
                login(request, usr)
                return Response("Done")
            return Response({"error": "password error"})
        return Response({"error": "username error"})
    return Response("Error")


@api_view(["POST"])
@permission_classes([IsAuthenticated])
@authentication_classes([BasicAuthentication, SessionAuthentication])
def LogOut(request):
    logout(request)
    return Response("Done")


@api_view(["POST"])
@permission_classes([IsAuthenticated])
@authentication_classes([BasicAuthentication, SessionAuthentication])
def Change_password(request):
    user = request.user
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        new_password = request.POST['new_password']
        colum_password = request.POST['colum_password']
        usr = User.objects.get(id=user.id)
        if usr.username == username:
            if authenticate(username=username, password=password) is not None:
                if new_password == colum_password:
                    usr.set_password(new_password)
                    return Response("Done")
                return Response({"error": "new_password error"})
            return Response({"error": "password error"})
        return Response({"error": "username error"})
    return Response("Error")


class RoleView(viewsets.ReadOnlyModelViewSet):
    queryset = Role.objects.all()
    serializer_class = RoomsSerializer


class StaffView(viewsets.ReadOnlyModelViewSet):
    queryset = Staff.objects.all()
    serializer_class = StaffSerializer


class CategoryView(viewsets.ReadOnlyModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class InfoView(viewsets.ReadOnlyModelViewSet):
    queryset = Info.objects.all()
    serializer_class = InfoSerializer


class FoodView(viewsets.ReadOnlyModelViewSet):
    queryset = Food.objects.all()
    serializer_class = FoodSerializer


class RestaurantView(viewsets.ReadOnlyModelViewSet):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer


class RoomsView(viewsets.ReadOnlyModelViewSet):
    queryset = Rooms.objects.all()
    serializer_class = RoomsSerializer


class AdsView(viewsets.ReadOnlyModelViewSet):
    queryset = Ads.objects.all()
    serializer_class = AdsSerializer


class HotelView(viewsets.ReadOnlyModelViewSet):
    queryset = Hotel.objects.all()
    serializer_class = HotelSerializer

