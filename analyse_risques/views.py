from django.shortcuts import render, redirect
from django.forms import modelformset_factory
from . import forms 
from .models import *

from django.contrib import messages

# Create your views here.
def home(request):
    form = forms.AssetForm()
    actifs = Asset.objects.all()
    message = ""
    errors = ''
    if request.method == 'POST':
        form = forms.AssetForm(request.POST)
        if form.is_valid():
            form.save()
            message = "Les actifs ont bien été enregistré"
            messages.success(request, message)
            return redirect('home')
    else:
        errors = form.errors
        
    context = {
        'form': form,
        'actifs': actifs
    }
        
    return render(request, "analyse_risques/AssetsList.html", context)

def vulnerabilite(request):
    actifs = Asset.objects.all()
    form = forms.AnalyseForm()

    if request.method == 'POST': 
        form = forms.AnalyseForm(request.POST)
        if form.is_valid():
            evaluation = form.save(commit=False) 
            evaluation.save()
            return redirect('vulnerabilite')
        else:
            print(form.errors)

    context = {
        'actifs': actifs,
        'form': form,
    }
    
    return render(request, "analyse_risques/analyse.html", context)

def exemple(request):
    return render(request, "exemple.html")