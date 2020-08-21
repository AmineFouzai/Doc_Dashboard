from django.db import models


class Depot(models.Model):
    numero_depot = models.IntegerField(primary_key=True)
    intitule_depot = models.CharField(max_length=100)
    def __str__(self):
            return str(self.numero_depot)+","+(self.intitule_depot)
    def __unicode__(self):
        return self.numero_depot

class Article(models.Model):
    article_id = models.IntegerField(primary_key=True)
    article_ref = models.CharField(max_length=20)
    article_design = models.CharField(max_length=100)
    prix_achat = models.IntegerField()
    def __str__(self):
            return str(self.article_id)+","+(self.article_ref)
    def __unicode__(self):
        return self.article_id

class Famille(models.Model):
    famille_id = models.IntegerField(primary_key=True)
    famille_intitule = models.CharField(max_length=100)
    def __str__(self):
            return str(self.famille_id)+","+(self.famille_intitule)
    def __unicode__(self):
        return self.famille_id

class Departement(models.Model):
    departement_id = models.CharField(primary_key=True,max_length=20)
    departement_intitule = models.CharField(max_length=20)
    def __str__(self):
            return str(self.departement_id)+","+(self.departement_intitule)
    def __unicode__(self):
        return self.departement_id

class Fournisseur(models.Model):
    fournisseur_id = models.IntegerField(primary_key=True)
    fournisseur_intitule = models.CharField(max_length=20)
    fournisseur_adresse = models.CharField(max_length=20)
    fournisseur_telephone = models.CharField(max_length=20)
    fournisseur_email = models.CharField(max_length=20)
    def __str__(self):
        return str(self.fournisseur_id)+","+(self.fournisseur_intitule)
    def __unicode__(self):
        return self.fournisseur_id

class Devise(models.Model):
    devise_id = models.IntegerField(primary_key=True)
    devise_intitule = models.CharField(max_length=20)
    def __str__(self):
        return self.devise_intitule
    def __unicode__(self):
        return self.devise_id

class Document(models.Model):
    document_id=models.IntegerField(primary_key=True)
    document_piece=models.CharField(max_length=100)
    document_type=models.IntegerField(default=11)#11 demande   12 d achat  16 facture 
    document_date=models.DateField()
    fournisseur_id=models.ForeignKey(Fournisseur,on_delete=models.CASCADE)
    document_devise=models.ForeignKey(Devise,on_delete=models.CASCADE)
    document_reference=models.CharField(max_length=100)
    document_validation1=models.BooleanField(default=False)
    document_validation2=models.BooleanField(default=False)
    #on scond change
    numero_depot=models.ForeignKey(Depot,on_delete=models.CASCADE,null=True)
    document_date_livraison = models.DateTimeField(null=True)
    document_cours = models.DecimalField(max_digits=6, decimal_places=2, null=True)
    departement_id= models.ForeignKey(Departement,on_delete=models.CASCADE,null=True)

    #on third change
    article_id =models.ForeignKey(Article,on_delete=models.CASCADE,null=True)
    document_P_U_HT = models.FloatField(default=0,null=True)
    document_P_U_DEV = models.FloatField(default=0,null=True)
    document_QT = models.IntegerField(default=0,null=True)
    document_taxe = models.FloatField(default=0, null=True)
    document_remise = models.FloatField(default=0, null=True)
    document_MT_HT = models.FloatField( default=0,null=True)
    document_MT_TTC = models.FloatField(default=0, null=True)

    def calculate_formula(self,prix):
        self.document_P_U_HT =float(self.document_QT)*float(prix) 
        self.document_MT_HT = float(self.document_P_U_HT) 
        self.document_MT_TTC=float(self.document_MT_HT)+float(self.document_P_U_HT)*float(self.document_taxe)/100


