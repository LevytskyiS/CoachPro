# Generated by Django 5.0 on 2023-12-31 20:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_alter_profile_is_client'),
    ]

    operations = [
        migrations.CreateModel(
            name='HomePageArticle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('content', models.TextField(max_length=1000)),
            ],
        ),
    ]