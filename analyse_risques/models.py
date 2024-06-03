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
    type_actif = models.ForeignKey(TypeActif, on_delete=models.CASCADE)
    nom_actif = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    valeur_unitaire_actif = models.IntegerField()
    cout_installation = models.IntegerField()
    cout_entretien = models.IntegerField()
    va = models.IntegerField()
    valeur_indisponibilite = models.IntegerField()
    menaces = models.ManyToManyField('Menace', through='ActifMenace')
    
    def __str__(self):
        return f"{self.nom_actif}"

    
class Menace(models.Model):
    nom_menace = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    vulnerabilte = models.ManyToManyField('Vunlerabilite')


class Vunlerabilite(models.Model):
    nom = models.CharField(max_length=200)
    code_cve = models.CharField(max_length=20, unique=True)
    description = models.TextField() 
    
    def __str__(self):
        return f"{self.code_cve}"

class ActifMenace(models.Model):
    actif = models.ForeignKey(Asset, on_delete=models.CASCADE)
    menace = models.ForeignKey(Menace, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.actif} - {self.menace}"


class EvaluationRisque(models.Model):		 		
    actif = models.ForeignKey(Asset, on_delete=models.CASCADE)	
    menaces = models.ForeignKey(Menace, null=True, blank=True, on_delete=models.CASCADE)	
    vulnerabilite = models.ForeignKey(Vunlerabilite, on_delete=models.CASCADE) 
    risque = models.CharField(max_length=200)
    probabilite_occurrence = models.FloatField()
    impact_c = models.IntegerField()
    impact_i = models.IntegerField()
    impact_d = models.IntegerField()
    criticite = models.IntegerField()

    def __str__(self):
        return f"{self.actif}"
