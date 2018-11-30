from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from django.views.generic import RedirectView

urlpatterns = [
    path('', RedirectView.as_view(url='home/')),
    path('home/', include('Projekt.urls')),
    path('admin/', admin.site.urls),

]
