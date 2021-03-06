# Generated by Django 3.2.9 on 2021-11-28 19:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_products'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('in_stock', models.BooleanField()),
                ('currency', models.CharField(max_length=10)),
                ('brand', models.CharField(max_length=100)),
                ('description', models.TextField(max_length=1000)),
                ('images', models.TextField(max_length=1000)),
                ('gender', models.CharField(max_length=10)),
            ],
        ),
    ]
