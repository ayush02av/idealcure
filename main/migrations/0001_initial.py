# Generated by Django 3.1.3 on 2021-08-04 06:10

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='FAQ',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Question', models.TextField()),
                ('Answer', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Package',
            fields=[
                ('Price', models.IntegerField(primary_key=True, serialize=False)),
                ('Duration', models.CharField(max_length=10)),
                ('Description', models.TextField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('User', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='auth.user')),
                ('Age', models.IntegerField(blank=True, null=True)),
                ('Address', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Treatment',
            fields=[
                ('Name', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('Description', models.TextField()),
                ('ImageLink', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='PatientRecord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Date', models.DateTimeField(default=datetime.datetime(2021, 8, 4, 11, 40, 3, 694315))),
                ('Report', models.TextField()),
                ('Patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.patient')),
            ],
        ),
        migrations.CreateModel(
            name='PatientFile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.CharField(blank=True, max_length=50, null=True)),
                ('Date', models.DateTimeField(default=datetime.datetime(2021, 8, 4, 11, 40, 3, 694315))),
                ('File', models.FileField(upload_to='patientfiles/')),
                ('Patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.patient')),
            ],
        ),
    ]
