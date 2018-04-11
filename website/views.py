from django.shortcuts import render
from .models import Band, Album, Track

def index(request):
    old_albums = Album.get_old_albums()
    context = {
        'old_albums': old_albums
    }
    return render(request, 'website/index.html', context)