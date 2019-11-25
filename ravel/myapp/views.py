from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from django.template import loader

from .models import Flight

def index (request):
	flight_list = Flight.objects.order_by('flight_number')[:5]
	output = ', '.join([f.flight_name for f in flight_list])

	template = loader.get_template('myapp/index.html')
	context = {
		'flight_list' : flight_list, 
	}
	return render (request, 'myapp/index.html', context)

def details (request, flight_id):
	flight = get_object_or_404 (Flight, pk = flight_id)
	return render(request, 'myapp/details.html', {'flight' : flight})