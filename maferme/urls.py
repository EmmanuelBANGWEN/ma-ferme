
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('tableau/', views.tableau, name='tableau'),
    path('connexion/', views.connexion, name='connexion'),
    path('Mise_a_jour/', views.update, name='update'),




]
