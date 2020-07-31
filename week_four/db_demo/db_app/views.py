from django.shortcuts import render, redirect
from .models import *

def root(request):
    return render(request, "home.html")

def register(request):
    # creating a new User
    if request.method == 'POST':
        new_user = User.objects.create(username= request.POST['name'], password=request.POST['pw'])
        print(new_user)
        request.session['name'] = new_user.username
        request.session['user_id'] = new_user.id
        return redirect('/success')
    return redirect('/')

def success(request):
    context = {
        'all_messages': Message_Post.objects.all()
    }
    return render(request, "media.html", context)

def login(request):
    # log somebody in
    # see if username exists in db
    if request.method == 'POST':
        logged_user = User.objects.filter(username=request.POST['name'])
        print(logged_user, "this is the result of the filter query")
        if len(logged_user) > 0:
            print(logged_user[0], "this is the user within the queryset")
            if logged_user[0].password == request.POST['pw']:
                request.session['name'] = logged_user[0].username
                request.session['user_id'] = logged_user[0].id
                return redirect('/success')
        # does their password match
        return redirect('/')
    return redirect('/')

def create_mess(request):
    if request.method == 'POST':
        # create a wall post
        new_post = Message_Post.objects.create(content=request.POST['mess_content'], poster=User.objects.get(id=request.session['user_id']))
        print(new_post)
        return redirect('/success')
    return redirect('/')

def profile(request, user_id):
    # retrieve the correlating user
    context = {
        'one_user': User.objects.get(id=user_id)
    }
    return render(request, "profile.html", context)