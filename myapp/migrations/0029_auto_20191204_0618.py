# Generated by Django 2.2.7 on 2019-12-04 00:48

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0028_auto_20191204_0442'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookings',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2019, 12, 4, 6, 18, 48, 638510)),
        ),
        migrations.AlterField(
            model_name='hotel_ratings',
            name='rating',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='hotel_ratings',
            name='review',
            field=models.CharField(default='', max_length=500, null=True),
        ),
    ]
