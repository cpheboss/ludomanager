from django.shortcuts import render
from django.views import generic
from ludomanagerapp.models import Game, Member

# Create your views here.

def index(request):
    """View function for home page of site"""

    num_members = Member.objects.count()
    num_games = Game.objects.count()

    context = {
        'num_members' : num_members,
        'num_games' : num_games,
    }

    return render(request, 'index.html', context = context)

class GameListView(generic.ListView):
    model = Game
    paginate_by = 10

class GameDetailView(generic.DetailView):
    model = Game

class MemberListView(generic.ListView):
    model = Member
    paginate_by = 10

class MemberDetailView(generic.DetailView):
    model = Member
    
