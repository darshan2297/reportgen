# Generated by Django 3.0.2 on 2020-02-11 07:52

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reportapp', '0031_topic1_created_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='topic1',
            name='created_date',
        ),
        migrations.AddField(
            model_name='topic1',
            name='date',
            field=models.DateField(blank=True, default=datetime.date.today),
        ),
    ]
