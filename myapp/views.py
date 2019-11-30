from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from django.template import loader

from .models import Flight, Trains

def index (request):
	flight_list = Flight.objects.order_by('flight_number')[:5]
	output = ', '.join([f.flight_name for f in flight_list])

	train_list = Trains.objects.order_by('train_number')[:5]
	output = ', '.join([t.train_name for t in train_list])


	template = loader.get_template('myapp/index.html')
	context = {
		'flight_list' : flight_list,
		'train_list' : train_list, 
	}
	return render (request, 'myapp/index.html', context)

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