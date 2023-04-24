from django.shortcuts import render
from home.models.tutorials_model import Tutorial
from django.views.generic import ListView
# Create your views here.

class TutorialListView(ListView):
    context_object_name = "tutorials"
    queryset = Tutorial.objects.all()
    template_name = 'tutorial/tutorial.html'
    
    
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["tutorials"] = Tutorial.objects.all() 
        return context