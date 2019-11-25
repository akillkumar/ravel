from django.db import models
from datetime import datetime, timedelta

# Some defaults
def default_start_time():
    now = datetime.now()
    start = now.replace(hour=22, minute=0, second=0, microsecond=0)
    return start if start > now else start + timedelta(days=1)  

# Every class is a table in our DB, and we make use of django's ORM to simplify back end calls
class Flight (models.Model):
	flight_name = models.CharField (max_length = 10, default = "")
	flight_number = models.IntegerField (unique = True)

	origin = models.CharField (max_length = 4)
	dest = models.CharField (max_length = 4)
	
	duration = models.FloatField (default=0.0)
	dept = models.DateTimeField (auto_now = False, default=default_start_time)
	arrival = models.DateTimeField (auto_now = False, default=default_start_time)
	
	flight_class = models.CharField (max_length = 20, default = "")
	seats = models.IntegerField (default = 0)
	price = models.FloatField (default=0.0)
	
	def __str__(self):
		return self.flight_name

class Trains (models.Model):
	train_name = models.CharField (max_length = 10, default = "")
	train_number = models.IntegerField (unique = True, default = 00)

	origin = models.CharField (max_length = 4, default = "")
	dest = models.CharField (max_length = 4, default = "")
	
	duration = models.FloatField (default=0.0)
	dept = models.DateTimeField (auto_now = False, default=default_start_time)
	arrival = models.DateTimeField (auto_now = False, default=default_start_time)
	
	train_class = models.CharField (max_length = 20, default = "")
	seats = models.IntegerField (default = 0)
	price = models.FloatField (default=0.0)

	def __str__(self):
		return self.train_name

class Buses (models.Model):
	bus_name = models.CharField (max_length = 15, default = "")
	bus_number = models.IntegerField (unique = True)

	origin = models.CharField (max_length = 4, default = "")
	dest = models.CharField (max_length = 4, default = "")
	
	duration = models.FloatField (default=0.0)
	dept = models.DateTimeField (auto_now = False, default=default_start_time)
	arrival = models.DateTimeField (auto_now = False, default=default_start_time)

	bus_class = models.CharField (max_length = 20, default = "")
	seats = models.IntegerField (default = 0)
	price = models.FloatField (default=0.0)

	def __str__(self):
		return self.bus_name
	
class Hotel (models.Model):
	hotel_name = models.CharField (max_length = 20, default = "")
	hotel_description = models.CharField  (max_length = 50, default = "")

	hotel_address = models.CharField (max_length = 50, default = "")
	hotel_city = models.CharField (max_length = 4, default = "")
	hotel_zip = models.IntegerField (default = 0)

	# deets
	hotel_beds = models.IntegerField (default = 0)
	hotel_baths = models.IntegerField (default = 0)
	hotel_rooms = models.IntegerField (default = 0)
	hotel_kitchen = models.BooleanField (default = False)
	hotel_ac = models.BooleanField (default = False)

	hotel_class = models.CharField (max_length = 15, default = "")
	available_rooms = models.IntegerField (default = 0)
	price = models.FloatField (default = 0.0)
	
	def __str__(self):
		return self.hotel_name
	


	