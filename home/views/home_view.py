from django.shortcuts import render
from home.models.home_model import Home
from home.models.newss_model import News
from django.views.generic import ListView


# Create your views here.

class HomeListView(ListView):
    context_object_name = "homes"
    paginate_by = 12
    queryset = Home.objects.all()
    template_name = 'home.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["homes"] = Home.objects.all() 
        return context

class NewsListView(ListView):
    context_object_name = "newss"
    paginate_by = 12
    queryset = News.objects.all()
    template_name = 'news/news.html' 
    #
    #
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["newss"] = News.objects.all().order_by('-datetime')
        return context
