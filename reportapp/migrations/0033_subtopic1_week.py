# Generated by Django 3.0.2 on 2020-02-11 10:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reportapp', '0032_auto_20200211_0752'),
    ]

    operations = [
        migrations.AddField(
            model_name='subtopic1',
            name='week',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
