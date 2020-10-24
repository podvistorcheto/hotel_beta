from django.contrib import admin
from .models import Room, Reservation
# Register your models here.


class RoomAdmin(admin.ModelAdmin):
    list_display = (
        'room_type',
        'size',
        'price',
        'capacity',
        'roomnumber',
    )
    readonly_fields = ('pk',)

    ordering = ('roomnumber',)


class ReservationAdmin(admin.ModelAdmin):
    list_display = (
        'first_name',
        'last_name',
        'user',
        'room',
        'guests',
        'check_in',
        'check_out',
        'specials',
        )
    readonly_fields = ('pk', 'date_posted')

    ordering = ('date_posted',)

admin.site.register(Room, RoomAdmin)
admin.site.register(Reservation, ReservationAdmin)