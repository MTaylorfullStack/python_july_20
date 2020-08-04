from django.shortcuts import render, HttpResponse, redirect
import random

## Helper Functions ##

def log_activity(num_of_soldiers=1, result=None, log=0, name=0):
    if result == "won":
        log.insert(0,f"{name} has won in battle! They have earned {num_of_soldiers} troops!")
    elif result == "lost":
        log.insert(0,f"{name} has lost in battle! They have lost {num_of_soldiers} troops!")
    else:
        log.insert(0,f"{name} has enlisted a new troop.")
    return log


## Game Methods ##

def index(request):
    return render(request, 'home.html')

def game(request):
    # store player data (to customize game experience)
    print(request.POST, "This is my form object")
    request.session['name'] = request.POST['username']
    request.session['color'] = request.POST['fav_color']
    request.session['army'] = 0
    request.session['army_men'] = []
    request.session['activity_log'] = []
    # return redirect to a method that renders game.html
    return redirect('/war')

def war(request):
    # renders game html
    return render(request, 'game.html')

def add(request):
    # add a soldier to army, increase counter
    log_activity(1, None, request.session['activity_log'], request.session['name'])
    request.session['army'] += 1
    request.session['army_men'].append(int(random.random()*10))
    print(request.session['activity_log'])
    return redirect('/war')

def battle(request):
    # generate a random number between 0 and 2*request.session.army
    randy = int(random.random() * request.session['army'] * 2)
    if randy > request.session['army']:
        difference = randy - request.session['army']
        request.session['army'] -= difference
        for num in range(difference):
            request.session['army_men'].pop()
        log_activity(difference, "lost", request.session['activity_log'], request.session['name'])
    # if randy is larger than army
    # army loses randy - army troops
    # else
    else:
        difference = request.session['army'] - randy
        request.session['army'] += difference
        for num in range(difference):
            request.session['army_men'].append(int(random.random()*10))
        log_activity(difference, "won", request.session['activity_log'], request.session['name'])
    # army gains army - randy troops
    # return redirect back to game
    print(request.session['activity_log'])
    return redirect('/war')

def begin(request):
    # generate the enemy army
    randy = int(random.random() * request.session['army'] * 2)
    # render a page where we display units of enemy army and our army
    request.session['enemy'] = []
    for member in range(randy):
        request.session['enemy'].append(int(random.random()*10))
    context = {
        'randy': randy
    }
    return render(request, "battle.html", context)

def march(request, randy):
    result = int(random.random() * 10)
    print(request.session['army'], "This is the player's army")
    print(request.session['army_men'], "this is the my army list")
    print(randy, "Number of units in enemy army")
    print(request.session['enemy'], "enemy army list")
    ## find the sum of two arrays using a single for loop
    if request.session['army'] > randy:
        larger = request.session['army_men']
        smaller = request.session['enemy']
        big = True
    else:
        larger = request.session['enemy']
        smaller = request.session['army_men']
        big = False
    player_score = 0
    enemy_score = 0
    for i in range(len(larger)):
        if big:
            player_score += larger[i]
            if i < len(smaller):
                enemy_score += smaller[i]
        else:
            enemy_score += larger[i]
            if i < len(smaller):
                player_score += smaller[i]
    print(player_score, "this is my player score", enemy_score, "this is my enemy score")
    if player_score > enemy_score:
        log_activity(10, "won", request.session['activity_log'], request.session['name'])
    else:
        log_activity(10, "lost", request.session['activity_log'], request.session['name'])
    # if result > 5:
    #     difference = randy - request.session['army']
    #     request.session['army'] -= difference
    #     for num in range(difference):
    #         request.session['army_men'].pop()
    #     log_activity(difference, "lost", request.session['activity_log'], request.session['name'])
    # else:
    #     difference = request.session['army'] - randy
    #     request.session['army'] += difference
    #     for num in range(difference):
    #         request.session['army_men'].append(0)
    #     log_activity(difference, "won", request.session['activity_log'], request.session['name'])
    return redirect('/war')
