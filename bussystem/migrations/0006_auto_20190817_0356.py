# Generated by Django 2.2.3 on 2019-08-17 10:56

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ('bussystem', '0005_auto_20190817_0355'),
    ]

    operations = [
        migrations.RenameField(
            model_name='route',
            old_name='busno',
            new_name='bus_no',
        ),
    ]
