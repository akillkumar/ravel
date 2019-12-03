from django.contrib import admin

from .models import Flight, Trains, Buses, Hotel, Bookings, Hotel_Ratings

admin.site.register(Flight)
admin.site.register(Trains)
admin.site.register(Buses)
admin.site.register(Hotel)
admin.site.register(Bookings)
admin.site.register(Hotel_Ratings)