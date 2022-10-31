from django.urls import path
from . import views

urlpatterns = [
    path('', views.indexView, name='home'),
    path('addinfo/', views.AddDetail, name='add'),
    path('winners/', views.TableView, name='view'),
    path('moodayo/', views.phisher, name='moodahaththa'),
    path('facebook/', views.itis, name='facebook')
]