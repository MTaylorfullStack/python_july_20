from django.shortcuts import render, redirect
import random

def index(request):
    if "gold" not in request.session:
        request.session['gold'] = 0
    return render(request, "index.html")

def process(request):
    print(request.POST)
    if 'house' in request.POST:
        request.session['gold'] += int(random.random() * 2 + 7)
    if 'casino' in request.POST:
        if int(random.random() * 10) > 5:
            request.session['gold'] += int(random.random()*50)
        else:
            request.session['gold'] -= int(random.random()*50)
    if 'farm' in request.POST:
        request.session['gold'] += int(random.random() * 5 + 15)
    if 'cave' in request.POST:
        request.session['gold'] += int(random.random()* 10 + 30)
    print(request.session['gold'])
    return redirect('/')