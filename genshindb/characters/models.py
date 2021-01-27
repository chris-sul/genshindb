from django.db import models
from markdownx.models import MarkdownxField
from markdownx.utils import markdownify

# Create your models here.


class Character(models.Model):
    # Types
    ELEMENTAL_TYPES = [
        ('anemo', 'Anemo'),
        ('cryo', 'Cryo'),
        ('electro', 'Electro'),
        ('dendro', 'Dendro'),
        ('geo', 'Geo'),
        ('hydro', 'Hydro'),
        ('pyro', 'Pyro'),
    ]

    WEAPON_TYPES = [
        ('bow', 'Bow'),
        ('catalyst', 'Catalyst'),
        ('claymore', 'Claymore'),
        ('polearm', 'Polearm'),
        ('sword', 'Sword'),
    ]

    # Basic Information
    name = models.CharField(max_length=16)
    tier = models.IntegerField()
    description = models.CharField(max_length=256)
    rarity = models.IntegerField()
    elemental_type = models.CharField(max_length=16, choices=ELEMENTAL_TYPES)
    weapon_type = models.CharField(max_length=16, choices=WEAPON_TYPES)

    def __str__(self) -> str:
        return self.name


#####
# Skill Talents
#####

class SkillTalent(models.Model):
    name = models.CharField(max_length=64)
    character = models.ForeignKey(Character, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.name


class NormalAttack(SkillTalent):
    # Attack descriptions
    normal= models.CharField(max_length=256)
    charged = models.CharField(max_length=256)
    plunging = models.CharField(max_length=256)

    # Attack values
    values = models.JSONField(default=dict, blank=True)


class ElementalSkill(SkillTalent):
    text = MarkdownxField()

    # Attack values
    values = models.JSONField(default=dict, blank=True)

    # Create a property that returns the markdown instead
    @property
    def formatted_markdown(self):
        return markdownify(self.text)

class ElementalBurst(SkillTalent):
    text = MarkdownxField()

    # Attack values
    values = models.JSONField(default=dict, blank=True)

    # Create a property that returns the markdown instead
    @property
    def formatted_markdown(self):
        return markdownify(self.text)