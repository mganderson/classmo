# Generated by Django 2.0.1 on 2018-02-21 00:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('discussions', '0006_auto_20180220_2314'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='created_date',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='comment',
            name='modified_date',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='post',
            name='created_date',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='post',
            name='modified_date',
            field=models.DateTimeField(),
        ),
    ]
