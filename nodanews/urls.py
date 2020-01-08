from django.conf.urls import url, include
from django.urls import include, path, re_path

from . import views

urlpatterns = [
	path('', views.index, name='index'),
	
###############Archive##########	

	path('about/', views.about, name='about'),
	path('archives/', views.archives, name='archives'),	
	path('node-dir/$', views.node_dir, name='node_dir_index'),
	path('node-dir/<int:id>/<slug:slug>/', views.node_dir_part, name='node_dir'),
	path('media-org-directory/', views.media_dir_athena, name='media_dir_test'),	
	path('node/<int:id>', views.node, name='node'),
	path('node/<int:id>/<slug:slug>/', views.nodeslug, name='nodes with slugs'),
	path('story/<int:id>/<slug:slug>/', views.stf, name='stories to follow'),
	path('hub/<int:id>/<slug:slug>/', views.stf_hub, name='hubs for stfs limited)'),
	path('hubx/<int:id>/<slug:slug>/', views.stf_hubx, name='hubs for stfs unlimited'),	
	path('media_dir/<int:id>/<slug:slug>/', views.media_org, name='media_org'),
	path('blog/<int:id>/<slug:slug>/', views.blog, name='blog'),
	path('in-depth/<int:id>/<slug:slug>/', views.analysis, name='in-depth'),
	path('journalist/<int:id>/<slug:slug>/', views.journalist, name='journalist'),
	path('issue/<int:id>/<slug:slug>/', views.political_issue, name='political issue'),	
	]