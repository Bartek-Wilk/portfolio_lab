# Generated by Django 3.1.5 on 2021-01-23 19:04

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dary', '0002_auto_20210123_2004'),
    ]

    operations = [
        migrations.AlterField(
            model_name='donation',
            name='pick_up_time',
            field=models.TimeField(default=datetime.time(20, 4, 29, 162135)),
        ),
    ]