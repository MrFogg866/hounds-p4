# Generated by Django 4.1.6 on 2023-03-24 18:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0008_profile_bio_profile_birthdate_profile_location_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='birthdate',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='slug',
        ),
    ]
