from django.contrib import admin
from .models import Animaux


@admin.register(Animaux)
class AnimauxAdmin(admin.ModelAdmin):
    list_display = ('identifiant', 'date_naissance', 'date_enregistrement', 'age', 'poids', 'sexe')
  