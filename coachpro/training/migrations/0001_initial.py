# Generated by Django 5.0 on 2024-02-01 18:45

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
            name='Training',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('exercise', models.CharField(max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='TrainingData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('weight', models.PositiveIntegerField()),
                ('reps', models.PositiveSmallIntegerField()),
                ('sets', models.PositiveSmallIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='TrainingPage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateField(auto_now_add=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='training_pages', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='TrainingDay',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.CharField(max_length=256)),
                ('training', models.ManyToManyField(to='training.training')),
                ('training_page', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='training_days', to='training.trainingpage')),
            ],
        ),
        migrations.CreateModel(
            name='TrainingStats',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('training', models.ManyToManyField(to='training.training')),
                ('training_data', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='training_stats', to='training.trainingdata')),
            ],
        ),
    ]
