from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import *


def error_view(request):
    return render(request, '404.html')


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = User.objects.filter(username=username)
        if user.count() > 0:
            usr = authenticate(username=username, password=password)
            if usr.status == 1:
                if usr is not None:
                    login(request, usr)
                    return redirect('dashboard')
                else:
                    return redirect('login')
            else:
                return redirect('login')
        else:
            return redirect('login')
    return render(request, 'login.html')


@login_required(login_url='login')
def logout_view(request):
    logout(request)
    return redirect('login')


@login_required(login_url='login')
def dashboard_view(request):
    return render(request, 'dashboard.html')


@login_required(login_url='login')
def staff_view(request):
    context = {
        'staff': Staff.objects.all()
    }
    return render(request, 'staff.html', context)


@login_required(login_url='login')
def users_view(request):
    context = {
        'users': User.objects.filter(status=2)
    }
    return render(request, 'users.html', context)


@login_required(login_url='login')
def rooms_view(request):
    context = {
        'room': Rooms.objects.all()
    }
    return render(request, 'rooms.html', context)


@login_required(login_url='login')
def add_user(request):
    try:
        if request.method == 'POST':
            number = 0
            username = request.POST.get('username')
            password = request.POST.get('password')
            cp = request.POST.get('confirm-password')
            phone = request.POST.get('phone')
            if cp == password:
                number += 1
                User.objects.create(username=number, first_name=username, password=password, phone=phone, status=2)
                return redirect('add-staff')
            else:
                return redirect('add-user')
    except Exception as err:
        return err
    return render(request, 'staff-user.html')


@login_required(login_url='login')
def customer_view(request):
    context = {
        'customer': User.objects.filter(status=3)
    }
    return render(request, 'customer.html', context)


@login_required(login_url='login')
def role_view(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        Role.objects.create(name=name)
        return redirect('role')
    context = {
        'role': Role.objects.all()
    }
    return render(request, 'role.html', context)


@login_required(login_url='login')
def add_staff(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        l_name = request.POST.get('l-name')
        status = request.POST.get('status')
        img = request.FILES.get('img')
        user = request.POST.get('user')
        time = request.POST.get('time')
        Staff.objects.create(name=name, l_name=l_name, status_id=status, img=img, user_id=user, time=time)
        return redirect('staff')
    us = User.objects.filter(status=2)
    context = {
        'users': us.last(),
        'role': Role.objects.all()
    }
    return render(request, 'add-staff.html', context)


@login_required(login_url='login')
def category_view(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        Category.objects.create(name=name)
        return redirect('category')
    context = {
        'category': Category.objects.all()
    }
    return render(request, 'category.html', context)


@login_required(login_url='login')
def info_view(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        img = request.FILES.get('img')
        Info.objects.create(name=name, img=img)
        return redirect('info')
    context = {
        'info': Info.objects.all()
    }
    return render(request, 'info.html', context)


@login_required(login_url='login')
def food_view(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        img = request.FILES.get('img')
        bio = request.POST.get('bio')
        Food.objects.create(name=name, img=img, bio=bio)
        return redirect('food')
    context = {
        'food': Food.objects.all()
    }
    return render(request, 'food.html', context)


@login_required(login_url='login')
def menu_view(request):
    if request.method == 'POST':
        food = request.POST.getlist('food')
        m = Menu.objects.create()
        for i in food:
            m.food.add(i)
        return redirect('menu')
    context = {
        'food': Food.objects.all(),
        'menu': Menu.objects.all()
    }
    return render(request, 'menu.html', context)


@login_required(login_url='login')
def get_menu(request, pk):
    mn = Menu.objects.get(id=pk)
    context = {
        'menu': mn.food.all()
    }
    return render(request, 'get-menu.html', context)


@login_required(login_url='login')
def get_info(request, pk):
    info = Rooms.objects.get(id=pk)
    context = {
        'info': info.info.all()
    }
    return render(request, 'get-info.html', context)


@login_required(login_url='login')
def get_img(request, pk):
    image = Rooms.objects.get(id=pk)
    context = {
        'img': image.img.all()
    }
    return render(request, 'get-image.html', context)


@login_required(login_url='login')
def image_view(request):
    try:
        if request.method == 'POST':
            img = request.FILES.get('img')
            Images.objects.create(img=img)
            return redirect('image')
        context = {
            'img': Images.objects.all()
        }
        return render(request, 'images.html', context)
    except Exception as err:
        return err


@login_required(login_url='login')
def room_view(request):
    context = {
        'room': Rooms.objects.all()
    }
    return render(request, 'room.html', context)


@login_required(login_url='login')
def add_room(request):
    try:
        if request.method == 'POST':
            request = request.POST.get
            category = request('category')
            price = request('price')
            info = request.POST.getlist('info')
            bed = request('bed')
            bio = request('bio')
            tv = request('tv')
            if tv is None:
                tv = False
            img = request.POST.getlist('img')
            video = request.FILES.get('video')
            rm = Rooms.objects.create(category_id=category, price=price, bed=bed, bio=bio, tv=tv, video=video)
            for i in info:
                rm.info.add(i)
            for i in img:
                rm.img.add(i)
            return redirect('room')
        context = {
            'img': Images.objects.all(),
            'category': Category.objects.all(),
            'info': Info.objects.all(),
        }
        return render(request, 'add-room.html', context)
    except Exception as err:
        return err


@login_required(login_url='login')
def des_view(request):
    try:
        if request.method == 'POST':
            room = request.POST.get('room')
            number = request.POST.get('number')
            rm = Rooms.objects.all()
            for i in rm:
                if i.id == room:
                    return redirect('des')
                else:
                    Description.objects.create(rooms_id=room, number=number)
                    return redirect('description')
        context = {
            'room': Rooms.objects.all(),
            'des': Description.objects.all()
        }
        return render(request, 'description.html', context)
    except Exception as err:
        return err


@login_required(login_url='login')
def order_view(request):
    try:
        if request.method == 'POST':
            user = request.POST.get('user')
            room = request.POST.get('room')
            start = request.POST.get('start')
            end = request.POST.get('end')
            Order.objects.create(user_id=user, room_id=room, start=start, end=end)
            return redirect('order')
        context = {
            'users': User.objects.filter(status=3),
            'room': Description.objects.all(),
            'order': Order.objects.all()
        }
        return render(request, 'order.html', context)
    except Exception as err:
        return err


@login_required(login_url='login')
def ads_view(request):
    try:
        if request.method == 'POST':
            name = request.POST.get('name')
            img = request.FILES.get('img')
            url = request.POST.get('url')
            Ads.objects.create(name=name, img=img, url=url)
            return redirect('ads')
        context = {
            'ads': Ads.objects.all()
        }
        return render(request, 'ads.html', context)
    except Exception as err:
        return err


@login_required(login_url='login')
def hotel_images_view(request):
    if request.method == 'POST':
        img = request.FILES.get('img')
        HotelImage.objects.create(img=img)
        return redirect('hotel-image')
    context = {
        'img': HotelImage.objects.all()
    }
    return render(request, 'hotel-image.html', context)


@login_required(login_url='login')
def hotel_view(request):
    context = {
        'hotel': Hotel.objects.all()
    }
    return render(request, 'hotel.html', context)


@login_required(login_url='login')
def add_hotel(request):
    try:
        if request.method == 'POST':
            name = request.POST.get('name')
            city = request.POST.get('city')
            rating = request.POST.get('rating')
            room = request.POST.getlist('room')
            img = request.POST.getlist('img')
            ads = request.POST.getlist('ads')
            h = Hotel.objects.create(name=name, city=city, rating=rating)
            for i in room:
                h.rooms.add(i)
            for i in img:
                h.img.add(i)
            for i in ads:
                h.ads.add(i)
            return redirect('hotel')
        context = {
            'room': Rooms.objects.all(),
            'hotel': HotelImage.objects.all(),
            'ads': Ads.objects.all(),
        }
        return render(request, 'add-hotel.html', context)
    except Exception as err:
        return err


@login_required(login_url='login')
def update_user(request, pk):
    try:
        usr = User.objects.get(id=pk)
        if request.method == 'POST':
            username = request.POST.get('username')
            phone = request.POST.get('phone')
            usr.first_name = username
            usr.phone = phone
            usr.save()
            return redirect('users')
        context = {
            'users': usr
        }
        return render(request, 'update-user.html', context)
    except Exception as err:
        return err


@login_required(login_url='login')
def update_role(request, pk):
    try:
        rl = Role.objects.get(id=pk)
        if request.method == 'POST':
            name = request.POST.get('name')
            rl.name = name
            rl.save()
            return redirect('role')
        context = {
            'role': rl
        }
        return render(request, 'update-role.html', context)
    except Exception as err:
        return err


@login_required(login_url='login')
def update_staff(request, pk):
    try:
        st = Staff.objects.get(id=pk)
        print(st.status)
        if request.method == 'POST':
            status = request.POST.get('status')
            time = request.POST.get('time')
            st.status_id = status
            st.time = time
            st.save()
            return redirect('staff')
        context = {
            'role': Role.objects.all(),
            'staff': st
        }
        return render(request, 'update-staff.html', context)
    except Exception as err:
        print(err)


@login_required(login_url='login')
def update_category(request, pk):
    try:
        cg = Category.objects.get(id=pk)
        if request.method == 'POST':
            name = request.POST.get('name')
            cg.name = name
        context = {
            'category': cg
        }
        return render(request, 'update-category.html', context)
    except Exception as err:
        return err


@login_required(login_url='login')
def update_info(request, pk):
    try:
        io = Info.objects.get(id=pk)
        if request.method == 'POST':
            name = request.POST.get('name')
            icon = request.FILES.get('icon')
            io.name = name
            if icon:
                io.icon = icon
            else:
                io.icon = io.icon
        context = {
            'info': io
        }
        return render(request, 'update-info.html', context)
    except Exception as err:
        return err


@login_required(login_url='login')
def update_food(request, pk):
    try:
        fd = Food.objects.get(id=pk)
        if request.method == 'POST':
            name = request.POST.get('name')
            price = request.POST.get('price')
            img = request.FILES.get('img')
            bio = request.POST.get('bio')
            fd.name = name
            fd.price = price
            if img:
                fd.img = img
            else:
                fd.img = fd.img
            fd.bio = fd.bio
            return redirect('food')
        context = {
            'food': fd
        }
        return render(request, 'update-food.html', context)
    except Exception as err:
        return err


@login_required(login_url='login')
def update_menu(request, pk):
    try:
        mn = Menu.objects.get(id=pk)
        if request.method == 'POST':
            day = request.POST.get('day')
            food = request.POST.getlist('menu')
            mn.day = day
            mn.food.clean()
            for i in food:
                mn.food.add(i)
            return redirect('menu')
        context = {
            'menu': mn,
            'food': Food.objects.all()
        }
        return render(request, 'update-menu.html', context)
    except Exception as err:
        return err


@login_required(login_url='login')
def update_images(request, pk):
    try:
        im = Images.objects.get(id=pk)
        if request.method == 'POST':
            img = request.POST.get('img')
            if img:
                im.img = img
            else:
                im.img = im.img
            return redirect('image')
        return render(request, 'update-images.html')
    except Exception as err:
        return err


@login_required(login_url='login')
def update_room(request, pk):
    try:
        rm = Rooms.objects.get(id=pk)
        if request.method == 'POST':
            request = request.POST.get
            category = request('category')
            price = request('price')
            info = request.POST.getlist('info')
            bed = request('bed')
            bio = request('bio')
            tv = request('tv')
            if tv is None:
                tv = False
            img = request.POST.getlist('img')
            video = request.FILES.get('video')
            rm.category_id = category
            rm.price = price
            rm.bed = bed
            rm.bio = bio
            rm.tv = tv
            if video:
                rm.video = video
            else:
                rm.video = video
            rm.info.clean()
            for i in info:
                rm.info.add(i)
            rm.img.clean()
            for i in img:
                rm.img.add(i)
            return redirect('room')
        context = {
            'img': Images.objects.all(),
            'info': Info.objects.all(),
            'room': rm,
        }
        return render(request, 'update-room.html', context)
    except Exception as err:
        return err


@login_required(login_url='login')
def update_des(request, pk):
    try:
        de = Description.objects.get(id=pk)
        if request.method == 'POST':
            room = request.POST.get('room')
            number = request.POST.get('number')
            busy = request.POST.get('busy')
            de.room_id = room
            de.number = number
            de.busy = busy
        context = {
            'about': de
        }
        return render(request, 'update-about.html', context)
    except Exception as err:
        return err


@login_required(login_url='login')
def update_order(request, pk):
    try:
        rd = Order.objects.get(id=pk)
        if request.method == 'POST':
            user = request.POST.get('user')
            room = request.POST.get('room')
            start = request.POST.get('start')
            end = request.POST.get('end')
            rd.user_id = user
            rd.room_id = room
            rd.start = start
            rd.end = end
            return redirect('order')
        context = {
            'order': rd
        }
        return render(request, 'update-order.html', context)
    except Exception as err:
        return err


@login_required(login_url='login')
def update_ads(request, pk):
    try:
        ads = Ads.objects.get(id=pk)
        if request.method == 'POST':
            name = request.POST.get('name')
            img = request.FILES.get('img')
            url = request.POST.get('url')
            if img:
                ads.img = img
            else:
                ads.img = ads.img
            ads.name = name
            ads.url = url
        context = {
            'ads': ads
        }
        return render(request, 'update-ads.html', context)
    except Exception as err:
        return err


@login_required(login_url='login')
def update_hotel_image(request, pk):
    try:
        im = HotelImage.objects.get(id=pk)
        if request.method == 'POST':
            img = request.POST.get('img')
            if img:
                im.img = img
            else:
                im.img = im.img
            return redirect('hotel-image')
        context = {
            'img': im
        }
        return render(request, 'update-hotel-img.html', context)
    except Exception as err:
        return err


@login_required(login_url='login')
def update_hotel(request, pk):
    try:
        ht = Hotel.objects.get(id=pk)
        if request.method == 'POST':
            name = request.POST.get('name')
            city = request.POST.get('city')
            rating = request.POST.get('rating')
            room = request.POST.getlist('room')
            img = request.POST.getlist('img')
            ads = request.POST.getlist('ads')
            ht.name = name
            ht.city = city
            ht.rating = rating
            ht.rooms.clean()
            for i in room:
                ht.rooms.add(i)
            ht.img.clean()
            for i in img:
                ht.img.add(i)
            ht.ads.clean()
            for i in ads:
                ht.ads.add(i)
        context = {
            'hotel': ht,
            'room': Rooms.objects.all(),
            'img': HotelImage.objects.all(),
            'ads': Ads.objects.all(),
        }
        return render(request, 'update-hotel.html', context)
    except Exception as err:
        return err


def delete_user(request, pk):
    User.objects.get(id=pk).delete()
    return redirect('user')


@login_required(login_url='login')
def delete_role(request, pk):
    Role.objects.get(id=pk).delete()
    return redirect('role')


@login_required(login_url='login')
def delete_staff(request, pk):
    Staff.objects.get(id=pk).delete()
    return redirect('staff')


@login_required(login_url='login')
def delete_category(request, pk):
    Category.objects.get(id=pk).delete()
    return redirect('category')


@login_required(login_url='login')
def delete_info(request, pk):
    Info.objects.get(id=pk).delete()
    return redirect('info')


@login_required(login_url='login')
def delete_food(request, pk):
    Food.objects.get(id=pk).delete()
    return redirect('food')


@login_required(login_url='login')
def delete_menu(request, pk):
    Menu.objects.get(id=pk).delete()
    return redirect('menu')


@login_required(login_url='login')
def delete_images(request, pk):
    Images.objects.get(id=pk).delete()
    return redirect('images')


@login_required(login_url='login')
def delete_room(request, pk):
    Rooms.objects.get(id=pk).delete()
    return redirect('room')


@login_required(login_url='login')
def delete_des(request, pk):
    Description.objects.get(id=pk).delete()
    return redirect('description')


@login_required(login_url='login')
def delete_order(request, pk):
    Order.objects.get(id=pk).delete()
    return redirect('order')


@login_required(login_url='login')
def delete_ads(request, pk):
    Ads.objects.get(id=pk).delete()
    return redirect('ads')


@login_required(login_url='login')
def delete_hotel(request, pk):
    Hotel.objects.get(id=pk).delete()
    return redirect('hotel')








