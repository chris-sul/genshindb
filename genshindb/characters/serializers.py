from rest_framework import serializers
from genshindb.characters.models import *


class CharacterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Character
        fields = ['name', 'tier', 'description', 'rarity', 'elemental_type', 'weapon_type']


class NormalAttackSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = NormalAttack
        fields = ['name', 'character', 'normal', 'charged', 'plunging', 'values']


class ElementalSkillSerializer(serializers.HyperlinkedModelSerializer):
    text = serializers.SerializerMethodField('markdown_text')

    def markdown_text(self, val):
        return val.text

    class Meta:
        model = NormalAttack
        fields = ['name', 'character', 'text', 'values']


class ElementalBurstSerializer(serializers.HyperlinkedModelSerializer):
    text = serializers.SerializerMethodField('markdown_text')

    def markdown_text(self, val):
        return val.text

    class Meta:
        model = NormalAttack
        fields = ['name', 'character', 'text', 'values']