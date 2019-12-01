from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth.models import User

from .models import Flight, Trains, Buses, Hotel, Bookings

from datetime import date,datetime
import datetime as dt

myVar=0

def index (request):
	return render (request, 'myapp/index.html', {})

def details (request, flight_id):
	flight = get_object_or_404 (Flight, pk = flight_id)
	return render(request, 'myapp/details.html', {'flight' : flight})

def places (request):
	hotel_list = Hotel.objects.all()
	return render (request, 'myapp/places.html', context={'hotel_list': hotel_list})

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
		airline = request.GET.get('airline','')
		arrivalTime = request.GET.get('arrivalTime','')
		fclass = request.GET.get('class','')

		

		results = Flight.objects.filter(
			origin__icontains = origin,
			dest__icontains = dest,
			dept__year = res.year,
			dept__month = res.month,
			dept__day = res.day, 
			seats__gte = passengers)

		prices = {}
		for i in range(6):
			prices[i] = Flight.objects.filter(
			origin__icontains = origin,
			dest__icontains = dest,
			dept__year = dates[i].year,
			dept__month = dates[i].month,
			dept__day = dates[i].day, 
			seats__gte = passengers).order_by('price')

			if len(prices[i]):
				prices[i] = '₹ '+str(prices[i][0].price)
			else:
				prices[i] = '-'

		print('HELLOOOOOOOOOOOo')
		print(results)
		
		if(sort):
			print('yes, sort')
			if(sort=='price'):
				order='price'

			if(sort=='-price'):
				order='-price'

			results = results.order_by(order)
		
		if deptTime:

			print('YEEEEEEEE')
			
			if deptTime=='0' or deptTime==0:
				lo = '00:00'
				hi = '06:00'
			elif deptTime=='1':
				lo = '06:00'
				hi = '12:00'
			elif deptTime=='2':
				lo = '12:00'
				hi = '20:00'
			else:
				lo = '20:00'
				hi = '23:59'
			
			begin = datetime.strptime(lo, '%H:%M').time()
			end = datetime.strptime(hi, '%H:%M').time()
			results = results.filter(deptTime__range=(begin, end))

		if arrivalTime:

			print('YEEEEEEEE')
			
			if arrivalTime=='0' or arrivalTime==0:
				lo = '00:00'
				hi = '06:00'
			elif arrivalTime=='1':
				lo = '06:00'
				hi = '12:00'
			elif arrivalTime=='2':
				lo = '12:00'
				hi = '20:00'
			else:
				lo = '20:00'
				hi = '23:59'
			
			begin = datetime.strptime(lo, '%H:%M').time()
			end = datetime.strptime(hi, '%H:%M').time()
			results = results.filter(arrivalTime__range=(begin, end))

		if fclass:
			results = results.filter(flight_class__iexact = fclass)

		if airline:

			results = results.filter(airline__iexact = airline)
			

		
	return render (request, 'myapp/search_flights.html', 
		{
			'flight_list': results, 
			'origin':origin,
			'dest':dest,
			'dept':dept,
			'passengers': passengers,
			'dates':dates,
			'res':res,
			'sort':sort,
			'deptTime':deptTime,
			'airline':airline,
			'arrivalTime':arrivalTime,
			'class':fclass,
			'prices':prices
		})


def filter_trains (request):
	global myVar
	if request.method=='GET':
		origin=request.GET.get('origin','')
		dest = request.GET.get('dest','')
		dept = request.GET.get('dept','')
		res = datetime.strptime(dept,'%m/%d/%Y')
		dates = {}
		myVar +=1
		for i in range(6):
			dates[i] = res + dt.timedelta(days=i-2)
		
		passengers = request.GET.get('passengers','')

		

		sort = request.GET.get('sort','')
		deptTime = request.GET.get('deptTime','')
		arrivalTime = request.GET.get('arrivalTime','')
		tclass = request.GET.get('class','')

		

		results = Trains.objects.filter(
			origin__icontains = origin,
			dest__icontains = dest,
			dept__year = res.year,
			dept__month = res.month,
			dept__day = res.day, 
			seats__gte = passengers)

		prices = {}
		for i in range(6):
			prices[i] = Trains.objects.filter(
			origin__icontains = origin,
			dest__icontains = dest,
			dept__year = dates[i].year,
			dept__month = dates[i].month,
			dept__day = dates[i].day, 
			seats__gte = passengers).order_by('price')

			if len(prices[i]):
				prices[i] = '₹ '+str(prices[i][0].price)
			else:
				prices[i] = '-'

		if(sort):
			print('yes, sort')
			if(sort=='price'):
				order='price'

			if(sort=='-price'):
				order='-price'

			results = results.order_by(order)
		
		if deptTime:

			if deptTime=='0' or deptTime==0:
				lo = '00:00'
				hi = '06:00'
			elif deptTime=='1':
				lo = '06:00'
				hi = '12:00'
			elif deptTime=='2':
				lo = '12:00'
				hi = '20:00'
			else:
				lo = '20:00'
				hi = '23:59'
			
			begin = datetime.strptime(lo, '%H:%M').time()
			end = datetime.strptime(hi, '%H:%M').time()
			results = results.filter(deptTime__range=(begin, end))

		if arrivalTime:

			if arrivalTime=='0' or arrivalTime==0:
				lo = '00:00'
				hi = '06:00'
			elif arrivalTime=='1':
				lo = '06:00'
				hi = '12:00'
			elif arrivalTime=='2':
				lo = '12:00'
				hi = '20:00'
			else:
				lo = '20:00'
				hi = '23:59'
			
			begin = datetime.strptime(lo, '%H:%M').time()
			end = datetime.strptime(hi, '%H:%M').time()
			results = results.filter(arrivalTime__range=(begin, end))

		if tclass:
			results = results.filter(flight_class__iexact = tclass)

		
	

		
	return render (request, 'myapp/search_trains.html', 
		{
			'train_list': results, 
			'origin':origin,
			'dest':dest,
			'dept':dept,
			'passengers': passengers,
			'dates':dates,
			'res':res,
			'sort':sort,
			'deptTime':deptTime,
			'arrivalTime':arrivalTime,
			'class':tclass,
			'prices':prices
		})




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