from django.contrib import admin
from .models import *

# Register your models here.

@admin.register(Header)
class HeaderAdmin(admin.ModelAdmin):
    list_display = ('titre', 'texte')
    fields = ('titre', 'image', 'texte')


@admin.register(PetitModel)
class PetitModelAdmin(admin.ModelAdmin):
    list_display = ('sujet', 'texte')
    fields = ('sujet', 'image', 'texte')


@admin.register(RowGx70)
class RowGx70Admin(admin.ModelAdmin):
    list_display = ('nom', 'texte', 'fonction')
    fields = ('image', 'texte', 'photo_profil', 'nom', 'fonction')

@admin.register(Partenaires)
class Partenaires(admin.ModelAdmin):
    list_display = ('texte', 'image')
    fields = ('texte', 'image')

@admin.register(Section)
class Section(admin.ModelAdmin):
    list_display = ('titre', 'texte')
    fields = ('titre', 'texte', 'image')

@admin.register(Professeur)
class Professeur(admin.ModelAdmin):
    list_display = ('nom', 'matiere')
    fields = ('nom', 'matiere', 'photo')