from django.contrib import admin
from home.models.agents_model import Agent
from home.models.maps_model import Map
from home.models.weapons_model import Weapon
from home.models.home_model import Home
from home.models.specs_model import Spec
from home.models.newss_model import News
from home.models.tutorials_model import Tutorial
from home.models.premiers_model import Premier
from home.models.battlepass_model import Battlepass
from home.models.gameupdates_model import Gameupdate

# Register your models here.
admin.site.register(Agent)
admin.site.register(Map)
admin.site.register(Weapon)
admin.site.register(Home)
admin.site.register(Spec)
admin.site.register(News)
admin.site.register(Tutorial)
admin.site.register(Premier)
admin.site.register(Battlepass)
admin.site.register(Gameupdate)