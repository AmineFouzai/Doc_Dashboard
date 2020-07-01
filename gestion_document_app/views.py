from django.shortcuts import render,redirect 
from django.contrib.auth.decorators import login_required
from bokeh.plotting import figure
from bokeh.embed import components
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
import json
from .forms import *
# Create your views here.

@login_required(login_url='/accounts/Login/')
def index_handler(request):
    if request.method=="GET":
        
        pls = ['Depot', 'Devise', 'Departement', 'Fournisseur', 'Article', 'Famille']
        counts=[
            Depot.objects.all().count() if  Exception  else 0, 
            Devise.objects.all().count() if  Exception  else 0,
            Departement.objects.all().count() if  Exception  else 0,
            Fournisseur.objects.all().count() if  Exception  else 0,
            Article.objects.all().count() if  Exception  else 0,
            Famille.objects.all().count() if  Exception  else 0,
        ]
        p = figure(x_range=pls, plot_height=250, title="Statistics",toolbar_location=None, tools="")
        p.vbar(x=pls, top=counts, width=0.9)
        p.xgrid.grid_line_color = None
        p.y_range.start = 0
        p.plot_width = 900
        p.plot_height = 500
        script,div=components(p)
        
        context={
            "script":script,
            "div":div
            }
        return render(request,'gestion_document_app/index.djt',context=context) 

@login_required(login_url='/accounts/Login/')
def depot_handler(request):
    form=DepotForm()
    if request.method=="GET":
        depots=Depot.objects.all()
        context={
        "depots":depots,
        }
        return render(request,'gestion_document_app/Depot.djt',context=context) 

@login_required(login_url='/accounts/Login/')
def delete_depot_handler(request,_id):
    if request.method=="POST":
        doc=Depot.objects.get(numero_depot=_id)
        doc.delete()
        return redirect('depot')

@login_required(login_url='/accounts/Login/')
def add_depot_handler(request):
    
    if request.method=="GET":
        form=DepotForm()
        context={
        "form":form,
        }
        return render(request,'gestion_document_app/AddDepot.djt',context=context)
    elif request.method=="POST":
        form=DepotForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('depot')
        else:
            context={
            "form":form
            }   
            return render(request,'gestion_document_app/AddDepot.djt',context=context)

@login_required(login_url='/accounts/Login/')
def update_depot_handler(request,_id):
    if request.method=="GET":
        doc=Depot.objects.get(numero_depot=_id)
        form=DepotForm(initial={'numero_depot': doc.numero_depot,"intitule_depot":doc.intitule_depot})
        context={
        "form":form
        }
        return render(request,'gestion_document_app/UpdateDepot.djt',context=context)
    elif request.method=="POST":
       
        form=DepotForm(request.POST)
        doc=Depot.objects.get(numero_depot=_id)
        
        if doc.numero_depot==int(form.data['numero_depot']):
            doc.numero_depot=form.data['numero_depot']
            doc.intitule_depot=form.data['intitule_depot']
            doc.save()
            return redirect('depot')
        else:
            doc=Depot.objects.get(numero_depot=_id)
            doc.delete()
            form.save()
            return redirect('depot')
  
@csrf_exempt
def delete_many_depot(request):
    if request.method=="POST":
        docs=json.loads(request.body)
        for doc in docs["todelete"]:
            doc=Depot.objects.get(numero_depot=doc)
            doc.delete()
        return redirect('depot')


#article
@login_required(login_url='/accounts/Login/')
def article_handler(request):
    form=DepotForm()
    if request.method=="GET":
        articles=Article.objects.all()
        context={
        "articles":articles,
        }
        return render(request,'gestion_document_app/Article.djt',context=context) 


@login_required(login_url='/accounts/Login/')
def add_article_handler(request):
    
    if request.method=="GET":
        form=ArticleForm()
        context={
        "form":form,
        }
        return render(request,'gestion_document_app/AddArticle.djt',context=context)
    elif request.method=="POST":
        form=ArticleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('article')
        else:
            context={
            "form":form
            }   
            return render(request,'gestion_document_app/AddArticle.djt',context=context)

@login_required(login_url='/accounts/Login/')
def delete_article_handler(request,_id):
    if request.method=="POST":
        doc=Article.objects.get(article_id=_id)
        doc.delete()
        return redirect('article')


@login_required(login_url='/accounts/Login/')
def update_article_handler(request,_id):

    if request.method=="GET":
        doc=Article.objects.get(article_id=_id)
        form=ArticleForm(initial={
            'article_id': doc.article_id,
            "article_ref":doc.article_ref,
            "article_design":doc.article_design,
            "prix_achat":doc.prix_achat
            })
        print(form)
        context={
        "form":form
        }
        return render(request,'gestion_document_app/UpdateArticle.djt',context=context)
    elif request.method=="POST":
       
        form=ArticleForm(request.POST)
        doc=Article.objects.get(article_id=_id)
        
        if doc.article_id==int(form.data['article_id']):
            doc.article_id=form.data['article_id']
            doc.article_ref=form.data['article_ref']
            doc.article_design=form.data['article_design']
            doc.prix_achat=form.data['prix_achat']
            doc.save()
            return redirect('article')
        else:
            doc=Article.objects.get(article_id=_id)
            doc.delete()
            form.save()
            return redirect('article')

@csrf_exempt
def delete_many_article(request):
    if request.method=="POST":
        docs=json.loads(request.body)
        for doc in docs["todelete"]:
            doc=Article.objects.get(article_id=doc)
            doc.delete()
        return redirect('article')



#devise
@login_required(login_url='/accounts/Login/')
def devise_handler(request):
    form=DeviseForm()
    if request.method=="GET":
        devises=Devise.objects.all()
        context={
        "devises":devises,
        }
        return render(request,'gestion_document_app/Devise.djt',context=context) 


@login_required(login_url='/accounts/Login/')
def add_devise_handler(request):
    
    if request.method=="GET":
        form=DeviseForm()
        context={
        "form":form,
        }
        return render(request,'gestion_document_app/AddDevise.djt',context=context)
    elif request.method=="POST":
        form=DeviseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('devise')
        else:
            context={
            "form":form
            }   
            return render(request,'gestion_document_app/AddDevise.djt',context=context)

@login_required(login_url='/accounts/Login/')
def delete_devise_handler(request,_id):
    if request.method=="POST":
        doc=Devise.objects.get(devise_id=_id)
        doc.delete()
        return redirect('devise')


@login_required(login_url='/accounts/Login/')
def update_devise_handler(request,_id):

    if request.method=="GET":
        doc=Devise.objects.get(devise_id=_id)
        form=DeviseForm(initial={
            'devise_id': doc.devise_id,
            "devise_intitule":doc.devise_intitule,
            })
        context={
        "form":form
        }
        return render(request,'gestion_document_app/UpdateDevise.djt',context=context)
    elif request.method=="POST":
       
        form=DeviseForm(request.POST)
        doc=Devise.objects.get(devise_id=_id)
        
        if doc.devise_id==int(form.data['devise_id']):
            doc.devise_id=form.data['devise_id']
            doc.devise_intitule=form.data['devise_intitule']
            doc.save()
            return redirect('devise')
        else:
            doc=Devise.objects.get(devise_id=_id)
            doc.delete()
            form.save()
            return redirect('devise')

@csrf_exempt
def delete_many_devise(request):
    if request.method=="POST":
        docs=json.loads(request.body)
        for doc in docs["todelete"]:
            doc=Devise.objects.get(devise_id=doc)
            doc.delete()
        return redirect('devise')





#famille
@login_required(login_url='/accounts/Login/')
def famille_handler(request):
    form=FamilleForm()
    if request.method=="GET":
        familles=Famille.objects.all()
        context={
        "familles":familles,
        }
        return render(request,'gestion_document_app/Famille.djt',context=context) 


@login_required(login_url='/accounts/Login/')
def add_famille_handler(request):
    
    if request.method=="GET":
        form=FamilleForm()
        context={
        "form":form,
        }
        return render(request,'gestion_document_app/AddFamille.djt',context=context)
    elif request.method=="POST":
        form=FamilleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('famille')
        else:
            context={
            "form":form
            }   
            return render(request,'gestion_document_app/AddFamille.djt',context=context)

@login_required(login_url='/accounts/Login/')
def delete_famille_handler(request,_id):
    if request.method=="POST":
        doc=Famille.objects.get(famille_id=_id)
        doc.delete()
        return redirect('famille')

@login_required(login_url='/accounts/Login/')
def update_famille_handler(request,_id):

    if request.method=="GET":
        doc=Famille.objects.get(famille_id=_id)
        form=FamilleForm(initial={
            'famille_id': doc.famille_id,
            "famille_intitule":doc.famille_intitule,
            })
        context={
        "form":form
        }
        return render(request,'gestion_document_app/UpdateFamille.djt',context=context)
    elif request.method=="POST":
       
        form=FamilleForm(request.POST)
        doc=Famille.objects.get(famille_id=_id)
        
        if doc.famille_id==int(form.data['famille_id']):
            doc.famille_id=form.data['famille_id']
            doc.famille_intitule=form.data['famille_intitule']
            doc.save()
            return redirect('famille')
        else:
            doc=Famille.objects.get(famille_id=_id)
            doc.delete()
            form.save()
            return redirect('famille')

@csrf_exempt
def delete_many_famille(request):
    if request.method=="POST":
        docs=json.loads(request.body)
        for doc in docs["todelete"]:
            doc=Famille.objects.get(famille_id=doc)
            doc.delete()
        return redirect('devise')



#fornissuer
@login_required(login_url='/accounts/Login/')
def fournisseur_handler(request):
    form=FournisseurForm()
    if request.method=="GET":
        fournisseurs=Fournisseur.objects.all()
        context={
        "fournisseurs":fournisseurs,
        }
        return render(request,'gestion_document_app/Fournisseur.djt',context=context) 


@login_required(login_url='/accounts/Login/')
def add_fournisseur_handler(request):
    
    if request.method=="GET":
        form=FournisseurForm()
        context={
        "form":form,
        }
        return render(request,'gestion_document_app/AddFournisseur.djt',context=context)
    elif request.method=="POST":
        form=FournisseurForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('fournisseur')
        else:
            context={
            "form":form
            }   
            return render(request,'gestion_document_app/AddFournisseur.djt',context=context)

@login_required(login_url='/accounts/Login/')
def delete_fournisseur_handler(request,_id):
    if request.method=="POST":
        doc=Fournisseur.objects.get(fournisseur_id=_id)
        doc.delete()
        return redirect('fournisseur')

@login_required(login_url='/accounts/Login/')
def update_fournisseur_handler(request,_id):

    if request.method=="GET":
        doc=Fournisseur.objects.get(fournisseur_id=_id)
        form=FournisseurForm(initial={
            'fournisseur_id': doc.fournisseur_id,
            "fournisseur_intitule":doc.fournisseur_intitule,
            "fournisseur_adresse":doc.fournisseur_adresse,
            "fournisseur_telephone":doc.fournisseur_telephone,
            "fournisseur_email":doc.fournisseur_email
            })
        context={
        "form":form
        }
        return render(request,'gestion_document_app/UpdateFournisseur.djt',context=context)
    elif request.method=="POST":
       
        form=FournisseurForm(request.POST)
        doc=Fournisseur.objects.get(fournisseur_id=_id)
        
        if doc.fournisseur_id==int(form.data['fournisseur_id']):
            doc.fournisseur_id=form.data['fournisseur_id']
            doc.fournisseur_intitule=form.data['fournisseur_intitule']
            doc.fournisseur_adresse=form.data['fournisseur_adresse']
            doc.fournisseur_telephone=form.data['fournisseur_telephone']
            doc.fournisseur_email=form.data['fournisseur_email']
            doc.save()
            return redirect('fournisseur')
        else:
            doc=Fournisseur.objects.get(fournisseur_id=_id)
            doc.delete()
            form.save()
            return redirect('fournisseur')

@csrf_exempt
def delete_many_fournisseur(request):
    if request.method=="POST":
        docs=json.loads(request.body)
        for doc in docs["todelete"]:
            doc=Fournisseur.objects.get(fournisseur_id=doc)
            doc.delete()
        return redirect('fournisseur')




#Departement
@login_required(login_url='/accounts/Login/')
def departement_handler(request):
    form=DepartementForm()
    if request.method=="GET":
        departements=Departement.objects.all()
        context={
        "departements":departements,
        }
        return render(request,'gestion_document_app/Departement.djt',context=context) 


@login_required(login_url='/accounts/Login/')
def add_departement_handler(request):
    
    if request.method=="GET":
        form=DepartementForm()
        context={
        "form":form,
        }
        return render(request,'gestion_document_app/AddDepartement.djt',context=context)
    elif request.method=="POST":
        form=DepartementForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('departement')
        else:
            context={
            "form":form
            }   
            return render(request,'gestion_document_app/AddDepartement.djt',context=context)

@login_required(login_url='/accounts/Login/')
def delete_departement_handler(request,_id):
    if request.method=="POST":
        doc=Departement.objects.get(departement_id=_id)
        doc.delete()
        return redirect('departement')

@login_required(login_url='/accounts/Login/')
def update_departement_handler(request,_id):

    if request.method=="GET":
        doc=Departement.objects.get(departement_id=_id)
        form=DepartementForm(initial={
            'departement_id': doc.departement_id,
            "departement_intitule":doc.departement_intitule,
            })
        context={
        "form":form
        }
        return render(request,'gestion_document_app/UpdateDepartement.djt',context=context)
    elif request.method=="POST":
       
        form=DepartementForm(request.POST)
        doc=Departement.objects.get(departement_id=_id)
        
        if doc.departement_id==form.data['departement_id']:
            doc.departement_id=form.data['departement_id']
            doc.departement_intitule=form.data['departement_intitule']
            doc.save()
            return redirect('departement')
        else:
            doc=Departement.objects.get(departement_id=_id)
            doc.delete()
            form.save()
            return redirect('departement')

@csrf_exempt
def delete_many_departement(request):
    if request.method=="POST":
        docs=json.loads(request.body)
        for doc in docs["todelete"]:
            doc=Departement.objects.get(departement_id=doc)
            doc.delete()
        return redirect('departement')




#continue crud function simllier to above
def document_handler(request):
   pass
#continue crud function simllier to above
def validation_handler(request):
    pass

#continue crud function simllier to above
def suivalidation_handler(request):
    pass