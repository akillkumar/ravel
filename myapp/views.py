from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.contrib.auth.models import User
from collections import Counter

from .models import Flight, Trains, Buses, Hotel, Bookings, Hotel_Ratings

from datetime import date,datetime
import datetime as dt

myVar=0

def most_frequent(List): 
	occurence_count = Counter(List)
	if occurence_count:
		return occurence_count.most_common(1)[0][0]
	else:
		return -1

def index (request):
	context = {}
	flag = True
	if request.user.is_authenticated:
		bookings = Bookings.objects.filter (user=request.user)

		flight_dest_list = []
		train_dest_list = []

		flight_origin_list = []
		train_origin_list = []

		for b in bookings:
			if b.booking_type == "Flight":
				obj = get_object_or_404 (Flight, pk = b.key)
				flight_dest_list.append(obj.dest)
				flight_origin_list.append(obj.origin)
			
			if b.booking_type == "Train":
				obj = get_object_or_404 (Trains, pk = b.key)
				train_dest_list.append(obj.dest)
				train_origin_list.append(obj.origin)

		hotel_list = Hotel.objects.filter (hotel_city=most_frequent(flight_origin_list))
		if hotel_list:
			h = hotel_list.order_by('hotel_rating')[0]
		else:
			h = "Aight"

		if most_frequent(flight_origin_list) == -1 and most_frequent(train_origin_list) == -1:
			flag = False
		
		return render (request, 'myapp/index.html', {
			'flag': True,
			'hotel': h,
			'flight_origin': most_frequent(flight_origin_list),
			'flight_dest': most_frequent(flight_dest_list),
			'train_origin':  most_frequent(train_origin_list),
			'train_dest':  most_frequent(train_dest_list),
		})
	else:
		return render (request, 'myapp/index.html', {})

def details (request, flight_id):
	flight = get_object_or_404 (Flight, pk = flight_id)
	return render(request, 'myapp/details.html', {'flight' : flight})

def places (request):
	if request.method=='GET':
		city = request.GET.get('location','').split('-')[0][0:3]
		guests = request.GET.get('guests','')
		priceLow = request.GET.get('priceLow','')
		priceHigh = request.GET.get('priceHigh','')

		if not priceLow:
			priceLow=0
		if not priceHigh:
			priceHigh=120000

		checkin = request.GET.get('checkin','')
		res1 = datetime.strptime(checkin,'%m/%d/%Y')

		checkout = request.GET.get('checkout','')
		res2 = datetime.strptime(checkout,'%m/%d/%Y')

		print((res2-res1).days)

		hotel_list = Hotel.objects.filter(hotel_city__icontains = city, price__gte = priceLow, price__lte = priceHigh)
		return render (request, 'myapp/places.html', 
			context={
				'hotel_list': hotel_list,
				'city':city,
				'nights':(res2-res1).days,
				'checkin':checkin,
				'checkout':checkout,
				'guests':guests,
				'priceLow':priceLow,
				'priceHigh':priceHigh})

def flight_details (request, flight_id):
	flight = get_object_or_404 (Flight, pk = flight_id)
	return render(request, 'myapp/flight_details.html', {'flight' : flight})

def train_details (request, train_id):
	train = get_object_or_404 (Trains, pk = train_id)
	return render(request, 'myapp/train_details.html', {'train' : train})

def hotel_details (request, hotel_id):
	if request.method=='GET':
		hotel = get_object_or_404 (Hotel,pk=hotel_id)
		return render (request, 'myapp/hotel-single.html',{'hotel':hotel})

def add_review (request):
	if request.method=='POST':
		user = request.user
		hotel_id = request.POST.get('hotel')
		hotel = get_object_or_404 (Hotel, pk=hotel_id)
		rating = request.POST.get('rating')
		review = request.POST.get('review')

		x = Hotel_Ratings.objects.filter(user=user,hotel=hotel_id)
		
		if len(x):
			review = x[0].review
			print(review)
			x[0].delete()

		r = Hotel_Ratings (user=user,hotel=hotel,rating=rating,review=review)
		r.save()

		RatingList = Hotel_Ratings.objects.filter(hotel=hotel_id)
		numReviews = RatingList.count()

		sumRating = 0

		for i in RatingList:
			sumRating+=i.rating
		
		overall = sumRating/numReviews

		x = Hotel.objects.get(pk=hotel_id)
		x.hotel_rating = overall
		x.hotel_number_of_ratings = numReviews
		x.save()

		print(user,hotel,rating,review)
		return HttpResponseRedirect('/myapp/hotel/'+hotel_id)

def myFunc (request):
	if request.method=='GET':
		print('GET PARAMS:')
		origin=(request.GET.get('origin',''))
		dest=(request.GET.get('dest',''))
		
	
	return render (request, 'myapp/temp.html',{'origin':origin,'dest':dest})

def filter_flights (request):
	global myVar
	if request.method=='GET':
		origin=request.GET.get('origin','')[0:3]
		dest = request.GET.get('dest','')[0:3]
		dept = request.GET.get('dept','')
		res = datetime.strptime(dept,'%m/%d/%Y')
		print('RESSSSSSSSSSSSSS')
		print(res.day)
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
				prices[i] = '₹ '+str((prices[i][0].price)*int(passengers))
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
	b = Bookings (user=request.user, booking_type='Flight', booking_name=flight.flight_name+ " " + request.user.username , key=flight.pk)
	b.save()

	return render (request, 'myapp/flight_booking.html', {'flight': flight})

def  book_train (request):
	if request.method == "POST":
		train_id = request.POST.get('train_id', '')
	
	train = get_object_or_404 (Trains, pk = train_id)

	# Add entry
	b = Bookings (user=request.user, booking_type='Train', booking_name=train.train_name+ " " + request.user.username , key=train.pk, price = train.price)
	b.save()

	return render (request, 'myapp/train_booking.html', {'train': train})

def profile (request):
	booking_list = Bookings.objects.filter (user=request.user)
	return render (request, 'myapp/profile.html', {'user': request.user, 'booking_list': booking_list})