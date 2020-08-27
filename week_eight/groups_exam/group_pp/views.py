from django.shortcuts import render, redirect
from .models import *

## Home methods

def index(request):
    return redirect('/main')

def main(request):
    return render(request, 'main.html')

def groups(request):
    context = {
        'all_orgs': Organization.objects.all()
    }
    return render(request, 'groups.html', context)

## log/reg methods

def register(request):
    if request.method == 'POST':
        print(request.POST)

        # create a user
        new_user = User.objects.create(first_name=request.POST['first_name'], last_name=request.POST['last_name'], email=request.POST['email'], password=request.POST['password'])
        print(new_user)
        request.session['name'] = new_user.first_name + ' ' + new_user.last_name
        request.session['user_id'] = new_user.id
        return redirect('/groups')
    return redirect('/main')

def login(request):
    if request.method == 'POST':
        # filter for user in DB
        logged_user = User.objects.filter(email=request.POST['email'])
        # if the filter query returned any users
        if len(logged_user) > 0:
            # store that user in logged_user
            logged_user = logged_user[0]
            if logged_user.password == request.POST['password']:
                print(logged_user, "successfully logged in")
                request.session['name'] = logged_user.first_name + ' ' + logged_user.last_name
                request.session['user_id'] = logged_user.id
                return redirect('/groups')
    return redirect('/main')

def logout(request):
    request.session.clear()
    return redirect('/')

## main content methods

def create_org(request):
    if request.method == 'POST':
        # Create an org
        user = User.objects.get(id=request.session['user_id'])
        new_org = Organization.objects.create(name=request.POST['org_name'], description = request.POST['description'], creator = user)
        print(new_org)
        new_org.members.add(user)
        return redirect('/groups')
    return redirect('/main')

def one_group(request, id):
    # get the clicked group
    context = {
        'one_org': Organization.objects.get(id=id),
        'user': User.objects.get(id=request.session['user_id'])
    }
    return render(request, 'one_org.html', context)

def join_org(request, id):
    # user joining
    user = User.objects.get(id=request.session['user_id'])
    # org being joined
    org = Organization.objects.get(id=id)
    # add user to org!
    org.members.add(user)
    return redirect(f'/groups/{user.id}')

def leave_org(request, id):
    user = User.objects.get(id=request.session['user_id'])
    org = Organization.objects.get(id=id)
    org.members.remove(user)
    return redirect(f'/groups/{user.id}')

def delete_org(request, id):
    Organization.objects.get(id=id).delete()
    return redirect('/groups')