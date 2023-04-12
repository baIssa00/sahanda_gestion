from django.contrib import admin
from .models import *

@admin.register(Commission)
class CommissionAdmin(admin.ModelAdmin):
    list_display = ['nom', 'cellule', 'responsable', 'description']
    
@admin.register(Membre)
class MembreAdmin(admin.ModelAdmin):
    list_display = ['nom', 'prenom', 'cellule', 'telephone', 'commission']
    
@admin.register(Cotisation)
class CotisationAdmin(admin.ModelAdmin):
    list_display = ['membre', 'type_cotisation', 'montant', 'date']
    
@admin.register(Produit)
class ProduitAdmin(admin.ModelAdmin):
    list_display = ['code', 'nom', 'quantite', 'commission']
    
@admin.register(Cellule)
class CelluleAdmin(admin.ModelAdmin):
    list_display = ['nom']
    
@admin.register(TypeCotisation)
class TypeCotisation(admin.ModelAdmin):
    list_display = ['nom']
