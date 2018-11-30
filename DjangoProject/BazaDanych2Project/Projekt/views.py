from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.http import HttpResponseRedirect

from .models import Assortment, Cart, CompletedCart
from .forms import SignUpForm
from django.contrib.auth.models import Group


def index(request):
    all_books = Assortment.objects.all()
    context = {
        'all_books': all_books,
    }
    return render(request, 'Projekt/main_page.html', context)


def salesman_details(request, id=0):
    user = getattr(request, 'user', None)
    if user.groups.filter(name='employee').exists():
        print("DETAILS")
        print(request)
        all_orders = CompletedCart.objects.all().filter(the_same_id=id)

        total_price = 0
        for order in all_orders:
            order.total_price = round(order.total_price, 2)
            total_price += order.total_price

        context = {
            'all_orders': all_orders,
            'total_price': round(total_price, 2),
        }

        return render(request, 'Projekt/salesman_details.html', context)
    else:
        return HttpResponseRedirect("/home/#ID" + str(1))

def salesman(request):
    user = getattr(request, 'user', None)
    if user.groups.filter(name='employee').exists():
        all_orders = CompletedCart.objects.all()

        list_with_the_same_ids = []
        filtered_orders = []

        for order in all_orders:
            if order.the_same_id not in list_with_the_same_ids:
                list_with_the_same_ids.append(order.the_same_id)
                filtered_orders.append(order)




        context = {
            'all_orders': filtered_orders,
        }
        return render(request, 'Projekt/salesman.html', context)
    else:
        return HttpResponseRedirect("/home/#ID" + str(1))




def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            my_group = Group.objects.get(name='user')
            my_group.user_set.add(user)
            login(request, user)
            return redirect('/home/')
    else:
        form = SignUpForm()
    return render(request, 'Projekt/signup.html', {'form': form})

def cart(request):
    customer = getattr(request, 'user', None)
    all_books_in_user_cart = Cart.objects.all().filter(customer=customer.username)
    total_price = 0
    for item in all_books_in_user_cart:
        item.total_price = round(item.total_price, 2)
        total_price += item.total_price
    context = {
        'all_books_in_user_cart': all_books_in_user_cart,
        'total_price': round(total_price, 2),
    }
    return render(request, 'Projekt/cart.html', context)

def confirm_order(request):
    print("confirm")
    customer = getattr(request, 'user', None)
    all_item_in_cart = Cart.objects.all().filter(customer=customer.username)

    the_same_id = 0
    for item in all_item_in_cart:
        completed_cart = CompletedCart()
        completed_cart.assortment = item.assortment
        completed_cart.amount = item.amount
        completed_cart.total_price = item.total_price
        completed_cart.customer = item.customer
        completed_cart.the_same_id = the_same_id
        completed_cart.save()
        if (the_same_id == 0):
            the_same_id = completed_cart.id

        completed_cart.the_same_id = the_same_id
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

    #return cart(request)
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






