# Generated by Django 3.1.3 on 2021-07-05 12:45

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('consultation', '0002_slot_patient'),
    ]

    operations = [
        migrations.AlterField(
            model_name='day',
            name='Date',
            field=models.DateField(default=datetime.date(2021, 7, 5), primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='slot',
            name='TimeAlloted',
            field=models.TimeField(default=datetime.time(18, 15, 53, 340007)),
        ),
    ]
