# Generated by Django 3.1.2 on 2020-10-27 09:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0003_room_hotel'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='location',
            name='name',
        ),
    ]