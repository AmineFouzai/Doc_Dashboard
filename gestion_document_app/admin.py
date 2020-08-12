from django.contrib import admin
from .models import(Depot,Article,Departement,Devise,Fournisseur,Famille,Document)
# Register your models here.

admin.site.register(Depot)
admin.site.register(Article)
admin.site.register(Devise)
admin.site.register(Departement)
admin.site.register(Fournisseur)
admin.site.register(Famille)
admin.site.register(Document)



