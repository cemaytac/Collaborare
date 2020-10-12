from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Player, Training
from .forms import StatForm

# Create your views here.


def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')


def players_index(request):
    players = Player.objects.all()
    return render(request, 'players/index.html', {'players': players})


def players_detail(request, player_id):
    player = Player.objects.get(id=player_id)
    stat_form = StatForm()
    return render(request, 'players/detail.html', {'player': player, 'stat_form': stat_form})


def add_stats(request, player_id):
    form = StatForm(request.POST)
    if form.is_valid():
        new_stats = form.save(commit=False)
        new_stats.player_id = player_id
        new_stats.save()
    return redirect('detail', player_id=player_id)


class PlayerCreate(CreateView):
    model = Player
    fields = ['first_name', 'last_name', 'age', 'kitNumber',
              'position', 'preferredFoot', 'team']


class PlayerUpdate(UpdateView):
    model = Player
    fields = ['first_name', 'last_name', 'age', 'kitNumber',
              'position', 'preferredFoot', 'team']


class PlayerDelete(DeleteView):
    model = Player
    success_url = '/players/'


class TrainingList(ListView):
    model = Training


class TrainingDetail(DetailView):
    model = Training
