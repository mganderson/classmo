# Generated by Django 2.0.1 on 2018-02-24 18:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schedules', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='session',
            name='registered_students',
            field=models.IntegerField(default=0),
        ),
    ]
