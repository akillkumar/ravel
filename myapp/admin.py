from django.contrib import admin

from .models import Flight, Trains, Buses, Hotel, Bookings

admin.site.register(Flight)
admin.site.register(Trains)
admin.site.register(Buses)
admin.site.register(Hotel)
admin.site.register(Bookings)