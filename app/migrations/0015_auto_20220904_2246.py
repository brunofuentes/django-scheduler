# Generated by Django 3.2.15 on 2022-09-04 20:46

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0014_auto_20220904_2244'),
    ]

    operations = [
        migrations.AlterField(
            model_name='request',
            name='res_body',
            field=models.JSONField(default=dict),
        ),
        migrations.AlterField(
            model_name='request',
            name='start_on',
            field=models.DateTimeField(default=datetime.datetime(2022, 9, 4, 22, 46, 2, 447027)),
        ),
    ]
