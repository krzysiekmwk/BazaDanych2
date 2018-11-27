from django.urls import path
from . import views as projekt_views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('', projekt_views.index, name='home'),
    path('add_to_cart/', projekt_views.add_to_cart, name='add_to_cart'),
    path('cart/edit_order/', projekt_views.edit_order, name='edit_order'),
    path('cart/confirm_order/', projekt_views.confirm_order, name='confirm_order'),
    path('signup/', projekt_views.signup, name='signup'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('cart/', projekt_views.cart, name='cart'),
]
