# Generated by Django 3.0.2 on 2020-02-07 09:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reportapp', '0017_auto_20200207_0743'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='up',
            field=models.BooleanField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='profile',
            name='mobno',
            field=models.CharField(max_length=10),
        ),
    ]
