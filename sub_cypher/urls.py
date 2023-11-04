from django import views
from django.contrib import admin
from django.urls import path, include
from sub_cypher.views import LogEntryListCreateView
from sub_cypher.views import LogEntryDetailView
from sub_cypher.views import *
from . import views



urlpatterns = [
    path('LogEntry', views.LogEntry, name='home'),
    path('log-entries/', views.LogEntryListCreateView, name='log-entry-create'),
    path('log-entries/list/', views.LogEntryDetailView.as_view(), name='log-entry-list'),
]

#     path('instantiate/', views.instantiate, name='instantiate'),
#     path('encrypt/', views.encrypt, name='encrypt'),
#     path('decrypt/', views.decrypt, name='decrypt'),
#     path('history/', views.history, name='history'),
#     path('menu/', views.menu, name='menu'),

