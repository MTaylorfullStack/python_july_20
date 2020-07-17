from django.urls import path
from . import views

urlpatterns = [
    path('', views.first_method),
    path('new_page', views.new_page)
]