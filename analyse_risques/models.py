from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver

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

    def __str__(self):
        return f"{self.nom_menace}"

class Domaine(models.Model):
    nom_domaine = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.nom_domaine}"
    
class Vunlerabilite(models.Model):
    nom = models.CharField(max_length=200)
    code_cve = models.CharField(max_length=20, unique=True)
    description = models.TextField() 
    domaine = models.ForeignKey(Domaine, on_delete=models.SET_NULL, null=True, blank=True)
    
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
    facteur_exposition = models.DecimalField(max_digits=4, decimal_places=2)
    probabilite_occurrence = models.DecimalField(max_digits=3, decimal_places=2) #ou ARO(Annual rate of occurence)
    sle = models.FloatField(default=0) #facteur_expostion * valeur_actif
    impact_c = models.IntegerField(null=True, blank=True) #SLE*ARO
    impact_i = models.IntegerField(null=True, blank=True)
    impact_d = models.IntegerField(null=True, blank=True)
    criticite = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return f"{self.actif}"

    def save(self, *args, **kwargs):
        #nommer le risque
        self.risque = str(self.actif.nom_actif) + "-R" + str(self.id)
        # Effectuer les calculs avant l'enregistrement
        self.sle = float(self.facteur_exposition/100) * self.actif.va  # Assurez-vous que "valeur" est le champ approprié pour la valeur de l'actif
        print(self.vulnerabilite.domaine)
        if str(self.vulnerabilite.domaine) == 'Confidentialité':
            self.impact_c = int(self.sle * float(self.probabilite_occurrence))
        elif str(self.vulnerabilite.domaine) == 'Integrité':
            self.impact_i = int(self.sle * float(self.probabilite_occurrence))
        else:
            self.impact_d = int(self.sle * float(self.probabilite_occurrence))

        # Appeler la méthode save() originale pour enregistrer l'objet
        super(EvaluationRisque, self).save(*args, **kwargs)
 