from django import views
from django.contrib import admin
from django.urls import path
from sub_cypher.views import LogEntryListCreateView
from sub_cypher.views import LogEntryDetailView



urlpatterns = [
    path('log-entries/', views.LogEntryListCreateView.as_view(), name='log-entry-list'),
    path('log-entries/<int:pk>/', views.LogEntryDetailView.as_view(), name='log-entry-detail'),
    path('instantiate/', views.instantiate, name='instantiate'),
    path('encrypt/', views.encrypt, name='encrypt'),
    path('decrypt/', views.decrypt, name='decrypt'),
    path('history/', views.history, name='history'),
    path('menu/', views.menu, name='menu'),
]
