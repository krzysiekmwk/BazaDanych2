from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.http import HttpResponseRedirect

from .models import Assortment, Cart, CompletedCart
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

def cart(request):
    customer = getattr(request, 'user', None)
    all_books_in_user_cart = Cart.objects.all().filter(customer=customer.username)
    context = {
        'all_books_in_user_cart': all_books_in_user_cart,
    }
    return render(request, 'Projekt/cart.html', context)

def confirm_order(request):
    print("confirm")
    customer = getattr(request, 'user', None)
    all_item_in_cart = Cart.objects.all().filter(customer=customer.username)

    for item in all_item_in_cart:
        completed_cart = CompletedCart()
        completed_cart.assortment = item.assortment
        completed_cart.amount = item.amount
        completed_cart.total_price = item.total_price
        completed_cart.customer = item.customer
        completed_cart.save()

        assortment = Assortment.objects.get(id=item.assortment.id)
        assortment.amount -= item.amount
        assortment.save()

        item.delete()

    return HttpResponseRedirect("/home/#ID" + str(1))

def edit_order(request):
    print("EDIT")
    index = 1
    if (request.POST.get("ID_DELETE")):
        id = request.POST.get("ID_DELETE")
        index = id
        cart = Cart.objects.get(id=id)
        cart.delete()
    elif(request.POST.get("ID_ONE_MORE")):
        id = request.POST.get("ID_ONE_MORE")
        index = id
        cart = Cart.objects.get(id=id)
        cart.amount += 1
        cart.total_price = cart.amount * cart.assortment.price
        cart.save()
    elif(request.POST.get("ID_ONE_LESS")):
        id = request.POST.get("ID_ONE_LESS")
        index = id
        cart = Cart.objects.get(id=id)
        if(not cart.amount <= 1):
            cart.amount -= 1
            cart.total_price = cart.amount * cart.assortment.price
            cart.save()

    return HttpResponseRedirect("/home/cart/#ID" + str(index))

def add_to_cart(request):
    print("ELL")
    assortment_id = request.POST.get("ID")
    assortment = Assortment.objects.get(id=assortment_id)
    customer = getattr(request, 'user', None)
    print(customer.username)
    try:
        actual_cart = Cart.objects.get(assortment=assortment, customer=customer.username)
        actual_cart.amount = actual_cart.amount + 1
        actual_cart.total_price += assortment.price
        actual_cart.save()
    except Cart.DoesNotExist:
        cart = Cart()
        cart.assortment = assortment
        cart.customer = customer.username
        cart.amount = 1
        cart.total_price = assortment.price
        cart.save()
    return HttpResponseRedirect("/home/#ID" + assortment_id)






