# Generated by Django 2.0.1 on 2018-04-14 17:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schedules', '0004_auto_20180414_1324'),
    ]

    operations = [
        migrations.AddField(
            model_name='config',
            name='primary_text_color',
            field=models.CharField(blank=True, default='', max_length=128),
        ),
    ]
