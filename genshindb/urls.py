"""genshindb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import include, path
from django.conf.urls import url
from rest_framework import routers
from markdownx import urls as markdownx

from genshindb import views

from .characters.views import CharacterViewSet, NormalAttackViewSet, ElementalSkillViewSet, \
    ElementalBurstViewSet


from .characters.urls import urlpatterns as characters_urls

admin.autodiscover()

# Api routers
public_router = routers.DefaultRouter()
public_router.register('characters', CharacterViewSet)
public_router.register('normalattack', NormalAttackViewSet)
public_router.register('elementalskill', ElementalSkillViewSet)
public_router.register('elementalburst', ElementalBurstViewSet)

app_name = 'genshindb'

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', views.index, name='index'),

    path('characters/', include(characters_urls)),
    url(r'^markdownx/', include(markdownx)),

    # API
    path('api/v1/', include(public_router.urls)),
]
