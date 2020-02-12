from django.conf.urls import url, include
from django.urls import include, path, re_path

from . import views

#NodaSF
urlpatterns = [
	path('', views.index, name='index'),
	path('test/', views.indexUC, name='index in training')
]