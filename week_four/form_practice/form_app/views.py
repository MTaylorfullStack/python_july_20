from django.shortcuts import render, redirect
import random

def index(request):
    return render(request, 'form.html')

def success(request):
    if "gold" not in request.session:
        request.session['gold'] = 0
    return render(request, "result.html")

def process(request):
    print(request.POST['user_name'])
    request.session['name'] = request.POST['user_name']
    request.session['loc'] = request.POST['location']
    request.session['lang'] = request.POST['fav_lang']
    request.session['comment'] = request.POST['comment']
    return redirect('/success')

def process_gold(request):
    print(request.POST)
    # add to some gold variable that we can view on the templates
    # need to know how much gold to add, which form was submitted
    if "farm" in request.POST:
        gold = int(random.random() * 10 + 10)
        request.session['gold'] += gold
    if "cave" in request.POST:
        gold =  int(random.random() * 5 + 5)
        request.session['gold'] += gold
    if "house" in request.POST:
        gold = int(random.random() * 3 + 2)
        request.session['gold'] += gold
    if "casino" in request.POST:
        gold = int(random.random() * 50)
        if int(random.random()*10) > 5:
            # gain
            request.session['gold'] += gold
        else:
            # lose
            request.session['gold'] -= gold
    return redirect('/success')

def reset(request):
    request.session.flush()
    return redirect('/')


