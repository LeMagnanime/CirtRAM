from django.shortcuts import render, redirect
from django.forms import modelformset_factory
from . import forms 
from .models import *

from django.contrib import messages

# Create your views here.
def home(request):
    AssetFormSet = modelformset_factory(Asset, form=forms.AssetForm, extra=2)
    message = ""
    if request.method == 'POST':
        formset = AssetFormSet(request.POST, queryset=Asset.objects.none())
        if formset.is_valid():
            formset.save()
            message = "Les actifs ont bien été enregistré"
            messages.success(request, message)
            return redirect('home')
    else:
        formset = AssetFormSet(queryset=Asset.objects.none())
        
    context = {
        'formset': formset,
    }
        
    return render(request, "analyse_risques/AssetsList.html", context)

def vulnerabilite(request):
    actifs = Asset.objects.all()
    formulaires = []
    
    for actif in actifs:
        form = forms.AnalyseForm(initial={'actif': actif})
        formulaires.append((actif, form))
    
    if request.method == 'POST':
        for actif, form in formulaires:
            form = forms.AnalyseForm(request.POST, initial={'actif': actif})
            if form.is_valid():
                form.save()
                return redirect('vulnerabilite')
            else:
                form.errors
    
    context = {
        'actifs':actifs,
        'formulaires': formulaires
    }
    
    return render(request, "analyse_risques/tableau_vulnerabilite.html", context)

def exemple(request):
    return render(request, "exemple.html")