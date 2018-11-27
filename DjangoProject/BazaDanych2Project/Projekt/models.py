from django.db import models


# TODO
# AGREGACJA
# ZMIANA PANELU ADMINA
# UZUPELNIONA DOKUMENTACJA

class Books(models.Model):

    class Meta:
        verbose_name = "Book"
        verbose_name_plural = "Books"

    ISBN = models.IntegerField(unique=True)
    title = models.CharField(max_length=250)   # tytul
    author = models.CharField(max_length=250)   # autor
    publishing_house = models.CharField(max_length=250) # wydawnictwo
    genre = models.CharField(max_length=250)    # gatunek
    cover = models.CharField(max_length=250, null=True, blank=True)

    def __str__(self):
        return self.title + ' - ' + self.author


class Assortment(models.Model):
    amount = models.IntegerField()  # ilosc na magazynie
    book = models.ForeignKey(Books, on_delete=models.CASCADE)
    price = models.FloatField(default=0)

    def __str__(self):
        return self.book.title + ' - ' + self.book.author + \
               ', amount: ' + str(self.amount) + ', pice: ' + str(self.price)


class Customer(models.Model):
    first_name = models.CharField(max_length=250)   # imie
    last_name = models.CharField(max_length=250)    # nazwisko
    email = models.CharField(max_length=250)    # adres email
    tel_number = models.CharField(max_length=250)   # numer kontatkowy
    loyalty_card = models.BooleanField(default=True)    # karta lojalnosciowa

    def __str__(self):
        return self.first_name + ' ' + self.last_name + ', email: ' + self.email + '; is loyal? ' + \
               str(self.loyalty_card)


class JobTitle(models.Model):
    job_title = models.CharField(max_length=250)    # nazwa stanowiska

    def __str__(self):
        return self.job_title


class Worker(models.Model):
    first_name = models.CharField(max_length=250)  # imie
    last_name = models.CharField(max_length=250)  # nazwisko
    email = models.CharField(max_length=250)  # adres email
    tel_number = models.CharField(max_length=250)
    salary = models.IntegerField()
    job_title = models.ForeignKey(JobTitle, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.first_name + ' ' + self.last_name + ', ' + self.job_title.job_title


class Cart(models.Model):   # przechowuje aktualne przedmioty w koszyku
    assortment = models.ForeignKey(Assortment, on_delete=models.CASCADE)    # wybrany asortyment
    customer = models.CharField(max_length=250)
    amount = models.IntegerField()  # ilosc zakupionych przedmiotow
    total_price = models.FloatField(default=0)

    def __str__(self):
        return self.customer + ' have in cart: ' + self.assortment.book.title +\
               ' in amount of: ' + str(self.amount)


class CompletedCart(models.Model):  # przechowuje zrealizowane karty
    assortment = models.ForeignKey(Assortment, on_delete=models.CASCADE)    # wybrany asortyment
    customer = models.CharField(max_length=250)
    amount = models.IntegerField()  # ilosc zakupionych przedmiotow
    total_price = models.FloatField(default=0)

    def __str__(self):
        return self.customer + ' bought: ' + self.assortment.book.title +\
               ' in amount of: ' + str(self.amount)


class Order(models.Model):
    completed_order = models.ForeignKey(CompletedCart, on_delete=models.CASCADE)
    order_date = models.DateField()
    was_paid = models.BooleanField(default=True)    # czy zamowienie zostalo juz oplacone
    cash_on_delivery = models.BooleanField(default=True)    # czy platnosc za pobraniem
    was_ordered = models.BooleanField(default=True)  # czy zostalo zrealizowane
    total_amount = models.FloatField()

    def __str__(self):
        return self.completed_order.customer + ' amount: ' + self.completed_order.assortment.book.title +\
               ' in amount of: ' + str(self.completed_order.amount) + ', price: ' + str(self.total_amount)

