# Generated by Django 5.0 on 2024-01-31 19:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('training', '0003_remove_training_reps_remove_training_sets_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trainingday',
            name='training',
            field=models.ManyToManyField(to='training.training'),
        ),
    ]
