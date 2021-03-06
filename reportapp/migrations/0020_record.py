# Generated by Django 3.0.2 on 2020-02-07 14:15

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('reportapp', '0019_subtopic_topic'),
    ]

    operations = [
        migrations.CreateModel(
            name='record',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(blank=True, default=datetime.date.today)),
                ('subtopic', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reportapp.subtopic')),
                ('topic', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reportapp.topic')),
            ],
        ),
    ]
