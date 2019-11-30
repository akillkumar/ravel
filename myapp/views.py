from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth.models import User

from .models import Flight, Trains, Buses, Hotel, Bookings

def index (request):
	return render (request, 'myapp/index.html', {})

def details (request, flight_id):
	flight = get_object_or_404 (Flight, pk = flight_id)
	return render(request, 'myapp/details.html', {'flight' : flight})

def places (request):
	return render (request, 'myapp/places.html', context={})

def myFunc (request):
	if request.method=='GET':
		print('GET PARAMS:')
		origin=(request.GET.get('origin',''))
		dest=(request.GET.get('dest',''))
		
	
	return render (request, 'myapp/temp.html',{'origin':origin,'dest':dest})

def filter_flights (request):
	if request.method=='GET':
		origin=request.GET.get('origin','')
		dest = request.GET.get('dest','')
		passengers = request.GET.get('passengers','')

		print('pass = ',passengers)

		results = Flight.objects.filter(origin__icontains = origin,dest__icontains = dest, seats__gte = passengers)

	return render (request, 'myapp/temp.html', {'flight_list': results, 'origin':origin,'dest':dest})

def filter_trains (request):
	if request.method=='GET':
		origin=request.GET.get('origin','')
		dest = request.GET.get('dest','')
		x = request.GET.get('dept','')

		print('departure = ',x.split('/'))

		results = Trains.objects.filter(origin__icontains = origin,dest__icontains = dest)

	return render (request, 'myapp/temp1.html', {'train_list': results, 'origin':origin,'dest':dest})


def  book_flight (request):
	if request.method == "POST":
		flight_id = request.POST.get('flight_id', '')
		print ('my flight id is - ',flight_id)
	
	flight = get_object_or_404 (Flight, pk = flight_id)

	# Add entry
	b = Bookings (user=request.user, booking_type='Flight', key=flight.pk)
	b.save()

	return render (request, 'myapp/booking.html', {'flight': flight})

def profile (request):
	booking_list = Bookings.objects.filter (user=request.user)
	return render (request, 'myapp/profile.html', {'user': request.user, 'booking_list': booking_list})