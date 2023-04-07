from django.contrib import admin
from home.models.agents_model import Agent
from home.models.maps_model import Map
from home.models.weapons_model import Weapon
from home.models.home_model import Home
from home.models.specs_model import Spec
from home.models.newss_model import News
from home.models.signups_model import Signup

# Register your models here.
admin.site.register(Agent)
admin.site.register(Map)
admin.site.register(Weapon)
admin.site.register(Home)
admin.site.register(Spec)
admin.site.register(News)
admin.site.register(Signup)