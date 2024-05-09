from django.forms import ModelForm
from .models import *

#formulaire pour l'ajout des actifs
class AssetForm(ModelForm):
    class Meta:
        model = Asset
        fields = '__all__'

class AnalyseForm(ModelForm):
    class Meta:
        model = Analyse
        fields = '__all__'
           