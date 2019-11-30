from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('places', views.places, name='places'),
    path('<int:flight_id>/', views.details, name='details'),
    path('$', views.filter, name="filter")
]
