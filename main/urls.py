# urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('api/v1/vote/', views.vote, name='vote'),
    path('candidates/', views.candidates, name='candidates'),
    path('', views.home, name='home')
]
