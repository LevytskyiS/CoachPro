# Generated by Django 5.0 on 2024-01-02 16:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0017_alter_profile_chronic_illness_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='Weight',
            new_name='weight',
        ),
    ]
