from django.db import models

# Create your models here.
class TypeActif(models.Model):
    class Meta:
        verbose_name = "Type d'actif"
        
    nom = models.CharField(max_length=100)
    
    def __str__(self):
        return f"{self.nom}"

class Asset(models.Model):
    class Meta:
        verbose_name = "Actif"
    actif = models.ForeignKey(TypeActif, on_delete=models.CASCADE)
    description = models.CharField(max_length=200)
    valeur_unitaire_actif = models.IntegerField()
    cout_installation = models.IntegerField()
    cout_entretien = models.IntegerField()
    va = models.IntegerField()
    valeur_indisponibilite = models.IntegerField()
    
    def __str__(self):
        return f"{self.actif}"


class Vunlerabilite(models.Model):
    nom = models.CharField(max_length=200)
    description = models.TextField()
    type_actif = models.ForeignKey(TypeActif, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.nom}"
    

class Analyse(models.Model):		 		
    actif = models.ForeignKey(Asset, on_delete=models.CASCADE)		
    vulnerabilite = models.ForeignKey(Vunlerabilite, on_delete=models.CASCADE)
    menaces = models.CharField(max_length=200) 
    misque = models.CharField(max_length=200)
    probabilite_occurrence = models.FloatField(max_length=200)
    impact_c = models.FloatField(max_length=200)
    impact_i = models.FloatField(max_length=200)
    impact_d = models.FloatField(max_length=200)
    criticite = models.FloatField(max_length=200)

    def __str__(self):
        return self.actif
