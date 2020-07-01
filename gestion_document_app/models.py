from django.db import models


class Depot(models.Model):
    numero_depot = models.IntegerField(primary_key=True)
    intitule_depot = models.CharField(max_length=100)


class Article(models.Model):
    article_id = models.IntegerField(primary_key=True)
    article_ref = models.CharField(max_length=20)
    article_design = models.CharField(max_length=100)
    prix_achat = models.IntegerField()
   
    


# class F_DOCENTETE(models.Model):
#     DO_Ref = models.CharField(max_length=50)
#     DO_Date = models.DateTimeField()
#     DO_Piece = models.CharField(primary_key=True, max_length=20)
#     DO_Piece_orig = models.CharField(max_length=20, null=True)
#     DO_Devise = models.SmallIntegerField()
#     DO_Statut = models.SmallIntegerField()
#     DE_No = models.IntegerField()
#     DO_TYPE = models.IntegerField()
#     DO_DateLiv = models.DateTimeField(null=True)
#     DO_Cours = models.DecimalField(max_digits=6, decimal_places=2, null=True)
#     CD_DEP = models.CharField(max_length=20, null=True)
#     Objet = models.CharField(max_length=20, null=True)
#     FN_NUM = models.CharField(max_length=20, null=True)
#     # DO_TYPE = CompositeForeignKey(DO_TYPE, on_delete=CASCADE, to_fields={
    #     "tiers_id": "DO_TYPE",
    #     "DO_Piece": LocalFieldValue("DO_Piece"),
    #     "type_tiers": RawFieldValue("DE_No")
    #
    # })

    # class Meta:
    #     db_table = "f_docentete"
    #     unique_together = (('DO_Piece', 'DO_TYPE'),)



# class DETAILLE_DOCUMENT(models.Model):
#     DO_Statut = models.SmallIntegerField()
#     DO_Piece = models.CharField(max_length=20)
#     DO_TYPE = models.IntegerField()
#     DO_Date = models.DateTimeField()
#     FN_NUM = models.CharField(max_length=17)
#     DO_Devise = models.SmallIntegerField()
#     DO_Ref = models.CharField(max_length=50)
#     Stat = models.CharField(max_length=10)

#     class Meta:
#          db_table = "detaille_document"


# class F_DOCLIGNE(models.Model):
#      DL_NO = models.IntegerField(primary_key=True)
#      REF_Article = models.CharField(max_length=20)
#      Designation = models.CharField(max_length=20)
#      P_U_HT = models.DecimalField(max_digits=6, decimal_places=2, null=True)
#      P_U_DEV = models.DecimalField(max_digits=6, decimal_places=2, null=True)
#      QT = models.IntegerField()
#      DE_No = models.IntegerField()
#      QT_AT = models.IntegerField()
#      Taxe = models.DecimalField(max_digits=6, decimal_places=2, null=True)
#      DO_TYPE = models.IntegerField()
#      DO_Piece = models.CharField(max_length=20)
#      Remise = models.DecimalField(max_digits=6, decimal_places=2, null=True)
#      MT_HT = models.DecimalField(max_digits=6, decimal_places=2, null=True)
#      MT_TTC = models.DecimalField(max_digits=6, decimal_places=2, null=True)

#      class Meta:
#          db_table = "f_docligne"





# class F_ARTSTOCK(models.Model):
#     AR_Ref = models.CharField(max_length=20)
#     DE_No = models.IntegerField()

#     class Meta:
#      db_table = "f_artstock"



#to create
class Famille(models.Model):
     famille_id = models.IntegerField(primary_key=True)
     famille_intitule = models.CharField(max_length=100)



#to create
class Departement(models.Model):
    departement_id = models.CharField(primary_key=True,max_length=20)
    departement_intitule = models.CharField(max_length=20)






#to create
class Fournisseur(models.Model):
    fournisseur_id = models.IntegerField(primary_key=True)
    fournisseur_intitule = models.CharField(max_length=20)
    fournisseur_adresse = models.CharField(max_length=20)
    fournisseur_telephone = models.CharField(max_length=20)
    fournisseur_email = models.CharField(max_length=20)





class Devise(models.Model):
    devise_id = models.IntegerField(primary_key=True)
    devise_intitule = models.CharField(max_length=20)

