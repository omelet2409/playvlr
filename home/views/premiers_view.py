from django.shortcuts import render
from home.models.premiers_model import Premier
from django.views.generic import ListView
# Create your views here.

class PremierListView(ListView):
    context_object_name = "premiers"
    queryset = Premier.objects.all()
    template_name = 'premier/premier.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["premiers"] = Premier.objects.all() 
        return context