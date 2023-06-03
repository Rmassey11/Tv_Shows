from django.shortcuts import render, HttpResponse, redirect
from .models import *
from django.contrib import messages
# Create your views here.

def index(request):
    context = {
        'AllShows': Show.objects.all() 
    }
    return render(request, 'index.html', context)

def new(request):
    return render(request, 'new.html')

def create(request):
    if request.method == 'POST':
        errors = Show.objects.show_validator(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
        else:
            ShowTitle = request.POST['title']
            ShowNetwork = request.POST['network']
            ShowDate = request.POST['release_date']
            ShowDesc = request.POST['desc']
            Show.objects.create(title=ShowTitle, network=ShowNetwork, release_date=ShowDate, desc=ShowDesc)
    return redirect('/')

def show(request, ShowId):
    context = {
        'show': Show.objects.filter(id=ShowId)[0]
    }
    return render(request, 'show.html', context)

def edit(request, ShowId):
    context = {
        'show': Show.objects.filter(id=ShowId)[0]
    }
    return render(request, 'edit.html', context)

def update(request, ShowId):
    if request.method == 'POST':
        toUpdate = Show.objects.get(id=ShowId)
        toUpdate.title = request.POST['title']
        toUpdate.network = request.POST['network']
        toUpdate.release_date = request.POST['release_date']
        toUpdate.desc = request.POST['desc']
        toUpdate.save()
    return redirect('/shows/<int:ShowId>')

def delete(request, ShowId):
    toDelete = Show.objects.get(id=ShowId)
    toDelete.delete()
    return redirect('/')