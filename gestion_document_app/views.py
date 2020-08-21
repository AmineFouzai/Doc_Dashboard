from django.shortcuts import render,redirect 
from django.contrib.auth.decorators import login_required
from bokeh.plotting import figure
from bokeh.embed import components
from bokeh.palettes import Category20c
from bokeh.transform import cumsum
import pandas as pd

from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.contrib.auth.models import User
import json
from .forms import *
# Create your views here.

@login_required(login_url='/accounts/Login/')
def index_handler(request):
    if request.method=="GET":
        
        pls = ['Depot', 'Devise', 'Departement', 'Fournisseur', 'Article', 'Famille']
        nb_users=User.objects.all().count()
        users=User.objects.all()
        documents=Document.objects.all().count()
        valids=0
        for valid in Document.objects.all():
            if valid.document_validation1 and valid.document_validation2:
                valids=valids+1
        counts=[
            Depot.objects.all().count() if  Exception  else 0, 
            Devise.objects.all().count() if  Exception  else 0,
            Departement.objects.all().count() if  Exception  else 0,
            Fournisseur.objects.all().count() if  Exception  else 0,
            Article.objects.all().count() if  Exception  else 0,
            Famille.objects.all().count() if  Exception  else 0,
        ]
        #bar plot
        p = figure(x_range=pls, plot_height=100, title="Statistics",toolbar_location=None, tools="")
        p.vbar(x=pls, top=counts, width=0.9)
        p.xgrid.grid_line_color = None
        p.y_range.start = 0
        p.plot_width = 700
        p.plot_height = 400
        script,div=components(p)
        #pie plot

        x={
            'Depot':Depot.objects.all().count() if  Exception  else 0, 
            'Devise':Devise.objects.all().count() if  Exception  else 0,
            'Departement':Departement.objects.all().count() if  Exception  else 0,
            'Fournisseur':Fournisseur.objects.all().count() if  Exception  else 0,
            'Article':Article.objects.all().count() if  Exception  else 0,
            'Famille':Famille.objects.all().count() if  Exception  else 0,
        }
        data = pd.Series(x).reset_index(name='value').rename(columns={'index':'structure'})
        data['angle'] = data['value']/data['value'].sum() * 2*3.14
        data['color'] = Category20c[len(x)]

        pie = figure(plot_height=350, title="Pie Chart", toolbar_location="left",
           tooltips="@structure: @value", x_range=(-0.5, 1.0))

        pie.wedge(x=0, y=1, radius=0.4,
            start_angle=cumsum('angle', include_zero=True), end_angle=cumsum('angle'),
            line_color="white", fill_color='color', legend_field='structure', source=data)

        pie.axis.axis_label=None
        pie.axis.visible=False
        pie.grid.grid_line_color = None
        pie.plot_width = 360
        pie.plot_height = 300
        script2,div2=components(pie)
        context={
            "script":script,
            "div":div,
            "counts":counts,
            "nb_users":nb_users,
            "documents":documents,
            "valids":valids,
            "users":users,
            "script2":script2,
            "div2":div2
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


#user handlers
def user_handler(request):

    if request.method=="GET":    
        users=User.objects.all()
        context={
        "users":users,
        "is_admin":request.user.is_superuser,
        "current_user":request.user.id
        }
        return render(request,'gestion_document_app/Users.djt',context=context) 


@login_required(login_url='/accounts/Login/')
def add_user_handler(request):
    
    if request.method=="GET":
        form=UserCreateForm()
        context={
        "form":form,
        }
        return render(request,'gestion_document_app/AddUser.djt',context=context)
    elif request.method=="POST":
        
        
        form=UserCreateForm(data=request.POST)
        if form.is_valid():
            if request.POST.get("staff") =="on":
                user=form.save()
                user=User.objects.get(username=user.username)
                user.is_superuser=True
                user.is_staff=True
                User.save(user)
                return redirect('users')
            else:
                user=form.save()
                return redirect('users')
        else:
            context={
            "form":form,
            "error":True
            }   
            return render(request,'gestion_document_app/AddUser.djt',context=context)


@login_required(login_url='/accounts/Login/')
def delete_user_handler(request,_id):
    if request.method=="POST":
        user=User.objects.get(id=_id)
        user.delete()
        return redirect('users')
        


#document handlers
@login_required(login_url='/accounts/Login/')
def document_handler(request):
    
    if request.method=="GET":    
        documents=Document.objects.all()
        context={
        "documents":documents
        }
        return render(request,'gestion_document_app/Document.djt',context=context) 


@login_required(login_url='/accounts/Login/')
def add_document_handler(request):
    
    if request.method=="GET":
        form=DocumentForm()
        context={
        "form":form,
        }
        return render(request,'gestion_document_app/AddDocument.djt',context=context)

    elif request.method=="POST":
        form=DocumentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('document')
        else:
            context={
            "form":form
            }   
            return render(request,'gestion_document_app/AddDocument.djt',context=context)

@login_required(login_url='/accounts/Login/')
def delete_document_handler(request,_id):
    if request.method=="POST":
        doc=Document.objects.get(document_id=_id)
        doc.delete()
        return redirect('document')

@login_required(login_url='/accounts/Login/')
def update_document_handler(request,_id):

    if request.method=="GET":
        doc=Document.objects.get(document_id=_id)
        if not doc.document_validation1  and not doc.document_validation2:
            form=DocumentForm(initial={
                'document_id': doc.document_id,
                "document_piece":doc.document_piece,
                "document_type":doc.document_type,
                "document_date":doc.document_date,
                "fournisseur_id":doc.fournisseur_id,
                "document_devise":doc.document_devise,
                "document_reference":doc.document_reference,
                })
            # form.fields['document_id'].disabled=True
            
        elif doc.document_validation1==False and doc.document_validation2==True or doc.document_validation1==True and  doc.document_validation2==False:
            form=DocumentFormValid1(
                initial={
                'document_id': doc.document_id,
                "numero_depot":doc.numero_depot,
                "document_date_livraison":doc.document_date_livraison,
                "document_cours":doc.document_cours,
                "departement_id":doc.departement_id
                }
            )
            # form.fields['document_id'].disabled=True
            
        elif doc.document_validation1 and doc.document_validation2:
            form=DocumentFormValid2(
                initial={
                'document_id': doc.document_id
                }
            )
            # form.fields['document_id'].disabled=True
            
        context={
        "form":form
        }
        return render(request,'gestion_document_app/UpdateDocument.djt',context=context)

    elif request.method=="POST":
       
        doc=Document.objects.get(document_id=_id)
        if not doc.document_validation1  and not doc.document_validation2:
                form=DocumentForm(data=request.POST)
                doc.document_id=form.data['document_id']
                doc.document_piece=form.data['document_piece']
                doc.document_type=form.data['document_type']
                doc.document_date=form.data['document_date']
                doc.fournisseur_id=Fournisseur.objects.get(fournisseur_id=form.data['fournisseur_id'])
                doc.document_devise=form.data['document_devise']
                doc.document_reference=form.data['document_reference']
                doc.save()
                return redirect('document')
            
        elif doc.document_validation1==False and doc.document_validation2==True or doc.document_validation1==True and  doc.document_validation2==False:
               form=DocumentFormValid1(data=request.POST)
               doc.numero_depot=Depot.objects.get(numero_depot=form.data['numero_depot'])
               doc.document_date_livraison=form.data['document_date_livraison']
               doc.document_cours=form.data['document_cours']
               doc.departement_id=Departement.objects.get(departement_id=form.data['departement_id'])
               doc.save()
               return redirect('document')
            
        elif doc.document_validation1 and doc.document_validation2:
                form=DocumentFormValid2(data=request.POST)
                article=Article.objects.get(article_id=form.data['article_id'])
                doc.article_id=article
                doc.document_P_U_DEV=form.data['document_P_U_DEV']
                doc.document_QT=form.data['document_QT']
                doc.document_taxe=form.data['document_taxe']
                doc.document_remise=form.data['document_remise']
                doc.calculate_formula(article.prix_achat)
                doc.save()
                return redirect('document')
            
@csrf_exempt
def delete_many_document(request):
    if request.method=="POST":
        docs=json.loads(request.body)
        for doc in docs["todelete"]:
            doc=Document.objects.get(document_id=doc)
            doc.delete()
        return redirect('document')





@login_required(login_url='/accounts/Login/')
def document_validation_handler(request):
    
    if request.method=="GET":    
        documents=Document.objects.all()
        context={
        "documents":documents
        }
        return render(request,'gestion_document_app/Validation.djt',context=context) 

@login_required(login_url='/accounts/Login')
def confirm_document_validation1_handler(request,_id):
    if request.method=="GET":
        doc=Document.objects.get(document_id=_id)
        doc.document_validation1=True
        if doc.document_type==11:
            doc.document_type=12
        elif doc.document_type==12:
            doc.document_type=16

        doc.save()
        return redirect('validation')

@login_required(login_url='/accounts/Login')
def cancel_document_validation1_handler(request,_id):
    if request.method=="GET":
        doc=Document.objects.get(document_id=_id)
        doc.document_validation1=False
        if doc.document_type==12:
            doc.document_type=11
        elif doc.document_type==16:
            doc.document_type=12
        doc.save()
        return redirect('validation')



@login_required(login_url='/accounts/Login')
def confirm_document_validation2_handler(request,_id):
    if request.method=="GET":
        doc=Document.objects.get(document_id=_id)
        doc.document_validation2=True
        if doc.document_type==11:
            doc.document_type=12
        elif doc.document_type==12:
            doc.document_type=16
        doc.save()
        return redirect('validation')

@login_required(login_url='/accounts/Login')
def cancel_document_validation2_handler(request,_id):
    if request.method=="GET":
        doc=Document.objects.get(document_id=_id)
        doc.document_validation2=False
        if doc.document_type==12:
            doc.document_type=11
        elif doc.document_type==16:
            doc.document_type=12

        doc.save()
        return redirect('validation')


def read_document_info(request,_id):
    if request.method=="GET":
        doc=Document.objects.get(document_id=_id)
        context={
            "doc":doc
        }
        return render(request,'gestion_document_app/ReadDocument.djt',context=context) 



