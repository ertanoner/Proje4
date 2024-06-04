"""
URL configuration for django_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
import anasayfa.views
import gonderen.views
import tasiyan.views

urlpatterns = [
    path('admin/', admin.site.urls),
     path('home/', anasayfa.views.anasayfafen, name="home"),
        path('anasayfa/', anasayfa.views.anasayfaf),
        path('', anasayfa.views.anasayfaf),
        path('gonderen/', gonderen.views.gonderenf, name="gonderenler"),
        path('gonderen/ekle', gonderen.views.ekle),
        path('gonderen/detay/<int:id>', gonderen.views.detay),
        path('gonderen/sil/<int:id>', gonderen.views.sil),
        path('gonderen/guncelle/<int:id>', gonderen.views.guncelle),
        path('gonderenler', gonderen.views.listele, name="gonderenliste"),
        path('gonderenler2', gonderen.views.listele2, name="gonderenliste2"),
        path('tasiyan/', tasiyan.views.tasiyanf, name="tasiyan"),
        path('tasiyanlar/', tasiyan.views.listele, name="tasiyanliste"),
        path('tasiyan/ekle', tasiyan.views.ekle),
        path('tasiyan/sil/<int:id>', tasiyan.views.sil),
    ]
