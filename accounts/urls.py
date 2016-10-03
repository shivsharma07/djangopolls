'''
Created on Nov 2, 2015

@author: Shiv Sharma
'''

from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^login/$', views.login, name='login'),
    #url(r'^process_login/$', views.process_login, name='process_login'),
    url(r'^loggedin/$', views.loggedin, name='loggedin'),
    url(r'^login_error/$', views.login_error, name='login_error'),
    url(r'^logout/$', views.logout, name='logout'),
    url(r'^restricted/$', views.restricted, name='restricted'),
]
    