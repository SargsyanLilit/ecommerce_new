# Generated by Django 3.2.9 on 2021-12-15 18:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_auto_20211215_2232'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='gender',
            field=models.IntegerField(blank=True, choices=[(0, 'Male'), (1, 'Female')], null=True),
        ),
    ]
