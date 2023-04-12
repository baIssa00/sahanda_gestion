from django.db import models
from .utils import generate_code
from django.utils import timezone

class Cellule(models.Model):
    nom = models.CharField(max_length=255)

    def __str__(self):
        return self.nom


class TypeCotisation(models.Model):
    nom = models.CharField(max_length=100)

    def __str__(self):
        return self.nom
    
    
class Commission(models.Model):
    nom = models.CharField(max_length=100)
    cellule = models.ForeignKey(Cellule, on_delete=models.SET_NULL, null=True, blank=True, related_name='commissions_cellule')
    responsable = models.ForeignKey('Membre', on_delete=models.SET_NULL, null=True, blank=True, related_name='commissions_responsable')
    description = models.TextField(blank=True)

    def __str__(self):
        return self.nom

class Membre(models.Model):
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    cellule = models.ForeignKey(Cellule, on_delete=models.CASCADE)
    telephone = models.CharField(max_length=20, null=True, blank=True)
    commission = models.ForeignKey(Commission, on_delete=models.SET_NULL, null=True, blank=True)
    
    def __str__(self):
        return f"{self.prenom} - {self.nom}"

class Cotisation(models.Model):
    membre = models.ForeignKey(Membre, on_delete=models.CASCADE)
    type_cotisation = models.ForeignKey(TypeCotisation, on_delete=models.CASCADE)
    montant = models.DecimalField(max_digits=8, decimal_places=2)
    date = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return f"Cotisation de {self.membre} - {self.date}"


class Produit(models.Model):
    code = models.CharField(max_length=10, unique=True, blank=True, editable=False)
    nom = models.CharField(max_length=100)
    quantite = models.IntegerField(default=0)
    commission = models.ForeignKey(Commission, on_delete=models.CASCADE)

    def __str__(self):
        return self.nom

    def save(self, *args, **kwargs):
        if not self.code:
            self.code = generate_code(self.nom)
        super().save(*args, **kwargs)
