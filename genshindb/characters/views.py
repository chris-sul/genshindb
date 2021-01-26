from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import DetailView
from rest_framework import viewsets, mixins
from django_filters.rest_framework import DjangoFilterBackend

from genshindb.characters.models import Character, SkillTalent, NormalAttack, ElementalSkill, ElementalBurst
from genshindb.characters.serializers import CharacterSerializer, NormalAttackSerializer

def index(request):
    ctx = {
        'characters': Character.objects.all()
    }
    return render(request, 'characters.html', ctx)


class CharacterDetailView(DetailView):
    model = Character
    template_name = 'character.html'
    context_object_name = 'character'
    slug_field = 'name__iexact'

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)

        if ctx['character'].skilltalent_set.all().exists():
            ctx['skilltalents'] = []
            for talent in NormalAttack.objects.filter(character=ctx['character']):
                talent.typename = 'Normal Attack'
                ctx['skilltalents'].append(talent)
            for talent in ElementalSkill.objects.filter(character=ctx['character']):
                talent.typename = 'Elemental Skill'
                ctx['skilltalents'].append(talent)
            for talent in ElementalBurst.objects.filter(character=ctx['character']):
                talent.typename = 'Elemental Burst'
                ctx['skilltalents'].append(talent)
        else:
            ctx['skilltalents'] = None
        return ctx


# API
class CharacterViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Character.objects.all()
    serializer_class = CharacterSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('name', 'elemental_type', 'weapon_type', 'rarity',)

class NormalAttackViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = NormalAttack.objects.all()
    serializer_class = NormalAttackSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('name', 'character',)