from django.db import models
from phone_field import PhoneField
from django.forms import ModelForm
from django.core import validators


def min_check(num):
    if len(num)<10 :
            raise validators.ValidationError("Content  must be of 10 character ")
    else:

        pass
        

class Contact(models.Model):    
    name=models.CharField(max_length=22)
    email=models.EmailField(max_length=100)
    mobile=PhoneField(max_length=19,blank=True, help_text='Contact phone number')
    issue=models.TextField(max_length=5000)
    def __str__(self):
        return self.name
    
    objects=models.Manager

class Post(models.Model):
   
    title=models.CharField(validators=[min_check],max_length=22)
    '''validators=[min_check]'''
    content=models.TextField(validators=[min_check])
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    objects=models.Manager
    def __str__(self):
        return self.title


class Category(models.Model):
   
    title=models.CharField(validators=[min_check],max_length=22)
    '''validators=[min_check]'''
    
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    objects=models.Manager
    def __str__(self):
        return self.title


class PostForm(ModelForm):
    class Meta:
        model=Post
        fields=['title','content']
    

    def clean(self):
        fields=self.cleaned_data
        print(fields)
        keys=list(fields.keys())
        if(len(fields[keys[0]])<10):
            raise validators.ValidationError(f"{keys[0]} must have at list 10 charchter")

        if(len(fields[keys[1]])<10):
            raise validators.ValidationError(f"{keys[1]} must have at list 10 charchter")
