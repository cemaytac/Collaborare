from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView, TemplateView
from .models import Player, Training, Team
from .forms import StatForm, SignupForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm

# Create your views here.


def signup(request):
    error_message = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            # This will add the user to the database
            user = form.save()
            # This is how we log a user in via code
            login(request, user)
            return redirect('index')
        else:
            error_message = 'Invalid sign up - try again'
    # A bad POST or a GET request, so render signup.html with an empty form
    signupform = SignupForm()
    context = {'signupform': signupform, 'error_message': error_message}
    return render(request, 'registration/signup.html', context)


def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')


@login_required
def players_index(request):
    players = Player.objects.all()
    return render(request, 'players/index.html', {'players': players})


@login_required
def players_detail(request, player_id):
    player = Player.objects.get(id=player_id)
    training_player_doesnt_have = Training.objects.exclude(
        id__in=player.training.all().values_list('id'))
    stat_form = StatForm()
    return render(request, 'players/detail.html', {'player': player, 'stat_form': stat_form, 'training': training_player_doesnt_have})


@login_required
def team_index(request):
    teams = Team.objects.filter(user=request.user)
    return render(request, 'team/index.html', {'teams': teams})


@login_required
def team_detail(request, team_id):
    team = Team.objects.get(id=team_id)
    players = Player.objects.filter(team=team)
    trainings = Training.objects.filter(team=team)
    return render(request, 'team/detail.html', {'team': team, 'players': players, 'trainings': trainings})


@login_required
def add_stats(request, player_id):
    form = StatForm(request.POST)
    if form.is_valid():
        new_stats = form.save(commit=False)
        new_stats.player_id = player_id
        new_stats.save()
    return redirect('detail', player_id=player_id)


# @login_required
# def team_create(request, user):
#     form = TeamForm(request.POST)
#     if form.is_valid():
#         new_team = form.save(commit=False)
#         user = new_team.user
#         new_team.save()
#     return redirect('team/create.html', user=user)


class TeamCreate(LoginRequiredMixin, CreateView):
    model = Team
    fields = '__all__'
    success_url = '/team/'


class PlayerCreate(LoginRequiredMixin, CreateView):
    model = Player
    fields = ['first_name', 'last_name', 'age', 'kitNumber',
              'position', 'preferredFoot', 'team']


class PlayerUpdate(LoginRequiredMixin, UpdateView):
    model = Player
    fields = '__all__'


class PlayerDelete(LoginRequiredMixin, DeleteView):
    model = Player
    success_url = '/players/'


class TrainingList(LoginRequiredMixin, ListView):
    model = Training


class TrainingDetail(LoginRequiredMixin, DetailView):
    model = Training


class TrainingCreate(LoginRequiredMixin, CreateView):
    model = Training
    fields = '__all__'


class TrainingUpdate(LoginRequiredMixin, UpdateView):
    model = Training
    fields = ['drill', 'date', 'description', 'duration', 'completed', ]


class TrainingDelete(LoginRequiredMixin, DeleteView):
    model = Training
    success_url = '/training/'


@login_required
def assoc_training(request, player_id, training_id):
    Player.objects.get(id=player_id).training.add(training_id)
    return redirect('detail', player_id=player_id)
