from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('project_detail/<int:pid>', views.project_detail, name='project_detail'),
     path('contact/', views.contact, name='contact'),

]
