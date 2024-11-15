# Generated by Django 5.1.2 on 2024-10-16 11:28

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='doctors',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='default', max_length=200)),
                ('Email', models.CharField(default='default', max_length=200)),
                ('password', models.CharField(default='default', max_length=200)),
                ('descri', models.CharField(blank=True, max_length=200, null=True)),
                ('profile_pic', models.FileField(default='static/images/defaultImage.jpg', upload_to='static/images/')),
                ('qualification', models.CharField(default='MBBS', max_length=200)),
                ('joinDate', models.DateTimeField(blank=True, null=True)),
                ('status', models.CharField(default='active', max_length=50)),
                ('lat', models.FloatField(blank=True, null=True)),
                ('long', models.FloatField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='hospital',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=200)),
                ('profile_pic', models.FileField(default='static/images/hospital.jpg', upload_to='static/images/')),
                ('hospDescri', models.CharField(blank=True, max_length=200, null=True)),
                ('location', models.CharField(blank=True, max_length=200)),
                ('lat', models.FloatField(blank=True, null=True)),
                ('long', models.FloatField(blank=True, null=True)),
                ('dist', models.FloatField(default=2.0)),
                ('contact', models.CharField(blank=True, max_length=13)),
                ('web_site', models.URLField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='specialization',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=200, null=True)),
                ('sepcialDescri', models.CharField(default='default', max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('appPatient', models.CharField(blank=True, max_length=100, null=True)),
                ('appEmail', models.EmailField(blank=True, max_length=254, null=True)),
                ('appContact', models.CharField(blank=True, max_length=15, null=True)),
                ('appAge', models.IntegerField(blank=True, null=True)),
                ('appGender', models.CharField(blank=True, max_length=20, null=True)),
                ('appAddress', models.CharField(blank=True, max_length=300, null=True)),
                ('appBookDT', models.DateTimeField(auto_now_add=True, null=True)),
                ('appDoc', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='doctorSection.doctors')),
            ],
        ),
        migrations.AddField(
            model_name='doctors',
            name='hosp',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='doctorSection.hospital'),
        ),
        migrations.CreateModel(
            name='PasswordResetToken',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('token', models.CharField(max_length=32, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('expires_at', models.DateTimeField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='doctorSection.doctors')),
            ],
        ),
        migrations.CreateModel(
            name='PaymentForAppoint',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.FloatField(blank=True, null=True)),
                ('razorpay_order_id', models.CharField(max_length=255, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('Appoint', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='doctorSection.appointment')),
            ],
        ),
        migrations.CreateModel(
            name='Reminder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('message', models.TextField()),
                ('reminder_token', models.IntegerField(blank=True, default=1, null=True)),
                ('reminder_time', models.DateTimeField(default=None)),
                ('is_sent', models.BooleanField(default=False)),
                ('appointment', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='doctorSection.appointment')),
            ],
        ),
        migrations.AddField(
            model_name='hospital',
            name='departments',
            field=models.ManyToManyField(to='doctorSection.specialization'),
        ),
        migrations.AddField(
            model_name='doctors',
            name='specialise',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='doctorSection.specialization'),
        ),
        migrations.CreateModel(
            name='timeslot',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('start_time', models.TimeField()),
                ('end_time', models.TimeField()),
                ('slotDuration', models.IntegerField(default=5)),
                ('isBooked', models.BooleanField(default=False)),
                ('apptoken', models.IntegerField(blank=True, null=True)),
                ('timeForDoc', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='doctorSection.doctors')),
            ],
            options={
                'unique_together': {('start_time', 'end_time')},
            },
        ),
        migrations.AddField(
            model_name='appointment',
            name='time_slot',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='doctorSection.timeslot'),
        ),
    ]
