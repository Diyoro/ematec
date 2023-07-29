from django.shortcuts import render
from .models import *
# Create your views here.

def index(request):
    context = {
        "header":Header.objects.last(),
        "petitmodels":PetitModel.objects.all(),
        "rowgx70":RowGx70.objects.last(),
        "partenaires":Partenaires.objects.all(),
        "section":Section.objects.last(),
        "professeur":Professeur.objects.all()
    }
    return render(request, 'user/index.html', context=context)

def about(request):
    return render(request, 'user/about.html')

def course(request):
    return render(request, 'user/course.html')

def contact(request):
    return render(request, 'user/contact.html')
