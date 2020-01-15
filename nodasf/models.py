from django.db import models
from django.db.models.aggregates import Count
from datetime import datetime

# Create your models here.

###########NodaSF##############
class County(models.Model):
    name = models.CharField(max_length=100, default='')
    image = models.ImageField(upload_to='media/stock', default='', blank=True) 
    description = models.TextField(default=' ')      
    slug = models.SlugField(max_length=100, default=' ')
    
    def __str__(self):
        return "{}/{}".format(self.name, self.id)   
    def get_district(self):
        return self.name
    
    class Meta:
        app_label = 'nodasf'        
        ordering = ('name',)

class Category(models.Model):
    name = models.CharField(max_length=100, default='')
    def __str__(self):
        return "{}/{}".format(self.name, self.id)
    class Meta:
        ordering = ('name',)        
        app_label = 'nodasf'
        
class Agency(models.Model):
    name = models.CharField(max_length=100, default='')
    picture = models.ImageField(upload_to='media/stock', default=" ")
    homepage = models.CharField(max_length=300, default='')
    description = models.TextField()
    category = models.ForeignKey(
        'Category',
        null=True,
        on_delete=models.PROTECT)
    issue = models.ForeignKey(
        'Issue',
        null=True,
        default=1,
        on_delete=models.PROTECT)   
    slug = models.SlugField(max_length=100, default=' ')
    
    def __str__(self):
        return self.name    
    class Meta:
        ordering = ('name',)
        app_label = 'nodasf'

class Genre(models.Model):
    name = models.CharField(max_length=100, default='')
    slug = models.SlugField(max_length=100, default=' ')

    def __str__(self):
        return "{}/{}".format(self.name, self.id)
    class Meta:
        app_label = 'nodasf'        

class Issue(models.Model):
    name = models.CharField(max_length=100, default='')
    imageQ = models.BooleanField(default=False)
    image = models.ImageField(upload_to='media/stock', default='', blank=True)
    slug = models.SlugField(max_length=100, default=' ')

    def __str__(self):
        return "{}/{}".format(self.name, self.id)    
    class Meta:
        ordering = ('name',)
        app_label = 'nodasf'        

class Organization(models.Model):
    name = models.CharField(max_length=100, default='')
    picture = models.ImageField(upload_to='media/stock', default=" ")
    homepage = models.CharField(max_length=300, default='')
    description = models.TextField()
    category = models.ForeignKey(
        'Category',
        null=True,    
        on_delete=models.PROTECT)
    issue = models.ForeignKey(
        'Issue',
        null=True,
        default=1,
        on_delete=models.PROTECT)    
    slug = models.SlugField(max_length=100, default=' ')
    
    def __str__(self):
        return self.name    
    class Meta:
        ordering = ('name',)
        app_label = 'nodasf'

class City(models.Model):
    name = models.CharField(max_length=100, default='')
    homepage = models.CharField(max_length=300, default=' ')    
    county = models.ForeignKey(
        'County',
        on_delete=models.PROTECT,)
    description = models.TextField(default=' ')    
    imageQ = models.BooleanField(default=False)
    image = models.ImageField(upload_to='media/stock', default='', blank=True)
    slug = models.SlugField(max_length=100, default=' ')

    def __str__(self):
        return self.name 
    def get_district(self):
        return self.name        
    class Meta:
        ordering = ('name',)        
        app_label = 'nodasf'
        
class Program(models.Model):
    name = models.CharField(max_length=200, default='name')
    homepage = models.CharField(max_length=300, default=' ')    
    organization = models.ForeignKey(
        'Organization',
        on_delete=models.PROTECT,)
    description = models.TextField(default=' ')    
    imageQ = models.BooleanField(default=False)
    image = models.ImageField(upload_to='media/stock', default='', blank=True) 
    category = models.ForeignKey(
        'Category',
        null=True,    
        on_delete=models.PROTECT)
    issue = models.ForeignKey(
        'Issue',
        null=True,
        default=1,
        on_delete=models.PROTECT)     
    def __str__(self):
        return self.name     
    class Meta:
        ordering = ('name',)  
        app_label = 'nodasf'
        
class Party(models.Model):
    name = models.CharField(max_length=100, default='')
    slug = models.SlugField(max_length=100, default=' ')

    def __str__(self):
        return self.name    

    class Meta:
        app_label = 'nodasf'        

class Level(models.Model):
    name = models.CharField(max_length=100, default='')
    slug = models.SlugField(max_length=100, default=' ')

    def __str__(self):
        return self.name    

    class Meta:
        app_label = 'nodasf'        
        
class District(models.Model):
    name = models.CharField(max_length=100, default='')
    description = models.TextField(default=' ')    
    county = models.ManyToManyField('County', related_name="counties")
    city = models.ManyToManyField('City', related_name="cities")
    image = models.ImageField(upload_to='media/stock', default='', blank=True)    
    level = models.ForeignKey(
        'Level',
        default=1,
        on_delete=models.PROTECT,)
    slug = models.SlugField(max_length=100, default=' ')    
  
    def __str__(self):
        return self.name   
    class Meta:
        ordering = ('name',)
        app_label = 'nodasf'        
        
class Venue(models.Model):
    name = models.CharField(max_length=100, default='')
    description = models.TextField(default=' ')
    homepage = models.CharField(max_length=300, default=' ')    
    city = models.ForeignKey(
        'City',
        null=True,        
        on_delete=models.SET_NULL,)     
    county = models.ForeignKey(
        'County',
        blank=True,
        null=True,
        on_delete=models.SET_NULL,)
    imageQ = models.BooleanField(default=False)
    image = models.ImageField(upload_to='media/stock', default='', blank=True)
    slug = models.SlugField(max_length=100, default=' ')

    def __str__(self):
        return self.name    
    class Meta:
        ordering = ('name',)
        app_label = 'nodasf'        
        
class SF_Event(models.Model):
    name = models.CharField(max_length=200)
    date = models.DateTimeField(default=datetime.now)
    city = models.ForeignKey(
        'City',
        null=True,        
        on_delete=models.SET_NULL,) 
    county = models.ForeignKey(
        'County',
        blank=True,
        null=True,        
        on_delete=models.SET_NULL,)
    free = models.BooleanField(default=False)
    cost = models.CharField(max_length=100, default='', blank=True)
    homepage = models.CharField(max_length=200, default='', blank=True)
    genre = models.ForeignKey(
        'Genre',
        null=True,        
        on_delete=models.SET_NULL,)
    description = models.TextField()
    venue = models.ForeignKey(
        'Venue',
        default=1,
        on_delete=models.CASCADE,)    
    imageQ = models.BooleanField(default=False)
    image = models.ImageField(upload_to='media/stock', default='', blank=True)
    slug = models.SlugField(max_length=100, default=' ')

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('-date',)
        app_label = 'nodasf'        

class Politician(models.Model):
    first_name = models.CharField(max_length=100, default='first')
    last_name = models.CharField(max_length=100, default='last')    
    party = models.ForeignKey(
        'Party',
        null=True,        
        on_delete=models.SET_NULL,)
    level = models.ForeignKey(
        'Level',
        null=True,        
        on_delete=models.SET_NULL,)
    county = models.ForeignKey(
        'County',
        blank=True,
        null=True,
        on_delete=models.SET_NULL,)
    district = models.ForeignKey(
        'District',
        null=True,
        on_delete=models.SET_NULL)        
    picture = models.ImageField(upload_to='media/faces', default=" ")
    homepage = models.CharField(max_length=300, default='')
    description = models.TextField()
    upcoming = models.ForeignKey(
        'SF_Event',
        null=True,
        on_delete=models.SET_NULL,
        blank=True)    
    candidate = models.BooleanField(default=False)        
    slug = models.SlugField(max_length=100, default=' ')

    def __str__(self):
        return self.last_name    

    class Meta:
        app_label = 'nodasf'
        
class Bureaucrat(models.Model):
    last_name = models.CharField(max_length=100, default='last')
    first_name = models.CharField(max_length=100, default='first')
    picture = models.ImageField(upload_to='media/faces', default=" ")
    description = models.TextField()
    organization = models.ForeignKey(
        'Organization',
        blank=True,
        null=True,
        on_delete=models.SET_NULL,)
    program = models.ManyToManyField(
        'Program',
        null=True,
        blank=True,)    
    def __str__(self):
        return self.last_name    
                
    class Meta:
        app_label = 'nodasf'
        
class Local_Link(models.Model):
    url = models.CharField(max_length=300, default='')
    headline = models.CharField(max_length=150, default='')
    posted = models.DateTimeField(auto_now_add=True, blank=True)
    county = models.ForeignKey(
        'County',
        blank=True,
        null=True,
        on_delete=models.PROTECT,)
    city = models.ForeignKey(
        'City',
       null=True,
        on_delete=models.PROTECT,
        blank=True)
    issue = models.ForeignKey(
        'Issue',
        on_delete=models.PROTECT,
       null=True,    
        blank=True,)        
    imageQ = models.BooleanField(default=False)
    image = models.ImageField(upload_to='media/stock', default='', blank=True)

    def __str__(self):
        return "{}/{}".format(self.headline, self.media)

    class Meta:
        ordering = ('-posted',)
        app_label = 'nodasf'        
