"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include

from home import views as home
from home.views.agents_view import AgentListView
from home.views.agents_view import AgentDetailView
from home.views.map_view import MapListView
from home.views.map_view import MapDetailView
from home.views.weapons_view import WeaponListView
from home.views.weapons_view import WeaponDetailView
from home.views.home_view import HomeListView
from home.views.specs_view import SpecsListView
from home.views.news_view import NewsListView
from home.views.tutorials_view import TutorialListView
from home.views.premiers_view import PremierListView
from home.views.battlepass_view import BattlepassListView


app_name = "home"

urlpatterns = [
    path('admin/', admin.site.urls),


    path(
        route='',
        view=HomeListView.as_view(),
        name='home',
    ),
    path(
        route='agents/',
        view=AgentListView.as_view(),
        name='agents',
    ),
    path(
        route='agents/<str:slug>/',
        view=AgentDetailView.as_view(),
        name='agent_detail',
    ),
    path(
        route='maps/',
        view=MapListView.as_view(),
        name='maps',
    ),
    path(
        route='maps/<str:slug>/',
        view=MapDetailView.as_view(),
        name='map_detail',
    ),
    path(
        route='weapons/',
        view=WeaponListView.as_view(),
        name='weapons',
    ),
    path(
        route='weapons/<str:slug>/',
        view=WeaponDetailView.as_view(),
        name='weapon_detail',
    ),
    path(
        route='specs/',
        view=SpecsListView.as_view(),
        name='specs',
    ),

    path(
        route='news/',
        view=NewsListView.as_view(),
        name='news',
    ),
    path(
        route='tutorials/',
        view=TutorialListView.as_view(),
        name='tutorials',
    ),
    path(
        route='premiers/',
        view=PremierListView.as_view(),
        name='premiers',
    ),
    path(
        route='battlepass/',
        view=BattlepassListView.as_view(),
        name='battlepass',
    ),



]
