from django.shortcuts import render
from home.models.gameupdates_model import Gameupdate
from django.views.generic import ListView
# Create your views here.

class GameupdateListView(ListView):
    context_object_name = "gameupdates"
    queryset = Gameupdate.objects.all()
    template_name = 'gameupdate/gameupdate.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["gameupdates"] = Gameupdate.objects.all() 
        return context
    