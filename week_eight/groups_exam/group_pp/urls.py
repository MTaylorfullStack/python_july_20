from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('main', views.main),
    # registration paths
    path('register', views.register),
    path('login', views.login),
    path('logout', views.logout),
    # groups paths
    path('groups', views.groups),
    path('create_org', views.create_org),
    path('groups/<int:id>', views.one_group),
    path('join/<int:id>', views.join_org),
    path('leave/<int:id>', views.leave_org),
    path('delete/<int:id>', views.delete_org)
]