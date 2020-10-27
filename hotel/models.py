from django.urls import reverse
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.conf import settings
# Create your models here.


class Location(models.Model):
    #location_id,location_name,,location
    location = models.CharField(max_length=50)
    country = models.CharField(max_length=50, default="Bulgaria")

    def __str__(self):
        return self.location


class Room(models.Model):
    ROOM_STATUS = ( 
    ("1", "available"), 
    ("2", "not available"),    
    ) 

    ROOM_TYPE = (  
    ("Vila_Bor ", "VILLA BOR"),
    ("Vila Aspen","VILLA ASPEN"),
    ("Vila Ela","VILLA ELA"),
    )
    #type,no_of_rooms,capacity,prices,Hotel
    room_type = models.CharField(max_length=50, choices=ROOM_TYPE)
    capacity = models.IntegerField()
    hotel = models.ForeignKey(Location, on_delete = models.CASCADE, null=True)
    price = models.DecimalField(max_digits=6, decimal_places=2, null=True)
    size = models.IntegerField(null=True)
    status = models.CharField(choices=ROOM_STATUS, max_length=15)
    roomnumber = models.IntegerField()

    def __str__(self):
        return self.room_type


class Reservation(models.Model):

    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    check_in = models.DateTimeField(null=False)
    check_out = models.DateTimeField(null=False)
    guests = models.IntegerField(null=False)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    specials = models.TextField(
        max_length=256, null=True)
    date_posted = models.DateTimeField(auto_now_add=True)
    booking_id = models.CharField(max_length=10, default="null")

    def __str__(self):
        return self.booking_id
