from django.urls import path
from . import views


urlpatterns = [
    path('', views.book_room_page, name='results-page'),
    path('reserve/', views.book_room_page, name='reserve-page'),
]