from django.conf.urls import url, include
from django.urls import include, path, re_path

from . import views

urlpatterns = [
	path('', views.index, name='index'),
	]