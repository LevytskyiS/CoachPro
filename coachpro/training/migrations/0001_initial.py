# Generated by Django 5.0 on 2024-01-07 12:00

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TrainingPage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateField(auto_now_add=True)),
                ('profile', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='trainingpage', to='main.profile')),
            ],
        ),
        migrations.CreateModel(
            name='Training',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(max_length=1000)),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='trainings', to='main.profile')),
                ('training_page', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='training', to='training.trainingpage')),
            ],
        ),
    ]
