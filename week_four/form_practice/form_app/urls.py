from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('process', views.process),
    path('success', views.success),
    path('process_money', views.process_gold),
    path('reset', views.reset)
]