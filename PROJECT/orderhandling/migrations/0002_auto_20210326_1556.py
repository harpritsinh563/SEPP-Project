# Generated by Django 3.1.5 on 2021-03-26 10:26

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orderhandling', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='expected_delivery',
            field=models.DateTimeField(default=datetime.datetime(2021, 4, 1, 15, 56, 23, 412991)),
        ),
        migrations.AlterField(
            model_name='order',
            name='order_created',
            field=models.DateTimeField(default=datetime.datetime(2021, 3, 26, 15, 56, 23, 412991)),
        ),
    ]