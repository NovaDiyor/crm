# Generated by Django 4.1 on 2022-12-04 20:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_hotel_ads'),
    ]

    operations = [
        migrations.CreateModel(
            name='HotelImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='hotel/')),
            ],
        ),
        migrations.RemoveField(
            model_name='hotel',
            name='img',
        ),
        migrations.AddField(
            model_name='hotel',
            name='img',
            field=models.ManyToManyField(to='main.hotelimage'),
        ),
    ]
