from django.shortcuts import render, HttpResponse, redirect

## methods for rendering HTML

def index(request):
    return HttpResponse("Placeholder for links to movies or directors")

def directors(request):
    return HttpResponse("Placeholder for form to add directors and table displying directors")

def movies(request):
    return HttpResponse("Placeholder for form to add movies and table displying movies")

def actors(request):
    return HttpResponse(f"Placeholder for form to add actors and table displaying all actors")

## Methods for grabbing one instance from db and displaying it on HTML

def one_director(request, id):
    return HttpResponse(f"Placeholder to display director data with id {id}")

def one_movie(request, id):
    return HttpResponse(f"Placeholder to display movie with id {id}")

## Methods for db instance deletion

def delete_director(request, id):
    return HttpResponse(f"Placeholder route to delete director {id}")

def delete_movie(request, id):
    return HttpResponse(f"Placeholder route delete movie {id}")

## Methods for db instance edits

def edit_director(request, id):
    return HttpResponse(f"Placeholder to edit director {id}")

def edit_movie(request, id):
    return HttpResponse(f"Placeholder to edit movie {id}")