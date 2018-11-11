from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.shortcuts import redirect

from django.template import loader
from Projekt.models import Books, Assortment, Cart, Customer
from django.http import HttpResponse, HttpResponseNotFound, Http404,  HttpResponseRedirect


def index(request):
    #all_books = Books.objects.all()
    all_books = Assortment.objects.all()
    #template = loader.get_template('Projekt/index.html')
    context = {
        'all_books' : all_books,
    }
    return render(request, 'Projekt/index.html', context)


def addToCart(request):
    print("ELL")
    assortment_id = request.POST.get("ID")
    assortment = Assortment.objects.get(id=assortment_id)
    customer = Customer.objects.get(id=1)

    try:
        actual_cart = Cart.objects.get(assortment=assortment, customer=customer)
        actual_cart.amount = actual_cart.amount + 1
        actual_cart.save()
    except Cart.DoesNotExist:
        cart = Cart()
        cart.assortment = assortment
        cart.customer = customer
        cart.amount = 1
        cart.save()

    return HttpResponseRedirect("/Projekt/#ID" + assortment_id)


