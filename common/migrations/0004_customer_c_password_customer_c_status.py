# Generated by Django 4.1.7 on 2023-03-07 11:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0003_rename_c_phone_number_customer_c_mobile'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='c_password',
            field=models.CharField(default='', max_length=30),
        ),
        migrations.AddField(
            model_name='customer',
            name='c_status',
            field=models.CharField(default='active', max_length=25),
        ),
    ]
