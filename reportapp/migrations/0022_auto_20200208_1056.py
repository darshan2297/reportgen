# Generated by Django 3.0.2 on 2020-02-08 10:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('reportapp', '0021_subtopic_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='subtopic',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='reportapp.profile'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='topic',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='reportapp.profile'),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='record',
        ),
    ]
