from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages
import bcrypt


# Home route
def index(request):
    return render(request, 'index.html')

# Success route
def success(request):
    context = {
        'all_messages': Wall_Message.objects.all()
    }
    return render(request, 'success.html', context)

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
        pw_hash = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt()).decode()
        new_user = User.objects.create(first_name=request.POST['f_name'], last_name=request.POST['l_name'], email=request.POST['email'], password=pw_hash)
        print(new_user.password)
        request.session['name'] = new_user.first_name
        request.session['user_id'] = new_user.id
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
            if bcrypt.checkpw(request.POST['password'].encode(), logged_user.password.encode()):
                # storing user data in session
                request.session['name'] = logged_user.first_name
                request.session['user_id'] = logged_user.id
                # routing to success page
                return redirect('/success')
    # this wasn't a post request, let's redirect home
    return redirect('/')

def logout(request):
    request.session.flush()
    return redirect('/')

## WALL FUNCTIONALITY ##

# add a message
def add_message(request):
    # make sure this is a POST request
    if request.method == 'POST':
        # validate our message!
        errors = Wall_Message.objects.validator(request.POST)
        # if we have errors
        if errors:
            # throw them into messages
            for key, values in errors.items():
                messages.error(request, values)
            return redirect('/success')
        # creating our message
        new_mess = Wall_Message.objects.create(content=request.POST['content'], poster=User.objects.get(id=request.session['user_id']))
        print(new_mess, "IS THIS A MESSAGE")
        return redirect('/success')
    return redirect('/')

def add_comm(request, id):
    # create a comment object
    # retrieving user with id from session
    poster = User.objects.get(id=request.session['user_id'])
    # retrieving message using id in url
    mess = Wall_Message.objects.get(id=id)
    # create the comment
    Comment.objects.create(content=request.POST['content'], poster=poster, message=mess)
    return redirect('/success')

def profile(request, id):
    context = {
        'one_user': User.objects.get(id=id)
    }
    return render(request, 'profile.html', context)

def edit_mess(request, id):
    # render a form where we can edit
    one_mess = Wall_Message.objects.get(id=id)
    if request.method == 'POST':
        one_mess.content = request.POST['content']
        one_mess.save()
        return redirect(f'/profile/{str(one_mess.poster.id)}')
    context = {
        'edit_mess': one_mess
    }
    return render(request, 'edit.html', context)

def delete_mess(request, id):
    Wall_Message.objects.get(id=id).delete()
    return redirect('/success')

def add_like(request, id):
    liked_message = Wall_Message.objects.get(id=id)
    user_liking = User.objects.get(id=request.session['user_id'])
    liked_message.likes.add(user_liking)
    return redirect('/success')
