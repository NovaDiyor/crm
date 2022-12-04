from datetime import date
from django.db import models
from io import BytesIO
import qrcode
from PIL import Image, ImageDraw
from django.core.files import File
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    status = models.IntegerField(default=3, choices=(
        (1, 'admin'),
        (2, 'staff'),
        (3, 'user'),
    ))
    phone = models.IntegerField(null=True, blank=True)
    passport = models.CharField(max_length=210, null=True, blank=True)


class Role(models.Model):
    name = models.CharField(max_length=210)


class Staff(models.Model):
    name = models.CharField(max_length=210)
    l_name = models.CharField(max_length=210)
    status = models.ForeignKey(Role, on_delete=models.SET_NULL, null=True, blank=True)
    img = models.ImageField(max_length=210)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    time = models.IntegerField(choices=(
        (1, 'Morning: from 8 a.m until 4 p.m'),
        (2, 'Afternoon: from 4 p.m until 0 p.m'),
        (3, 'Night: from 0 p.m until  8 a.m'),
    ))
    enter = models.BooleanField(default=False)
    many = models.IntegerField(default=0)
    qr = models.FileField(upload_to="Qr/", null=True, blank=True)

    def save(self, *args, **kwargs):
        qrcode_img = qrcode.make(f"{self.name}")
        canvas = Image.new("RGB", (290, 290), "white")
        draw = ImageDraw.Draw(canvas)
        canvas.paste(qrcode_img)
        name = f"{self.id}"
        buffer = BytesIO()
        canvas.save(buffer, "PNG")
        self.qr.save(name, File(buffer), save=False)
        canvas.close()
        super().save(*args, **kwargs)


class Category(models.Model):
    name = models.CharField(max_length=210)


class Info(models.Model):
    name = models.CharField(max_length=210)
    icon = models.ImageField(upload_to='info/')


class Food(models.Model):
    name = models.CharField(max_length=210)
    price = models.IntegerField()
    img = models.ImageField(upload_to='food/')
    bio = models.TextField()


class Menu(models.Model):
    day = models.DateField(auto_now_add=True)
    food = models.ManyToManyField(Food)


class Images(models.Model):
    img = models.ImageField(upload_to='rooms')


class Rooms(models.Model):
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    price = models.IntegerField()
    info = models.ManyToManyField(Info)
    bed = models.IntegerField()
    bio = models.TextField()
    tv = models.BooleanField(default=True)
    img = models.ManyToManyField(Images)
    video = models.FileField(upload_to='rooms/', null=True, blank=True)
    is_video = models.BooleanField(default=False)
    rating = models.IntegerField(choices=(
        (1, '1-start'),
        (2, '2-start'),
        (3, '3-start'),
        (4, '4-start'),
        (5, '5-start'),
    ))

    def save(self, *args, **kwargs):
        if self.video:
            is_video = True
        else:
            is_video = False
        self.is_video = is_video
        super(Rooms, self).save(*args, **kwargs)


class Description(models.Model):
    rooms = models.ForeignKey(Rooms, on_delete=models.CASCADE)
    number = models.IntegerField()
    busy = models.BooleanField(default=False)


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    room = models.ForeignKey(Description, on_delete=models.PROTECT, null=True, blank=True)
    start = models.DateField()
    end = models.DateField()

    def save(self, *args, **kwargs):
        room = self.room
        day = date.today()
        if self.start.day == day.day:
            room.busy = True
        if self.end.day == day.day:
            room.busy = False
        room.save()
        super(Order, self).save(*args, **kwargs)


class Ads(models.Model):
    name = models.CharField(max_length=210)
    img = models.ImageField(upload_to='ads/')
    url = models.CharField(max_length=210)


class Hotel(models.Model):
    name = models.CharField(max_length=210)
    city = models.CharField(max_length=210)
    rating = models.IntegerField(choices=(
        (1, '1-start'),
        (2, '2-start'),
        (3, '3-start'),
        (4, '4-start'),
        (5, '5-start'),
    ))
    rooms = models.ManyToManyField(Rooms)
    img = models.ImageField(upload_to='hotel/')


