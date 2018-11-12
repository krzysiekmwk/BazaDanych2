from django.shortcuts import render

from .models import Assortment, Cart, Customer
from django.http import HttpResponseRedirect


def index(request):
    all_books = Assortment.objects.all()
    context = {
        'all_books': all_books,
    }
    return render(request, 'Projekt/index.html', context)


def add_to_cart(request):
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

    return HttpResponseRedirect("/#ID" + assortment_id)


