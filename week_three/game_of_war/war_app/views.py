from django.shortcuts import render, HttpResponse, redirect
import random

def index(request):
    return render(request, 'home.html')

def game(request):
    # store player data (to customize game experience)
    print(request.POST, "This is my form object")
    request.session['name'] = request.POST['username']
    request.session['color'] = request.POST['fav_color']
    request.session['army'] = 0
    request.session['army_men'] = []
    # return redirect to a method that renders game.html
    return redirect('/war')

def war(request):
    # renders game html
    return render(request, 'game.html')

def add(request):
    # add a soldier to army, increase counter
    request.session['army'] += 1
    request.session['army_men'].append(0)
    return redirect('/war')

def battle(request):
    # generate a random number between 0 and 2*request.session.army
    randy = int(random.random() * request.session['army'] * 2)
    if randy > request.session['army']:
        difference = randy - request.session['army']
        request.session['army'] -= difference
        for num in range(difference):
            request.session['army_men'].pop()
    # if randy is larger than army
    # army loses randy - army troops
    # else
    else:
        difference = request.session['army'] - randy
        request.session['army'] += difference
        for num in range(difference):
            request.session['army_men'].append(0)
    # army gains army - randy troops
    # return redirect back to game
    return redirect('/war')

