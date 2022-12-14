# Generated by Django 3.2.15 on 2022-09-04 20:44

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0012_alter_request_start_on'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='request',
            name='description',
        ),
        migrations.AddField(
            model_name='request',
            name='res_body',
            field=models.JSONField(default={}),
        ),
        migrations.AddField(
            model_name='request',
            name='res_status',
            field=models.CharField(default=0, max_length=500),
        ),
        migrations.AddField(
            model_name='request',
            name='type',
            field=models.CharField(choices=[('GET', 'GET'), ('POST', 'POST')], default='GET', max_length=100),
        ),
        migrations.AddField(
            model_name='request',
            name='url',
            field=models.CharField(default='', max_length=500),
        ),
        migrations.AlterField(
            model_name='request',
            name='start_on',
            field=models.DateTimeField(default=datetime.datetime(2022, 9, 4, 22, 44, 4, 456616)),
        ),
    ]
