from django.urls import path
from . import views

urlpatterns = [
    path('', views.root),
    path('register', views.register),
    path('success', views.success),
    path('login', views.login),
    path('create_mess', views.create_mess),
    path('profile/<int:user_id>', views.profile)
]