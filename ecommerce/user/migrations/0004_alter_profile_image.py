# Generated by Django 3.2.9 on 2021-12-15 18:50

from django.db import migrations, models
import user.models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_profile_gender'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(blank=True, default='products/images/profile_icon.png', null=True, upload_to=user.models.image_path),
        ),
    ]
