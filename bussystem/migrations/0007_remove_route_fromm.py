# Generated by Django 2.2.3 on 2019-08-17 10:57

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ('bussystem', '0006_auto_20190817_0356'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='route',
            name='fromm',
        ),
    ]
