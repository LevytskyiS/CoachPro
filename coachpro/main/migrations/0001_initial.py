# Generated by Django 5.0 on 2024-01-03 22:25

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
            name='NotePage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Note',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(max_length=1000)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='notes', to=settings.AUTH_USER_MODEL)),
                ('note_page', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='notes', to='main.notepage')),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_client', models.BooleanField(default=False)),
                ('is_coach', models.BooleanField(default=False)),
                ('age', models.IntegerField(null=True)),
                ('weight', models.IntegerField(null=True)),
                ('height', models.IntegerField(null=True)),
                ('lifestyle', models.CharField(choices=[('A', 'Active'), ('P', 'Passive')], max_length=1, null=True)),
                ('blood_pressure', models.IntegerField(null=True)),
                ('chronic_illness', models.CharField(max_length=200)),
                ('spine', models.CharField(max_length=200)),
                ('schedule', models.TextField(max_length=1000)),
                ('steps', models.IntegerField(null=True)),
                ('muscles', models.CharField(max_length=200)),
                ('unfavourite_food', models.CharField(max_length=200)),
                ('food_allergies', models.CharField(max_length=200)),
                ('favourite_food', models.CharField(max_length=200)),
                ('test_results', models.TextField(max_length=1000)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='photo')),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='photos', to='main.profile')),
            ],
        ),
        migrations.AddField(
            model_name='notepage',
            name='profile',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='notepage', to='main.profile'),
        ),
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='file')),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='files', to='main.profile')),
            ],
        ),
        migrations.CreateModel(
            name='Weight',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now_add=True)),
                ('value', models.DecimalField(decimal_places=2, max_digits=5)),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='weights', to='main.profile')),
            ],
        ),
    ]
