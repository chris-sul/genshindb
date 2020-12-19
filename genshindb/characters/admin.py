from django.contrib import admin

from .models import Character, NormalAttack, ElementalSkill, ElementalBurst

from markdownx.admin import MarkdownxModelAdmin

admin.site.register(Character)
admin.site.register(NormalAttack)
admin.site.register(ElementalSkill, MarkdownxModelAdmin)
admin.site.register(ElementalBurst, MarkdownxModelAdmin)