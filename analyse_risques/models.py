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
    Valeur_unitaire_actif = models.IntegerField()
    Cout_installation = models.IntegerField()
    Cout_entretien = models.IntegerField()
    VA = models.IntegerField()
    Valeur_indisponibilité = models.IntegerField()
    
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
    Vulnérabilité = models.ForeignKey(Vunlerabilite, on_delete=models.CASCADE)
    Menaces = models.CharField(max_length=200) 
    Risque = models.CharField(max_length=200)
    Probabilité_occurrence = models.FloatField(max_length=200)
    Impact_C = models.FloatField(max_length=200)
    Impact_I = models.FloatField(max_length=200)
    Impact_D = models.FloatField(max_length=200)
    Criticité = models.FloatField(max_length=200)

    def __str__(self):
        return self.actif