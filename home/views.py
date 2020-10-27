from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from hotel.models import Location, Room, Reservation
from django.contrib import messages
from django.contrib.auth.models import User
import datetime


def index(request):
    return render(request, "home/index.html")

''' Initial search page '''
def searchpage(request):
    all_location = Location.objects.all()
    if request.method == "POST":
        try:
            print(request.POST)
            location = Location.objects.all().get(id=int(request.POST['search_location']))
            reserve_room = []

            ''' to find the room already booked and exclude them from the query set'''
            for each_reservation in Reservation.objects.all():
                if str(each_reservation.check_in) < str(request.POST['cin']) and str(each_reservation.check_out) < str(request.POST['cout']):
                    pass
                elif str(each_reservation.check_in) > str(request.POST['cin']) and str(each_reservation.check_out) > str(request.POST['cout']):
                    pass
                else:
                    reserve_room.append(each_reservation.rood.id)

            room = Room.objects.all().filter(hotel=hotel, capacity_gte = int(request.POST['capacity'])).exclude(id_in=reserve_room)
            if len(room) == 0:
                messages.warning(request, "Sorry. No rooms are available for these dates")
                data = {'rooms': room, 'all_location': all_location, 'flag': True}
                response = render(request, 'room_results.html', data)
        except Exception as e:
            messages.error(request, e)
            response = render(request, 'room_results.html', {'all_location': all_location})
    
    else:
        data = {'all_location': all_location}
        response = render(request, 'home/index.html', data)
    return HttpResponse(response)

