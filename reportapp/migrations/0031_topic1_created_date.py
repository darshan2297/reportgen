# Generated by Django 3.0.2 on 2020-02-11 07:36

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reportapp', '0030_remove_topic1_created_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='topic1',
            name='created_date',
            field=models.DateField(default=datetime.date.today),
        ),
    ]
