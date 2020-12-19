from django.urls import path

from . import views

app_name = 'characters'

urlpatterns = [
    path('', views.index, name='index'),
    path('<slug:slug>/', views.CharacterDetailView.as_view() , name='character'),
]