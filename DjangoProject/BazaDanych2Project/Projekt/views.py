from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.http import HttpResponseRedirect

from .models import Assortment, Cart, Customer
from .forms import SignUpForm


def index(request):
    all_books = Assortment.objects.all()
    context = {
        'all_books': all_books,
    }
    return render(request, 'Projekt/main_page.html', context)


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('/home/')
    else:
        form = SignUpForm()
    return render(request, 'Projekt/signup.html', {'form': form})


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

    return HttpResponseRedirect("/home/#ID" + assortment_id)






