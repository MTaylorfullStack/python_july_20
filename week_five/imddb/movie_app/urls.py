from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('directors', views.directors),
    path('movies', views.movies),
    path('director/<int:id>', views.one_director),
    path('movie/<int:id>', views.one_movie),
    path('director/delete/<int:id>', views.delete_director),
    path('movie/delete/<int:id>', views.delete_movie),
    path('director/edit/<int:id>', views.edit_director),
    path('movie/edit/<int:id>', views.edit_movie),
    path('actors', views.actors)
]
