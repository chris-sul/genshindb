from django.shortcuts import render
from django.http import HttpResponse
from genshindb.characters.models import Character

# Create your views here.
def index(request):
    ctx = {
        'characters': Character.objects.all()
    }
    return render(request, 'characters.html', ctx)