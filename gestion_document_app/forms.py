from django import forms
from .models import *

class DepotForm(forms.ModelForm):
    class Meta:
        model=Depot
        fields=['numero_depot','intitule_depot']


class ArticleForm(forms.ModelForm):
    class Meta:
        model=Article
        fields=["article_id","article_ref","article_design","prix_achat"]



class DeviseForm(forms.ModelForm):
    class Meta:
        model=Devise
        fields=["devise_id","devise_intitule"]


class FamilleForm(forms.ModelForm):
    class Meta:
        model=Famille
        fields=["famille_id","famille_intitule"]



class DepartementForm(forms.ModelForm):
    class Meta:
        model=Departement
        fields=["departement_id","departement_intitule"]



class FournisseurForm(forms.ModelForm):
    class Meta:
        model=Fournisseur
        fields=["fournisseur_id","fournisseur_intitule","fournisseur_adresse","fournisseur_telephone","fournisseur_email"]