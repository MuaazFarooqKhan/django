# Generated by Django 2.2.3 on 2019-08-30 19:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bussystem', '0004_auto_20190831_0011'),
    ]

    operations = [
        migrations.AlterField(
            model_name='routee',
            name='booked_seats',
            field=models.CharField(max_length=3000, null=True),
        ),
    ]
