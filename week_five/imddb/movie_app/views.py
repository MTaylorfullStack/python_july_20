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
    # grab an instance a movie
    context = {
        'one_movie': Movie.objects.get(id=id),
        'all_actors': Actor.objects.all()
    }
    # display this movie on some one_movie.html
    return render(request, "one_movie.html", context)

## Methods for db instance deletion

def delete_director(request, id):
    # retrieve director with corresponding id
    Director.objects.get(id=id).delete()
    # delete them
    return redirect('/directors')

def delete_movie(request, id):
    Movie.objects.get(id=id).delete()
    return redirect('/movies')

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
    # retrieve this movie
    edit_movie = Movie.objects.get(id=id)
    # edit this movies data
    edit_movie.title = request.POST['title']
    # save our edit
    edit_movie.save()
    # redirect to some page where we can view updated data
    return redirect(f'/movie/{id}')

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

def add_actor(request):
    if request.method == 'POST':
        Actor.objects.create(name=request.POST['name'])
        return redirect('/')
    return redirect('/')

## Many-To-Many

def add_actor_to_movie(request, id):
    movie = Movie.objects.get(id=id)
    actor = Actor.objects.get(id=request.POST['actor'])
    actor.movies.add(movie)
    return redirect('/movies')