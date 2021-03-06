# Generated by Django 3.0.2 on 2020-02-04 10:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=50)),
                ('lastname', models.CharField(max_length=50)),
                ('fathername', models.CharField(max_length=50)),
                ('username', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=50)),
                ('varify_password', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=250)),
                ('profile_pic', models.ImageField(upload_to='Profileimage')),
            ],
        ),
    ]
