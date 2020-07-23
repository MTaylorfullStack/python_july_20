from django.shortcuts import render, HttpResponse

def index(request):
    return HttpResponse("We have successfully started a Django project!")

# Create your views here.
