# Generated by Django 4.0.3 on 2022-04-10 12:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proxyhandler', '0005_proxies_protocol'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='proxies',
            name='latency',
        ),
        migrations.AlterField(
            model_name='proxies',
            name='speed',
            field=models.FloatField(default=0.0, verbose_name='Speed in seconds'),
        ),
    ]
