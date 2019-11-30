from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('places', views.places, name='places'),
    path('<int:flight_id>/', views.details, name='details'),
    path('flights/', views.filter_flights, name="filter_flights"),
    path('trains/', views.filter_trains, name="filter_trains")
]
