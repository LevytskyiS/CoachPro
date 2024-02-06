# Generated by Django 5.0 on 2024-02-06 18:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mealplan', '0008_remove_food_day_mealinfo'),
    ]

    operations = [
        migrations.AddField(
            model_name='food',
            name='calories',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True),
        ),
        migrations.AddField(
            model_name='food',
            name='carbohydrates',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True),
        ),
        migrations.AddField(
            model_name='food',
            name='fats',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True),
        ),
        migrations.AddField(
            model_name='food',
            name='proteins',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True),
        ),
    ]