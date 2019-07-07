# Generated by Django 2.2 on 2019-07-06 07:21

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('shop_app', '0003_medicine_publish_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='medicine',
            name='Expiry',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='medicine',
            name='MFD',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
