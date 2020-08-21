from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.http import HttpResponse

urlpatterns=[
    path('',views.index_handler,name='index'),
    path('depot/',views.depot_handler,name='depot'),
    path('depot/<int:_id>',views.delete_depot_handler,name='delete_depot'),
    path('depot/add',views.add_depot_handler,name="add_depot"),
    path('depot/udpate/<int:_id>',views.update_depot_handler,name="update_depot"),
    path('depot/deletemany',views.delete_many_depot),

    path('article/',views.article_handler,name='article'),
    path('article/<int:_id>',views.delete_article_handler,name='delete_article'),
    path('article/add',views.add_article_handler,name="add_article"),
    path('article/udpate/<int:_id>',views.update_article_handler,name="update_article"),
    path('article/deletemany',views.delete_many_article),
      
    path('devise/',views.devise_handler,name='devise'),
    path('devise/<int:_id>',views.delete_devise_handler,name='delete_devise'),
    path('devise/add',views.add_devise_handler,name="add_devise"),
    path('devise/udpate/<int:_id>',views.update_devise_handler,name="update_devise"),
    path('devise/deletemany',views.delete_many_devise),

    path('famille/',views.famille_handler,name='famille'),
    path('famille/<int:_id>',views.delete_famille_handler,name='delete_famille'),
    path('famille/add',views.add_famille_handler,name="add_famille"),
    path('famille/udpate/<int:_id>',views.update_famille_handler,name="update_famille"),
    path('famille/deletemany',views.delete_many_famille),
    
    path('fournisseur/',views.fournisseur_handler,name='fournisseur'),
    path('fournisseur/<int:_id>',views.delete_fournisseur_handler,name='delete_fournisseur'),
    path('fournisseur/add',views.add_fournisseur_handler,name="add_fournisseur"),
    path('fournisseur/udpate/<int:_id>',views.update_fournisseur_handler,name="update_fournisseur"),
    path('fournisseur/deletemany',views.delete_many_fournisseur),
    
    path('departement/',views.departement_handler,name='departement'),
    path('departement/add',views.add_departement_handler,name="add_departement"),
    path('departement/udpate/<str:_id>',views.update_departement_handler,name="update_departement"),
    path('departement/<str:_id>',views.delete_departement_handler,name='delete_departement'),
    path('departement/deletemany/all',views.delete_many_departement),


    path('document/',views.document_handler,name="document"),
    path('document/add',views.add_document_handler,name="add_document"),
    path('document/<int:_id>',views.delete_document_handler,name='delete_document'),
    path('document/udpate/<int:_id>',views.update_document_handler,name="update_document"),
    path('document/deletemany',views.delete_many_document),
    path('document/get/<int:_id>',views.read_document_info,name="details"),

    path('validation/',views.document_validation_handler,name="validation"),
    path('validation/confirm1/<int:_id>',views.confirm_document_validation1_handler,name="confirm1"),
    path('validation/cancel1/<int:_id>',views.cancel_document_validation1_handler,name="cancel1"),
    path('validation/confirm2/<int:_id>',views.confirm_document_validation2_handler,name="confirm2"),
    path('validation/cancel2/<int:_id>',views.cancel_document_validation2_handler,name="cancel2"),


    path('users/',views.user_handler,name="users"),
    path('users/add',views.add_user_handler,name="add_users"),
    path('users/<int:_id>',views.delete_user_handler,name='delete_user'),
    

 
]+staticfiles_urlpatterns()