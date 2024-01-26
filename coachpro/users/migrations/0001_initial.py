# Generated by Django 5.0 on 2024-01-26 22:30

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_client', models.BooleanField(default=False)),
                ('is_coach', models.BooleanField(default=False)),
                ('age', models.IntegerField(blank=True, null=True)),
                ('weight', models.IntegerField(blank=True, null=True)),
                ('height', models.IntegerField(blank=True, null=True)),
                ('lifestyle', models.CharField(blank=True, choices=[('Active', 'Active'), ('Passive', 'Passive')], max_length=7, null=True)),
                ('blood_pressure', models.IntegerField(blank=True, null=True)),
                ('chronic_illness', models.CharField(blank=True, max_length=200)),
                ('spine', models.CharField(blank=True, max_length=200)),
                ('schedule', models.TextField(blank=True, max_length=1000)),
                ('steps', models.IntegerField(blank=True, null=True)),
                ('muscles', models.CharField(blank=True, max_length=200)),
                ('unfavourite_food', models.CharField(blank=True, max_length=200)),
                ('food_allergies', models.CharField(blank=True, max_length=200)),
                ('favourite_food', models.CharField(blank=True, max_length=200)),
                ('test_results', models.TextField(blank=True, max_length=1000)),
                ('clients', models.ManyToManyField(blank=True, null=True, related_name='clients', to=settings.AUTH_USER_MODEL)),
                ('coach', models.ManyToManyField(blank=True, null=True, related_name='coach', to=settings.AUTH_USER_MODEL)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
