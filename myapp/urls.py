from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('hotels/', views.places, name='places'),
    path('f<int:flight_id>/', views.flight_details, name='flight_details'),
    path('t<int:train_id>/', views.train_details, name='trains_details'),
    path('flights/', views.filter_flights, name="filter_flights"),
    path('trains/', views.filter_trains, name="filter_trains"),
    path('flight_booking/', views.book_flight,  name="book_flight"),
    path('train_booking/', views.book_train,  name="book_train"),
    path('profile/', views.profile, name="profile"),
]
