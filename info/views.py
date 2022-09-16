from django.shortcuts import render
from .models import Players, Matches, Trophies
# Create your views here.


def main_page(request):
    return render(request, 'info/main.html')


def list_of_players(request):
    list_plays = Players.objects.all()
    context = {
        'list_plays': list_plays
    }
    return render(request, 'players/list_players.html', context)

def trophy(request):
    return render(request, 'trophy/trophy.html')

def date_of_match(request):
    date_match = Matches.objects.all()
    context = {
        'date_match': date_match
    }
    return render(request, 'matches/matches.html', context)