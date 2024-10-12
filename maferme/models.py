from django.db import models
from datetime import datetime, date



class Animaux(models.Model):
    identifiant = models.CharField(max_length=50)
    date_naissance = models.DateField(auto_now_add=False, null=True, blank=True)
    date_enregistrement = models.DateField(auto_now_add=True, null=True, blank=True)
    age = models.CharField(max_length=50, null=True, blank=True)  
    poids = models.PositiveIntegerField()  
    
    STATUT_CHOICES =(
        ('Male', 'M'),
        ('Female', 'F'),
    )
    sexe = models.CharField(choices=STATUT_CHOICES, max_length=10)
    
    
    def save(self, *args, **kwargs):
        # calcul l'âge en années
        if isinstance(self.date_naissance, str):
            self.date_naissance = datetime.strptime(self.date_naissance, "%Y-%m-%d").date()
        if isinstance(self.date_enregistrement, str):
            self.date_enregistrement = datetime.strptime(self.date_enregistrement, "%Y-%m-%d").date()
        
        if self.date_naissance:
            today = date.today()
            age_years = today.year - self.date_naissance.year
            age_months = today.month - self.date_naissance.month
            age_days = today.day - self.date_naissance.day
            if age_years < 1:
                # Si âge est infé à 1 an, afficher en mois
                age_in_months = age_months + (12 if age_days < 0 else 0)  # Compte les mois
                age_in_months = age_in_months if age_in_months >= 0 else 0  # Éviter les valeurs négatives
                self.age = f"{age_in_months} mois"
            else:
                # Si âge est sup ou égal à 1, afficher en années, mois et jours
                if age_days < 0:
                    age_months -= 1
                    age_days += 30  # Approximatif pour les jours

                self.age = f"{age_years} ans, {age_months} mois, {age_days} jours"

        super(Animaux, self).save(*args, **kwargs)

    
    def __str__(self):
        return self.identifiant