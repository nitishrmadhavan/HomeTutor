from csv import field_size_limit
from dataclasses import field, fields
from django.forms import ModelForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import profile,Messages

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model=User
        fields=['first_name','email','username','password1','password2']
        labels={
            'first_name':'Name'
        }

    def __init__(self,*args,**kwargs):
        super(CustomUserCreationForm,self).__init__(*args,**kwargs)
        
        for name,field in self.fields.items():
            field.widget.attrs.update({'class':'input'})

class ProfileForm(ModelForm):
    class Meta:
        model=profile
        fields=['name','username','email','age','qualify1','qualify2','profile_image','short_intro','lang','exp','noofsession','hours',
        'noofstudents','phone','education','topicsinc1','topicsinc2','class1','class2','bio','location',]

        labels={'name':'Name','username':'Username','email':'Email ID','age':'Age','qualify1':'Qualification Degree 1','qualify2':'Qualification Degree 2',
        'profile_image':'Profile Image','short_intro':'Introduction','lang':'Languages Known','exp':'Experiance','noofsession':'Number of Sessions',
        'hours':'Hours','noofstudents':'Number of Students','phone':'Phone Number','education':'Education Details','topicsinc1':'Specialized Topic 1',
        'topicsinc2':'Specialized Topic 2','class1':'Prefered Standard 1','class2':'Prefered Standard 2','bio':'Bio','location':'Location',}

        
    def __init__(self,*args,**kwargs):
        super(ProfileForm,self).__init__(*args,**kwargs)
        
        
        for name,field in self.fields.items():
            field.widget.attrs.update({'class':'input'})



class MessageForm(ModelForm):
    class Meta:
        model = Messages
        fields = ['name', 'email', 'subject', 'body']

    def __init__(self, *args, **kwargs):
        super(MessageForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'input'})