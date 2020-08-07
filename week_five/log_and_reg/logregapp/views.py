from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from .models import *

def index(request):
    return render(request, "log.html")

def success(request):
    if 'name' not in request.session:
        return redirect('/')
    return render(request, "success.html")

def register(request):
    if request.method == 'POST':
        errors = User.objects.validator(request.POST)
        print(errors)
        if len(errors) > 0:
            for key, values in errors.items():
                messages.error(request, values)
            return redirect('/')
        new_user = User.objects.create(first_name=request.POST['first_name'], last_name=request.POST['last_name'], email=request.POST['email'], password=request.POST['password'])
        request.session['name'] = new_user.first_name
        return redirect('/success')
    return redirect('/')

def login(request):
    print("Is my method being called")
    if request.method == 'POST':
        print("is it a post request?")
        logged_user = User.objects.filter(email=request.POST['email'])
        print(logged_user)
        print(User.objects.all())
        if len(logged_user) > 0:
            logged_user = logged_user[0]
            print(logged_user)
            print(logged_user.password, request.POST['password'])
            if logged_user.password == request.POST['password']:
                request.session['name'] = logged_user.first_name
                return redirect('/success')
    return redirect('/')

def logout(request):
    request.session.flush()
    return redirect('/')