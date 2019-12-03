from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

from .models import Flight, Trains, Buses, Hotel, Bookings


@admin.register(Bookings,Flight,Trains,Buses,Hotel)
class ViewAdmin(ImportExportModelAdmin):
    pass