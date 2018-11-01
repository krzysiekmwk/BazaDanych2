from django.contrib import admin
from .models import Books, Assortment, Customer, JobTitle, Worker, Cart, CompletedCart, Order

admin.site.register(Books)
admin.site.register(Assortment)
admin.site.register(Customer)
admin.site.register(JobTitle)
admin.site.register(Worker)
admin.site.register(Cart)
admin.site.register(CompletedCart)
admin.site.register(Order)