from django.db import models
#from tinymce.models import HTMLField
from django.db.models.aggregates import Count
from datetime import datetime

class Theme(models.Model):
    name: models.CharField(max_length=100, default=' ')
    
    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ('name',)


class Event(models.Model):
    headline = models.CharField(max_length=150, default=' ')
    lead = models.TextField()
    date_created = models.DateField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    body = models.TextField()
    image = models.ImageField(upload_to='media/stock', default='')
    credit = models.CharField(max_length=200, default='') 
    videoQ = models.BooleanField(default=False)
    video = models.CharField(max_length=500, default='', blank=True)     
    theme = models.ForeignKey(
        'Theme',
        on_delete=models.CASCADE)
    slug = models.SlugField(max_length=100, default=' ')
    
    def __str__(self):
        return self.headline
    class Meta:
        ordering = ('-date_created',)

class Media_Org(models.Model):
    name = models.CharField(max_length=100, default='')
    date_posted = models.DateTimeField(auto_now_add=True)
    home_page = models.CharField(max_length=200, default='')
    country = models.CharField(max_length=100, default='')
#   region = models.ForeignKey('Region',
#   default=1,
#    null=True,
#    on_delete=models.CASCADE,)
    date_founded = models.DateField(default='1956-02-27')
    logo = models.ImageField(upload_to='media/logos')
    description = models.TextField()
    ready = models.BooleanField(default=False)
#    political_lean = models.ForeignKey(
#        'Political_Lean',
#        default=1,
#        null=True,
#        on_delete=models.PROTECT,)
#    media_character = models.ForeignKey(
#        'Media_Character',
#        default=1,
#        null=True,
#        on_delete=models.PROTECT,)
    slug = models.SlugField(max_length=100, default=' ')

    
    def __str__(self):
        return self.name
    class Meta:
        ordering = ('name',)
        
class Report_Link(models.Model):
    url = models.CharField(max_length=300, default='', blank=True)
    title = models.CharField(max_length=150, default='', blank=True)
    posted = models.DateTimeField(auto_now=True, blank=True)    
    media = models.ForeignKey(
        'Media_Org',
        on_delete=models.CASCADE,)
    event = models.ForeignKey(
        'Event',
        on_delete=models.CASCADE,
        default=1)
    imageQ = models.BooleanField(default=False)
    image = models.ImageField(upload_to='media/temp', default='', blank=True)        

    def __str__(self):
        return "{}/{}".format(self.title, self.event)  
        
    class Meta:
        ordering = ('-posted',)

class Blog(models.Model):
    headline = models.CharField(max_length=200, default='')
    date_posted = models.DateField(auto_now_add=True)
    text = models.TextField()
    slug = models.SlugField(max_length=200, default=' ') 
    event = models.ForeignKey(
        'Event',
        on_delete=models.CASCADE,
        default=1)    
    def __str__(self):
        return "{}".format(self.headline)
    class Meta:
        ordering = ('-date_posted',)