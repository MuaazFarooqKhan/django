# Generated by Django 2.2.3 on 2019-08-30 20:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bussystem', '0010_auto_20190831_0145'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='email',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]