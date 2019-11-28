from django.contrib import admin

from .models import Flight, Trains, Buses, Hotel

admin.site.register(Flight)
admin.site.register(Trains)
admin.site.register(Buses)
admin.site.register(Hotel)