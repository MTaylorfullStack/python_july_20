from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages


# Home route
def index(request):
    return render(request, 'index.html')

# Success route
def success(request):
    return render(request, 'success.html')

## USER routes ##

# User registration (create)
def register(request):
    # is this a post request?
    if request.method == 'POST':
        # if it is, let's validate our data
        errors = User.objects.validator(request.POST)
        print(errors)
        # if there were errors
        if len(errors) > 0:
            # compile those errors into the messages object
            for key, values in errors.items():
                messages.error(request, values)
            # redirect home, where user can correct errors
            return redirect('/')
        # no errors, good to CREATE
        new_user = User.objects.create(first_name=request.POST['f_name'], last_name=request.POST['l_name'], email=request.POST['email'], password=request.POST['password'])
        request.session['name'] = new_user.first_name
        # redirect to success route
        return redirect('/success')
    # if this wasn't a post request, redirect to home page
    return redirect('/')


# User login (filtering for users)
def login(request):
    # is this a post request?
    if request.method == 'POST':
        # let's use the post data to filter for users
        logged_user = User.objects.filter(email=request.POST['email'])
        # did we find a user?
        if len(logged_user) > 0:
            # storing User Object instead of Queryset containing user
            logged_user = logged_user[0]
            # does their submitted password match our password in the DB?
            if logged_user.password == request.POST['password']:
                # storing user data in session
                request.session['name'] = logged_user.first_name
                # routing to success page
                return redirect('/success')
    # this wasn't a post request, let's redirect home
    return redirect('/')
