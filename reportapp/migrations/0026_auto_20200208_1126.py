# Generated by Django 3.0.2 on 2020-02-08 11:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('reportapp', '0025_auto_20200208_1108'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='topic1',
            name='user',
        ),
        migrations.AlterField(
            model_name='subtopic1',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reportapp.profile'),
        ),
    ]
