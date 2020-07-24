from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('start_game', views.game),
    path('war', views.war),
    path('add_soldier', views.add),
    path('battle', views.battle)
]