# Generated by Django 2.2.7 on 2019-11-30 11:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0010_auto_20191130_1618'),
    ]

    operations = [
        migrations.AddField(
            model_name='flight',
            name='airline',
            field=models.CharField(default='', max_length=30),
        ),
        migrations.AlterField(
            model_name='flight',
            name='flight_name',
            field=models.CharField(default='', max_length=30),
        ),
    ]
