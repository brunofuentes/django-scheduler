# Generated by Django 3.2.15 on 2022-09-04 16:27

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_alter_request_start_on'),
    ]

    operations = [
        migrations.AlterField(
            model_name='request',
            name='start_on',
            field=models.DateTimeField(default=datetime.datetime(2022, 9, 4, 18, 27, 53, 308734)),
        ),
    ]
