from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('process', views.process),
    path('view_user', views.view_user),
    path('reset', views.reset),
    path('start_game', views.start_game)
]