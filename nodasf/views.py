from django.shortcuts import get_object_or_404, render, redirect
from django.template.loader import get_template
from django.template import Context
from django.template.defaulttags import register
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.urls import reverse
from django.db.models import F, Q
from .models import Venue, Agency, Genre, Issue, Party, Level, Event, Politician, Local_Link, District, Category, Organization, Program, Bureaucrat, Story, Blog, Report_Link, Media_Org

def index(request):
	return render (request, 'sf-index.html')

def indexUC(request):
    
    return render (request, 'sf-indexUC.html')