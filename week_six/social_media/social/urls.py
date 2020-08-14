from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('register', views.register),
    path('login', views.login),
    path('success', views.success),
    path('logout', views.logout),
    ## wall paths
    path('create_message', views.add_message),
    path('profile/<int:id>', views.profile),
    path('edit/<int:id>', views.edit_mess),
    path('delete/<int:id>', views.delete_mess),
    path('add_comment/<int:id>', views.add_comm),
    path('like/<int:id>', views.add_like),
]