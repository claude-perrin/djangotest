# Generated by Django 4.0.3 on 2022-04-10 10:28

import datetime
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('proxyhandler', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='proxies',
            name='Ip',
        ),
        migrations.RemoveField(
            model_name='proxies',
            name='Latency',
        ),
        migrations.RemoveField(
            model_name='proxies',
            name='Port',
        ),
        migrations.RemoveField(
            model_name='proxies',
            name='Speed',
        ),
        migrations.RemoveField(
            model_name='proxies',
            name='Success',
        ),
        migrations.RemoveField(
            model_name='proxies',
            name='Updated',
        ),
        migrations.RemoveField(
            model_name='proxies',
            name='pub_date',
        ),
        migrations.AddField(
            model_name='proxies',
            name='anonymity',
            field=models.TextField(default=None),
        ),
        migrations.AddField(
            model_name='proxies',
            name='country',
            field=models.TextField(default=None),
        ),
        migrations.AddField(
            model_name='proxies',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='date published'),
        ),
        migrations.AddField(
            model_name='proxies',
            name='latency',
            field=models.IntegerField(default=0, verbose_name='Latency in ms'),
        ),
        migrations.AddField(
            model_name='proxies',
            name='protocol',
            field=models.TextField(default=None),
        ),
        migrations.AddField(
            model_name='proxies',
            name='socket',
            field=models.TextField(default=None, unique=True),
        ),
        migrations.AddField(
            model_name='proxies',
            name='speed',
            field=models.IntegerField(default=0, verbose_name='Speed in ms'),
        ),
        migrations.AddField(
            model_name='proxies',
            name='success',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='proxies',
            name='updated',
            field=models.DateTimeField(default=datetime.datetime(1, 1, 1, 0, 0), verbose_name='Updated'),
        ),
    ]
