from django import forms
from .models import *

class MembreForm(forms.ModelForm):
    class Meta:
        model = Membre
        fields = ['prenom', 'nom', 'cellule', 'commission']
        

class NouveauMembreForm(forms.ModelForm):
    class Meta:
        model = Membre
        fields = ['prenom', 'nom', 'cellule', 'commission']
        
        
class CommissionForm(forms.ModelForm):
    class Meta:
        model = Commission
        fields = ['nom', 'cellule', 'responsable', 'description']
        

class ProduitForm(forms.ModelForm):
    commission = forms.ModelChoiceField(queryset=Commission.objects.all())
    
    class Meta:
        model = Produit
        fields = ['nom', 'quantite', 'commission']
        

class CotisationForm(forms.ModelForm):
    type_cotisation = forms.ModelChoiceField(queryset=TypeCotisation.objects.all())

    class Meta:
        model = Cotisation
        fields = ['membre', 'montant', 'type_cotisation']