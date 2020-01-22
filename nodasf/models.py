from django.db import models
from django.db.models.aggregates import Count
from datetime import datetime

class Author(models.Model):
    name = models.CharField(max_length=100, default='name here')
    image = models.ImageField(upload_to='media/stock', default='')    
    def __str__(self):
        return self.name
    class Meta:
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
    imageQ = models.BooleanField(default=False)
    image = models.ImageField(upload_to='media/stock', default='', blank=True)
    slug = models.SlugField(max_length=100, default=' ')

    def __str__(self):
        return self.name    
    class Meta:
        ordering = ('name',)
        app_label = 'nodasf'        
        
class Event(models.Model):
    name = models.CharField(max_length=200)
    date = models.DateTimeField(default=datetime.now)
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
    district = models.ForeignKey(
        'District',
        null=True,
        on_delete=models.SET_NULL)        
    picture = models.ImageField(upload_to='media/faces', default=" ")
    homepage = models.CharField(max_length=300, default='')
    description = models.TextField()
    upcoming = models.ForeignKey(
        'Event',
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
        blank=True,)    
    def __str__(self):
        return self.last_name    
                
    class Meta:
        app_label = 'nodasf'
        
class Local_Link(models.Model):
    url = models.CharField(max_length=300, default='')
    headline = models.CharField(max_length=150, default='')
    posted = models.DateTimeField(auto_now_add=True, blank=True)
    issue = models.ForeignKey(
        'Issue',
        on_delete=models.CASCADE,
       null=True,    
        blank=True,)        
    imageQ = models.BooleanField(default=False)
    image = models.ImageField(upload_to='media/stock', default='', blank=True)

    def __str__(self):
        return "{}/{}".format(self.headline, self.media)

    class Meta:
        ordering = ('-posted',)
        app_label = 'nodasf'        

class Story(models.Model):
    headline = models.CharField(max_length=150, default=' ')
    lead = models.TextField()
    date_created = models.DateField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    body = models.TextField()
    image = models.ImageField(upload_to='media/stock', default='')
    credit = models.CharField(max_length=200, default='') 
    videoQ = models.BooleanField(default=False)
    video = models.CharField(max_length=500, default='', blank=True)     
    issue = models.ManyToManyField('Issue',)
    politician = models.ManyToManyField(
        'Politician',
        blank=True,)
    bureaucrat = models.ManyToManyField(
        'Bureaucrat',
        blank=True,)
    program = models.ManyToManyField(
        'Program',
        blank=True)
    author = models.ForeignKey(
        'Author',
        on_delete=models.CASCADE,
        default=1,
        )    
    slug = models.SlugField(max_length=100, default=' ')
    
    def __str__(self):
        return self.headline
    class Meta:
        ordering = ('-date_created',)
        app_label = 'nodasf'

class Media_Org(models.Model):
    name = models.CharField(max_length=100, default='')
    date_posted = models.DateTimeField(auto_now_add=True)
    home_page = models.CharField(max_length=200, default='')
    country = models.CharField(max_length=100, default='')
    date_founded = models.DateField(default='1956-02-27')
    logo = models.ImageField(upload_to='media/logos')
    description = models.TextField()
    ready = models.BooleanField(default=False)
    slug = models.SlugField(max_length=100, default=' ')

    
    def __str__(self):
        return self.name
    class Meta:
        ordering = ('name',)
        app_label = 'nodasf'
        
class Report_Link(models.Model):
    url = models.CharField(max_length=300, default='', blank=True)
    title = models.CharField(max_length=150, default='', blank=True)
    posted = models.DateTimeField(auto_now=True, blank=True)    
    media = models.ForeignKey(
        'Media_Org',
        on_delete=models.CASCADE,
        blank=True)
    story = models.ForeignKey(
        'Story',
        on_delete=models.CASCADE,)
    imageQ = models.BooleanField(default=False)
    image = models.ImageField(upload_to='media/temp', default='', blank=True)        

    def __str__(self):
        return "{}/{}".format(self.title, self.event)  
        
    class Meta:
        ordering = ('-posted',)
        app_label = 'nodasf'        

class Blog(models.Model):
    headline = models.CharField(max_length=200, default='')
    date_posted = models.DateField(auto_now_add=True)
    text = models.TextField()
    slug = models.SlugField(max_length=200, default=' ') 
    story = models.ForeignKey(
        'Story',
        on_delete=models.CASCADE,
        blank=True,
        null=True,)    
    def __str__(self):
        return "{}".format(self.headline)
    class Meta:
        ordering = ('-date_posted',)
        app_label = 'nodasf'