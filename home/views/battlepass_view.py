from django.shortcuts import render
from home.models.battlepass_model import Battlepass
from django.views.generic import ListView


class BattlepassListView(ListView):
    context_object_name = "battlepasss"
    paginate_by = 12
    queryset = Battlepass.objects.all()
    template_name = 'battlepass/battlepass.html' 
    #
    #
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["battlepasss"] = Battlepass.objects.all()
        return context
