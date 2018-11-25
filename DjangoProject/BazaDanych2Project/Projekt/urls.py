from django.urls import path
from . import views as projekt_views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('', projekt_views.index, name='home'),
    path('add_to_cart/', projekt_views.add_to_cart, name='add_to_cart'),
    path('signup/', projekt_views.signup, name='signup'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
]
