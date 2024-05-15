from django.shortcuts import render
from home.models.maps_model import Map
from django.views.generic import ListView
from django.views.generic import DetailView
# Create your views here.

class MapListView(ListView):
    context_object_name = "maps"

    queryset = Map.objects.all()
    template_name = 'map/map.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["maps"] = Map.objects.all().order_by('name')
        return context
    
class MapDetailView(DetailView):
    model = Map
    template_name = 'map/map_detail.html'
    
    def get_context_data(self, **kwargs):
        kwargs['map'] = self.get_object
        return super().get_context_data(**kwargs)