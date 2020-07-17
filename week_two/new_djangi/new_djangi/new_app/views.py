from django.shortcuts import render

# Create your views here.

def first_method(request):
    return render(request, 'index.html')

def new_page(request):
    
    context = {
        'number_of_refreshes': 10
    }
    return render(request, 'new.html', context)
