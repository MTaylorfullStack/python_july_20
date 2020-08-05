from django.shortcuts import render, HttpResponse, redirect
from .models import *

## methods for rendering HTML

def index(request):
    # render some HTML with hyperlinks to /movies or /directors
    return render(request, 'index.html')

def directors(request):
    # grab all directors from db
    context = {
        'all_directors': Director.objects.all()
    }
    # render page with add director form and table of all directors
    return render(request, 'directors.html', context)

def movies(request):
    # grab all movies from db
    context = {
        'all_movies': Movie.objects.all(),
        'all_directors' : Director.objects.all()
    }
    # render page with add movie form and table of all movie data
    return render(request, 'movies.html', context)

def actors(request):
    return HttpResponse("Placeholder for form to add actors and table displaying all actors")

## Methods for grabbing one instance from db and displaying it on HTML

def one_director(request, id):
    # retrieve this director from db
    context = {
        'director': Director.objects.get(id=id)
    }
    # render page with all director data
    return render(request, "one_director.html", context)

def one_movie(request, id):
    return HttpResponse(f"Placeholder to display movie with id {id}")

## Methods for db instance deletion

def delete_director(request, id):
    # retrieve director with corresponding id
    Director.objects.get(id=id).delete()
    # delete them
    return redirect('/directors')

def delete_movie(request, id):
    return HttpResponse(f"Placeholder route delete movie {id}")

## Methods for db instance edits

def edit_director(request, id):

    if request.method == 'POST':
        # retrieve director with corresponding id
        edit_director = Director.objects.get(id=id)
        edit_director.name = request.POST['name']
        edit_director.save()
        return redirect(f'/director/{id}')
        
    return HttpResponse(f"Placeholder to edit director {id}")

def edit_movie(request, id):
    return HttpResponse(f"Placeholder to edit movie {id}")

## Methods for creating DB data

def add_director(request):
    if request.method == 'POST':
        print(request.POST)
        Director.objects.create(name=request.POST['name'])
        return redirect('/directors')
    return redirect('/')

def add_movie(request):
    if request.method == 'POST':
        print(request.POST)
        Movie.objects.create(title=request.POST['title'], description=request.POST['description'], director=Director.objects.get(id=request.POST['director']))
        return redirect('/movies')
    return redirect('/')