from cProfile import Profile
from distutils.command.upload import upload
from email.policy import default
from operator import mod
from re import T
from tkinter import CASCADE
from django.db import models
from django.contrib.auth.models import User
import uuid
from django.db.models.signals import post_save,post_delete
from django.dispatch import receiver


# Create your models here.
class profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,null=True,blank=True)
    name=models.CharField(max_length=200,null=True,blank=True)
    username=models.CharField(max_length=200,null=True,blank=True)
    email=models.CharField(max_length=500,null=True,blank=True)
    age=models.IntegerField(max_length=2,null=True,blank=True)
    qualify1=models.CharField(max_length=500,null=True,blank=True)
    qualify2=models.CharField(max_length=500,null=True,blank=True)
    profile_image=models.ImageField(null=True,blank=True,upload_to='profiles/',default='profiles/user-default.png')
    short_intro=models.CharField(max_length=200,blank=True,null=True)
    lang=models.CharField(max_length=200,null=True,blank=True)
    exp=models.IntegerField(max_length=2,null=True,blank=True)
    noofsession=models.IntegerField(max_length=2,null=True,blank=True)
    hours=models.IntegerField(max_length=2,null=True,blank=True)
    noofstudents=models.IntegerField(max_length=2,null=True,blank=True)
    phone=models.IntegerField(max_length=10,null=True,blank=True)
    education=models.TextField(null=True,blank=True)
    topicsinc1=models.TextField(null=True,blank=True)
    topicsinc2=models.TextField(null=True,blank=True)
    class1=models.TextField(null=True,blank=True)
    class2=models.TextField(null=True,blank=True)
    bio=models.TextField(null=True,blank=True)
    location=models.CharField(max_length=200,null=True,blank=True)
    
    created=models.DateTimeField(auto_now_add=True)
    id=models.UUIDField(default=uuid.uuid4,unique=True,primary_key=True,editable=False)

    def __str__(self):
        return str(self.username)



class Messages(models.Model):
    #on delete the account the reciver will able to see the message and it should not be deleted
    sender=models.ForeignKey(profile,on_delete=models.SET_NULL,null=True,blank=True)
    #null = true means user dont have account can send message 
    recipient=models.ForeignKey(profile,on_delete=models.SET_NULL,null=True,blank=True,related_name="messagess")
    name=models.CharField(max_length=200,null=True,blank=True)
    email=models.CharField(max_length=500,null=True,blank=True)
    subject=models.CharField(max_length=200,null=True,blank=True)
    body=models.TextField()
    is_read=models.BooleanField(default=False,null=True)
    created=models.DateTimeField(auto_now_add=True)
    id=models.UUIDField(default=uuid.uuid4,unique=True,primary_key=True,editable=False)

    def __str__(self):
        return str(self.subject)
    
    #when user open inbox it should order based on
    class Meta:
        ordering=['is_read','-created']
    





