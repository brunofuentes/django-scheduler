# Generated by Django 3.2.15 on 2022-09-04 18:44

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0011_alter_request_start_on'),
    ]

    operations = [
        migrations.AlterField(
            model_name='request',
            name='start_on',
            field=models.DateTimeField(default=datetime.datetime(2022, 9, 4, 20, 44, 45, 419694)),
        ),
    ]
