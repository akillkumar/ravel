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
	global myVar
	if request.method=='GET':
		origin=request.GET.get('origin','')
		dest = request.GET.get('dest','')
		dept = request.GET.get('dept','')
		res = datetime.strptime(dept,'%m/%d/%Y')
		dates = {}
		myVar +=1
		print('my var = ', myVar)
		for i in range(6):
			dates[i] = res + dt.timedelta(days=i-2)
		
		passengers = request.GET.get('passengers','')

		

		sort = request.GET.get('sort','')
		deptTime = request.GET.get('deptTime','')

		results = Flight.objects.filter(
			origin__icontains = origin,
			dest__icontains = dest,
			dept__year = res.year,
			dept__month = res.month,
			dept__day = res.day, 
			seats__gte = passengers)
		
		if(sort):
			if(sort=='price'):
				order='price'

			if(sort=='-price'):
				order='-price'

			results.order_by(order)
		
		if deptTime:

			print('YEEEEEEEE')
			
			if deptTime=='1' or deptTime==1:
				print('NEEEEEEEEEEe')
				results.filter(dept__hour__lt = 10)
			

		
	return render (request, 'myapp/search.html', 
		{
			'flight_list': results, 
			'origin':origin,
			'dest':dest,
			'dept':dept,
			'passengers': passengers,
			'dates':dates,
			'res':res,
			'sort':sort
		})


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