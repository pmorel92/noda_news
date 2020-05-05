from django.conf.urls import url, include
from django.urls import include, path, re_path

from . import views

urlpatterns = [
	path('', views.index, name='index'),
	path('test/', views.indexUC, name='work in progress'),
	path('event/<int:event_id>/<slug:slug>/', views.event, name="event view"),

###############Archive##########	

	path('about/', views.about, name='about'),
	path('archives/', views.archives, name='archives'),	
	path('node-dir/', views.node_dir, name='node_dir_index'),
	path('node-dir/<int:id>/<slug:slug>/', views.node_dir_part, name='node_dir'),
	path('media-org-directory/', views.media_dir_athena, name='media_dir_test'),	
	path('node/<int:node_id>', views.node, name='node'),
	path('node/<int:node_id>/<slug:slug>/', views.nodeslug, name='nodes with slugs'),
	path('story/<int:stf_id>/<slug:slug>/', views.stf, name='stories to follow'),
	path('hub/<int:stf_hub_id>/<slug:slug>/', views.stf_hub, name='hubs for stfs limited)'),
	path('hubx/<int:stf_hub_id>/<slug:slug>/', views.stf_hubx, name='hubs for stfs unlimited'),	
	path('media_dir/<int:media_org_id>/<slug:slug>/', views.media_org, name='media_org'),
	path('blog/<int:blog_id>/<slug:slug>/', views.blog, name='blog'),
	path('in-depth/<int:id>/<slug:slug>/', views.analysis, name='in-depth'),
	path('journalist/<int:journalist_id>/<slug:slug>/', views.journalist, name='journalist'),
	path('issue/<int:issue_id>/<slug:slug>/', views.political_issue, name='political issue'),	
	]