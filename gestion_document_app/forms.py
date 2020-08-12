from django import forms

from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

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


class UserCreateForm(UserCreationForm):

    class Meta:
        fields = ('username','email','password1')
        model = get_user_model()

class DateInput(forms.DateInput):
    input_type = 'date'

class DocumentForm(forms.ModelForm):
    class Meta:
        model=Document
        fields=["document_id","document_piece","document_type","document_date","fournisseur_id","document_devise","document_reference"]
        widgets = {
            'document_date': DateInput()
        }
class DocumentFormValid1(forms.ModelForm):
    
    class Meta:
        model=Document
        fields=["document_id","numero_depot","document_date_livraison","document_cours","departement_id"]
        widgets = {
            'document_date_livraison': DateInput()
        }
        
class DocumentFormValid2(forms.ModelForm):
    class Meta:
        model=Document
        fields=["document_id","article_id","document_P_U_DEV","document_QT","document_taxe","document_remise"]
        