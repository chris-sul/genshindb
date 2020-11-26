from django.db import models

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
        ('bow', 'BOW'),
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