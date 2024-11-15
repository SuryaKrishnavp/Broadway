# Generated by Django 5.1.2 on 2024-10-14 07:38

import django.db.models.deletion
import jobsection.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('usersection', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='JobPostings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Jobtitle', models.CharField(max_length=100)),
                ('Jobrole', models.CharField(max_length=100)),
                ('Job_Category', models.CharField(max_length=100)),
                ('Job_Type', models.CharField(max_length=100)),
                ('Qualification', models.CharField(default='degree', max_length=100)),
                ('Min_salary', models.FloatField()),
                ('Max_salary', models.FloatField()),
                ('Vaccancies', models.IntegerField()),
                ('Jobexperience', models.CharField(max_length=100)),
                ('Country', models.CharField(max_length=100)),
                ('State', models.CharField(max_length=100)),
                ('District', models.CharField(max_length=100)),
                ('Place', models.CharField(max_length=100)),
                ('Description', models.TextField(max_length=250)),
                ('Logo', models.ImageField(upload_to='images/')),
                ('Posted_Date', models.DateTimeField(auto_now_add=True)),
                ('Company_name', models.CharField(default='nil', max_length=100)),
                ('Company_license', models.CharField(max_length=100, null=True)),
                ('User', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='usersection.userinfo')),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('User_Photo', models.ImageField(upload_to='static/images')),
                ('User_Name', models.CharField(max_length=100)),
                ('Email', models.EmailField(max_length=254, null=True)),
                ('Phonenumber', models.CharField(max_length=12, null=True)),
                ('Title', models.CharField(max_length=100)),
                ('Qualification', models.CharField(max_length=100)),
                ('Description', models.TextField(max_length=300)),
                ('User', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='usersection.userinfo')),
            ],
        ),
        migrations.CreateModel(
            name='Applications_received',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('RelevantSkill', models.CharField(max_length=100, null=True)),
                ('Portfolio_link', models.CharField(max_length=100, null=True)),
                ('Cover_letter', models.FileField(null=True, upload_to='pdfs/covers/', validators=[jobsection.models.validate_pdf])),
                ('Resume', models.FileField(upload_to='pdfs/resumes/', validators=[jobsection.models.validate_pdf])),
                ('Applied_date', models.DateField(auto_now_add=True)),
                ('Applicant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='usersection.userinfo')),
                ('Posted_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jobsection.jobpostings')),
                ('Applicant_profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jobsection.profile')),
            ],
        ),
        migrations.CreateModel(
            name='Saved_Jobs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Saved_job', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jobsection.jobpostings')),
                ('User', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='usersection.userinfo')),
            ],
        ),
    ]
