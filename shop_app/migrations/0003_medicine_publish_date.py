# Generated by Django 2.2 on 2019-06-30 06:36

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('shop_app', '0002_medicine'),
    ]

    operations = [
        migrations.AddField(
            model_name='medicine',
            name='Publish_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
