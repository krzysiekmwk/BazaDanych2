from django.contrib import admin
from .models import *


@admin.register(Books, Assortment, Customer, JobTitle, Worker, Cart, CompletedCart, Order)
class FullAdmin(admin.ModelAdmin):
    pass
