from django.shortcuts import render, redirect

def index(request):
    # if 'user_list' not in request.session:
    #     print("Initializing empty list")
    #     request.session['user_list'] = []
    return render(request, 'index.html')

def start_game(request):
    request.session['user_list'] = []
    return redirect('/')

def process(request):
    print(request.POST, "This is my form data queryset")
    request.session['user_list'].append(request.POST['username'])
    print(request.session['user_list'], "this is my list in session")
    return redirect('/view_user')

def view_user(request):
    print(request.session['user_list'], "the user list from the view_user method")
    return render(request, 'user.html')

def reset(request):
    request.session.clear()
    return redirect('/')

