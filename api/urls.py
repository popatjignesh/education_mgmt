from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from api import views
from rest_framework.authtoken import views as tokenView


urlpatterns = patterns('',
	url(r'^register/', views.register, name='register'),
	url(r'^login/', tokenView.obtain_auth_token),
	url(r'^university/list/', views.university_list, name='university-list'),
	url(r'^school/add/', views.school_add, name='school-add'),
	url(r'^school/list/', views.school_list, name='school-list'),
	url(r'^school/detail/(?P<pk>[0-9]+)/', views.school_detail, name='school-detail'),
	url(r'^school/update/(?P<pk>[0-9]+)/', views.school_update, name='school-update'),
	url(r'^school/delete/(?P<pk>[0-9]+)/', views.school_delete, name='school-delete'),
	url(r'^university/list1/', views.university_list1, name='university-list1'),
	url(r'^student/add/', views.student_add, name='student-add'),
	url(r'^university/delete/(?P<pk>[0-9]+)/', views.university_delete, name='university-delete'),
)

