from django.shortcuts import render
from .models import Animaux

# Create your views here.
def home(request):
    return render(request, 'index.html')

def tableau(request):
    mes_animaux = Animaux.objects.all()
    mes_animaux = mes_animaux.order_by('date_naissance')
    context = {
         'mes_animaux' : mes_animaux,
    }
    return render(request, 'tableau.html', context)

def update(request):
    if request.method == 'POST':
        for animal in Animaux.objects.all():
            # Récupérer les valeurs envoyées par le formulaire et mettre à jour l'objet
            animal.date_naissance = request.POST.get(f'date_naissance_{animal.id}', animal.date_naissance)
            animal.date_enregistrement = request.POST.get(f'date_enregistrement_{animal.id}', animal.enregistrement)

            animal.poids = request.POST.get(f'poids_{animal.id}', animal.poids)
            animal.sexe = request.POST.get(f'sexe_{animal.id}', animal.sexe)
            animal.save()
        return redirect('tableau')
    else:
        mes_animaux = Animaux.objects.all()
        return render(request, 'update.html', {'mes_animaux': mes_animaux})




from django.shortcuts import render, redirect
from django.contrib import messages

# Prédéfinit le nom d'utilisateur et le mot de passe
PREDEFINED_USERNAME = "django"  # Remplace par ton nom d'utilisateur
PREDEFINED_PASSWORD = "django"  # Remplace par ton mot de passe

def connexion(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        if username == PREDEFINED_USERNAME and password == PREDEFINED_PASSWORD:
            return redirect('tableau')  
        else:
            messages.error(request, "Nom d'utilisateur ou mot de passe incorrect")
            
    return render(request, 'connexion.html')
