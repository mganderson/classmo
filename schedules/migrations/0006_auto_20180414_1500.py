# Generated by Django 2.0.1 on 2018-04-14 19:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schedules', '0005_config_primary_text_color'),
    ]

    operations = [
        migrations.AlterField(
            model_name='config',
            name='primary_color',
            field=models.CharField(blank=True, max_length=7),
        ),
        migrations.AlterField(
            model_name='config',
            name='primary_text_color',
            field=models.CharField(blank=True, max_length=7),
        ),
        migrations.AlterField(
            model_name='config',
            name='secondary_color',
            field=models.CharField(blank=True, max_length=7),
        ),
        migrations.AlterField(
            model_name='config',
            name='secondary_text_color',
            field=models.CharField(blank=True, max_length=7),
        ),
    ]
