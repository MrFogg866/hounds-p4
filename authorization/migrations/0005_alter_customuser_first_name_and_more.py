# Generated by Django 4.1.6 on 2023-03-21 13:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authorization', '0004_alter_customuser_last_login'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='first_name',
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='last_name',
            field=models.CharField(max_length=150),
        ),
    ]