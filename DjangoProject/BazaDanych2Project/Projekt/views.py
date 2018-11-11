from django.shortcuts import render
from django.http import HttpResponse

from django.template import loader
from Projekt.models import Books, Assortment

def index(request):
    #all_books = Books.objects.all()
    all_books = Assortment.objects.all()
    #template = loader.get_template('Projekt/index.html')
    context = {
        'all_books' : all_books,
    }
    return render(request, 'Projekt/index.html', context)
