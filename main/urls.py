# urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('api/v1/vote/', views.vote, name='vote'),
    path('candidates/', views.candidates, name='candidates'),
    path('add-voter/', views.add_voter, name='add_voter'),
    path('', views.home, name='home')
]
