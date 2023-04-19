from django.shortcuts import render
from home.models.signups_model import Signup
from django.views.generic import ListView
# Create your views here.

class SignupListView(ListView):
    context_object_name = "signups"
    queryset = Signup.objects.all()
    template_name = 'signup/signup.html'
    
    
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["signups"] = Signup.objects.all() 
        return context