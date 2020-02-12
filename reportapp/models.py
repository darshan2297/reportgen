from django.db import models
from django.contrib.auth.models import User
from datetime import datetime,date
from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.

class profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    fathername = models.CharField(max_length=50)
    email = models.EmailField(max_length=250,unique=True)
    profile_pic = models.ImageField(upload_to='Profileimage')
    collage_name = models.CharField(max_length = 200)
    address = models.CharField(max_length= 200)
    mobno = models.CharField(max_length=10)
    pid = models.CharField(max_length = 10)
    project_title = models.CharField(max_length = 200,blank = True)
    company_name = models.CharField(max_length=200)
    up = models.BooleanField() 
    def __str__(self):
        return self.user.username

class topic1(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    topic = models.CharField(max_length = 100)
    date = models.DateField(default=date.today,blank=True)
    
    def __str__(self):
        return self.topic

class subtopic1(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    date = models.DateField(default=date.today,blank=True)
    topic = models.ForeignKey(topic1,on_delete=models.CASCADE)
    subtopic = models.CharField(max_length=1000)
    
    def __str__(self):
        return self.subtopic
