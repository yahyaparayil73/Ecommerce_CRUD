# Generated by Django 4.1.7 on 2023-03-13 09:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('common', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('p_name', models.CharField(max_length=50)),
                ('p_description', models.CharField(max_length=50)),
                ('p_number', models.BigIntegerField()),
                ('p_stock', models.BigIntegerField()),
                ('p_price', models.BigIntegerField()),
                ('p_category', models.CharField(max_length=50)),
                ('p_image', models.ImageField(upload_to='product/')),
                ('seller', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='common.seller')),
            ],
            options={
                'db_table': 'product',
            },
        ),
    ]