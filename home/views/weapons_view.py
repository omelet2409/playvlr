from django.shortcuts import render
from home.models.weapons_model import Weapon
from django.views.generic import ListView
from django.views.generic import DetailView
# Create your views here.

class WeaponListView(ListView):
    context_object_name = "weapons"
    
    queryset = Weapon.objects.all()
    template_name = 'weapon/weapon.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["weapons"] = Weapon.objects.all() 
        return context

class WeaponDetailView(DetailView):
    model = Weapon
    template_name = 'weapon/weapon_detail.html'
    
    def get_context_data(self, **kwargs):
        kwargs['weapon'] = self.get_object
        return super().get_context_data(**kwargs)