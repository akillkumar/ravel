from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.contrib.auth.models import User
from collections import Counter

from .models import Flight, Trains, Buses, Hotel, Bookings, Hotel_Ratings

from datetime import date,datetime
import datetime as dt

import operator

myVar=0

def most_frequent(List): 
	occurence_count = Counter(List)
	if occurence_count:
		return occurence_count.most_common(1)[0][0]
	else:
		return -1

cityCodes = {'AGX': 'Agatti Island', 'AMD': 'Ahmedabad', 'AJL': 'Aizawl', 'AKD': 'Akola', 'IXV': 'Along', 'LKO': 'Lucknow', 'LUH': 'Ludhiana', 'IXB': 'Bagdogra', 'IXE': 'Mangalore', 'IXL': 'Leh', 'RGH': 'Balurghat', 'IXD': 'Allahabad', 'SHL': 'Shillong', 'BEK': 'Bareli', 'BEP': 'Bellary', 'BLR': 'Bangalore', 'BUP': 'Bhatinda', 'BHU': 'Bhavnagar', 'BHO': 'Bhopal', 'BBI': 'Bhubaneswar', 'BKB': 'Bikaner', 'PAB': 'Bilaspur', 'IXR': 'Ranchi', 'GAU': 'Guwahati', 'CBD': 'Car Nicobar', 'IXC': 'Chandigarh', 'MAA': 'Chennai', 'BOM': 'Mumbai', 'IXU': 'Aurangabad', 'COK': 'Kochi', 'COH': 'Cooch Behar', 'CDP': 'Cuddapah', 'UDR': 'Udaipur', 'GOI': 'Goa', 'NMB': 'Daman', 'DAE': 'Daparizo', 'DAI': 'Darjeeling', 'DED': 'Dehra Dun', 'DEP': 'Deparizo', 'IDR': 'Indore', 'DBD': 'Dhanbad', 'DIB': 'Dibrugarh', 'DMU': 'Dimapur', 'DIU': 'Diu', 'DHM': 'Dharamsala', 'ISK': 'Nasik', 'GAY': 'Gaya', 'GOP': 'Gorakhpur', 'JGA': 'Jamnagar', 'GUX': 'Guna', 'GWL': 'Gwalior', 'HSS': 'Hissar', 'HBX': 'Hubli', 'HYD': 'Hyderabad', 'DEL': 'New Delhi', 'JLR': 'Jabalpur', 'JGB': 'Jagdalpur', 'JSA': 'Jaisalmer', 'PYB': 'Jeypore', 'JDH': 'Jodhpur', 'IXH': 'Kailashahar', 'IXQ': 'Kamalpur', 'IXY': 'Kandla', 'KNU': 'Kanpur', 'IXK': 'Keshod', 'HJR': 'Khajuraho', 'AGR': 'Agra', 'IXN': 'Khowai', 'KLH': 'Kolhapur', 'KTU': 'Kota', 'CCJ': 'Kozhikode', 'KUU': 'Bhuntar Kullu.', 'IXS': 'Silchar', 'IXI': 'Lilabari', 'PNQ': 'Pune', 'IXM': 'Madurai', 'LDA': 'Malda', 'MOH': 'Mohanbari', 'IMF': 'Imphal', 'MZA': 'Muzaffarnagar', 'MZU': 'Muzaffarpur', 'MYQ': 'Mysore', 'NDC': 'Nanded', 'CCU': 'Kolkata', 'NVY': 'Neyveli', 'OMN': 'Osmanabad', 'PGH': 'Pantnagar', 'IXT': 'Pasighat', 'IXP': 'Pathankot', 'PAT': 'Patna', 'CJB': 'Coimbatore', 'PNY': 'Pondicherry', 'PBD': 'Porbandar', 'IXZ': 'Port Blair', 'PUT': 'Puttaparthi', 'RPR': 'Raipur', 'ATQ': 'Amritsar', 'RJA': 'Rajahmundry', 'RAJ': 'Rajkot', 'RJI': 'Rajouri', 'RMD': 'Ramagundam', 'RTC': 'Ratnagiri', 'REW': 'Rewa', 'RRK': 'Rourkela', 'JRH': 'Jorhat', 'BHJ': 'Bhuj', 'RUP': 'Rupsi', 'SXV': 'Salem', 'TEZ': 'Tezpur', 'IXG': 'Belgaum', 'JAI': 'Jaipur', 'TNI': 'Satna', 'IXJ': 'Jammu', 'SSE': 'Sholapur', 'SLV': 'Simla', 'IXA': 'Agartala', 'IXW': 'Jamshedpur', 'NAG': 'Nagpur', 'SXR': 'Srinagar', 'STV': 'Surat', 'TEI': 'Tezu', 'TJV': 'Thanjavur', 'TRV': 'Trivandrum', 'TIR': 'Tirupati', 'TRZ': 'Trichy', 'TCR': 'Tuticorin', 'BDQ': 'Vadodara', 'VNS': 'Varanasi', 'VGA': 'Vijayawada', 'VTZ': 'Vishakhapatnam', 'WGC': 'Warangal', 'ZER': 'Zero'}

def index (request):
	context = {}

	books = Bookings.objects.all()
	fdests = {}
	tdests = {}
	for x in books:
		if x.booking_type=='Flight':
			f = Flight.objects.get(pk=x.key)
			res = f.dest

			if res in fdests:
				fdests[res]+=1
			else:
				fdests[res]=1
		
		elif x.booking_type=='Train':
			t = Trains.objects.get(pk=x.key)
			if t.dest in tdests:
				tdests[t.dest]+=1
			else:
				tdests[t.dest]=1
	print(fdests)
	print(tdests)

	frec1 = {}
	frec2 = {}
	trec1 = {}
	trec2 = {}

	frec1['location'] = (sorted(fdests.items(), key=operator.itemgetter(1))[-1][0])
	frec1['numFlights'] = Flight.objects.filter(dest=frec1['location']).count()
	frec1['minPrice'] = Flight.objects.filter(dest=frec1['location']).order_by('price')[0:3]
	
	frec2['location'] = (sorted(fdests.items(), key=operator.itemgetter(1))[-2][0])
	frec2['numFlights'] = Flight.objects.filter(dest=frec2['location']).count()
	frec2['minPrice'] = Flight.objects.filter(dest=frec2['location']).order_by('price')[0:3]
	
	trec1['location'] = (sorted(tdests.items(), key=operator.itemgetter(1))[-1][0])
	trec1['numTrains'] = Trains.objects.filter(dest=trec1['location']).count()
	trec1['minPrice'] = Trains.objects.filter(dest=trec1['location']).order_by('price')[0:3]

	trec2['location'] = (sorted(tdests.items(), key=operator.itemgetter(1))[-2][0])
	trec2['numTrains'] = Trains.objects.filter(dest=trec2['location']).count()
	trec2['minPrice'] = Trains.objects.filter(dest=trec2['location']).order_by('price')[0:3]

	hots = Hotel.objects.all().order_by('-hotel_rating')[0:5]






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
			'frec1': frec1,
			'frec2': frec2,
			'trec1': trec1,
			'trec2': trec2,
			'hots':hots

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
		reviews = Hotel_Ratings.objects.filter(hotel=hotel_id)

		loc = hotel.hotel_city
		recs = Hotel.objects.filter(hotel_city = loc).order_by('hotel_rating')[0:3]
		print('RECSSSSSSSSSSS')
		print(recs)
		res = {}
		for x in range(len(recs)):
			res[x] = recs[x]

		return render (request, 'myapp/hotel-single.html',
						{'hotel':hotel,
						'reviews':reviews,
						'ratingRangeFull':range(int(hotel.hotel_rating)),
						'ratingRangeEmpty':range(5-int(hotel.hotel_rating)),
						'recs':recs})

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
		passengers = request.POST.get('passengers', '')
	
	flight = get_object_or_404 (Flight, pk = flight_id)
	print (passengers)

	# Add entry
	b = Bookings (user=request.user, booking_type='Flight', booking_name=flight.flight_name+ " " + request.user.username , key=flight.pk, travellers = passengers, price=int(passengers)*flight.price)
	b.save()

	return render (request, 'myapp/flight_booking.html', {'flight': flight, 'booking': b})

def  book_train (request):
	if request.method == "POST":
		train_id = request.POST.get('train_id', '')
		passengers = request.POST.get('passengers', '')
	
	train = get_object_or_404 (Trains, pk = train_id)

	# Add entry
	b = Bookings (user=request.user, booking_type='Train', booking_name=train.train_name+ " " + request.user.username , key=train.pk, travellers = passengers, price=int(passengers)*train.price)
	b.save()

	return render (request, 'myapp/train_booking.html', {'train': train, 'booking': b})



def  book_hotel (request):
	if request.method == "POST":
		hotel_id = request.POST.get('hotel_id', '')
	
	hotel = get_object_or_404 (Hotel, pk = hotel_id)

	# Add entry
	b = Bookings (user=request.user, booking_type='Hotel', booking_name=hotel.hotel_name+ " " + request.user.username , key=hotel.pk, price = hotel.price)
	b.save()

	return render (request, 'myapp/hotel_booking.html', {'hotel': hotel, 'booking': b})

def profile (request):
	booking_list = Bookings.objects.filter (user=request.user)
	return render (request, 'myapp/profile.html', {'user': request.user, 'booking_list': booking_list})