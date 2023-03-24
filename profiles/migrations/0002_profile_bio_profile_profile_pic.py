# Generated by Django 4.1.6 on 2023-03-21 13:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='bio',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='profile_pic',
            field=models.ImageField(blank=True, upload_to='profile_pics/'),
        ),
    ]
