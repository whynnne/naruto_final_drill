from django.contrib import admin
from .models import Village, Character, Jutsu

@admin.register(Village)
class VillageAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at', 'updated_at')

@admin.register(Character)
class CharacterAdmin(admin.ModelAdmin):
    list_display = ('name', 'power_level', 'rating', 'rarity', 'created_at', 'updated_at')
    search_fields = ('name', 'rarity', 'village__name')
    list_filter = ('rarity', 'village')

@admin.register(Jutsu)
class JutsuAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at', 'updated_at')
    filter_horizontal = ('character',)