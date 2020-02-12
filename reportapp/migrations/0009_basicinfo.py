# Generated by Django 3.0.2 on 2020-02-06 13:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('reportapp', '0008_remove_profile_password'),
    ]

    operations = [
        migrations.CreateModel(
            name='basicinfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('collagename', models.CharField(max_length=200)),
                ('address', models.CharField(max_length=500)),
                ('mobno', models.IntegerField()),
                ('reportno', models.IntegerField()),
                ('pid', models.IntegerField()),
                ('projecttitle', models.CharField(blank=True, max_length=200)),
                ('compname', models.CharField(max_length=200)),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reportapp.profile')),
            ],
        ),
    ]
