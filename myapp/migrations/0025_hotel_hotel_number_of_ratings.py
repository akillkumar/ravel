# Generated by Django 2.2.7 on 2019-12-03 12:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0024_hotel_hotel_rating'),
    ]

    operations = [
        migrations.AddField(
            model_name='hotel',
            name='hotel_number_of_ratings',
            field=models.IntegerField(default=0),
        ),
    ]