from django.urls import path, include

from .views import main_page, list_of_players, trophy, date_of_match


urlpatterns = [
    path('', main_page),
    path('models.Players/', list_of_players),
    path('info/models.Trophies', trophy),
    path('info/models.Matches', date_of_match),
]