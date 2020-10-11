from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')


def players_index(request):
    return render(request, 'players/index.html', {'players': players})
