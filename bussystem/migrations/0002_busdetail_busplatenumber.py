# Generated by Django 2.2.3 on 2019-08-16 12:20

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('bussystem', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='busdetail',
            name='busplatenumber',
            field=models.CharField(max_length=150, null=True),
        ),
    ]
