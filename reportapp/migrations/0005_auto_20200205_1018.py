# Generated by Django 3.0.2 on 2020-02-05 10:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reportapp', '0004_remove_profile_verify_password'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='username',
            new_name='uname',
        ),
    ]
