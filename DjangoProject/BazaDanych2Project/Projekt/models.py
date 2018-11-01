from django.db import models


class Books(models.Model):
    ISBN = models.IntegerField()
    title = models.CharField(max_length=250)   # tytul
    author = models.CharField(max_length=250)   # autor
    publishing_house = models.CharField(max_length=250) # wydawnictwo
    genre = models.CharField(max_length=250)    # gatunek


class Assortment(models.Model):
    amount = models.IntegerField()  # ilosc na magazynie
    ISBN_CODE = models.ForeignKey(Books, on_delete=models.CASCADE)


class Customer(models.Model):
    first_name = models.CharField(max_length=250)   # imie
    last_name = models.CharField(max_length=250)    # nazwisko
    email = models.CharField(max_length=250)    # adres email
    tel_number = models.CharField(max_length=250)   # numer kontatkowy
    loyalty_card = models.BooleanField(default=True)    # karta lojalnosciowa


class JobTitle(models.Model):
    job_title = models.CharField(max_length=250)    # nazwa stanowiska


class Worker(models.Model):
    first_name = models.CharField(max_length=250)  # imie
    last_name = models.CharField(max_length=250)  # nazwisko
    email = models.CharField(max_length=250)  # adres email
    tel_number = models.CharField(max_length=250)
    salary = models.IntegerField()
    job_title = models.ForeignKey(JobTitle, on_delete=models.DO_NOTHING)


class Cart(models.Model):   # przechowuje aktualne przedmioty w koszyku
    assortment = models.ForeignKey(Assortment, on_delete=models.CASCADE)    # wybrany asortyment
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)    # klient
    amount = models.IntegerField()  # ilosc zakupionych przedmiotow


class CompletedCart(models.Model):  # przechowuje zrealizowane karty
    assortment = models.ForeignKey(Assortment, on_delete=models.CASCADE)  # wybrany asortyment
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)  # klient
    amount = models.IntegerField()  # ilosc zakupionych przedmiotow


class Order(models.Model):
    completed_order = models.ForeignKey(CompletedCart, on_delete=models.CASCADE)
    order_date = models.DateField()
    was_paid = models.BooleanField(default=True)    # czy zamowienie zostalo juz oplacone
    cash_on_delivery = models.BooleanField(default=True)    # czy platnosc za pobraniem
    was_ordered = models.BooleanField(default=True)  # czy zostalo zrealizowane
    total_amount = models.IntegerField()

