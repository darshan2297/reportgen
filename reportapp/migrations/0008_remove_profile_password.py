# Generated by Django 3.0.2 on 2020-02-06 08:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reportapp', '0007_auto_20200206_0832'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='password',
        ),
    ]
