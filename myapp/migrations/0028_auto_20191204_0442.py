# Generated by Django 2.2.7 on 2019-12-03 23:12

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0027_remove_hotel_totalprice'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookings',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2019, 12, 4, 4, 42, 22, 536126)),
        ),
    ]