from django.db import models
from datetime import date


class Animaux(models.Model):
    identifiant = models.CharField(max_length=50)
    date_naissance = models.DateField(auto_now_add=False, null=True, blank=True)
    date_enregistrement = models.DateField(auto_now_add=True, null=True, blank=True)

    # age = models.IntegerField()
    poids = models.IntegerField()
    STATUT_CHOICES =(
        ('Male', 'M'),
        ('Female', 'F'),
    )
    sexe = models.CharField(choices=STATUT_CHOICES, max_length=10)

    @property
    def age(self):
        today = date.today()
        age = today.year - self.date_naissance.year - (
            (today.month, today.day) < (self.date_naissance.month, self.date_naissance.day)
        )
        return age
    
    def __str__(self):
        return self.identifiant