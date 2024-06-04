from django.shortcuts import render

# Create your views here.

from django.template import loader
from django.http import HttpResponse


def gonderenf(request):
    template = loader.get_template('gonderenler.html')
    return HttpResponse(template.render())


import gonderen
from gonderen.models import Yuksahibi
from django import forms
from django.shortcuts import redirect


class GondericiForm(forms.ModelForm):

    class Meta:
        model = Yuksahibi
        fields = ['TC', 'AdiSoyadi', 'Aciklama']


def ekle(request):
    if request.method == 'POST':
        xx = GondericiForm(request.POST)
        if xx.is_valid():
            # Form verileri işleme
            xx.save()  # Veritabanına kaydetme
            return redirect('gonderenliste')  #url name
    else:
        xx = GondericiForm()
    return render(request, 'gonderenekle.html', {'form': xx})


def listele(request):
    gonderenliste = Yuksahibi.objects.all()
    template = loader.get_template('gonderenlistele.html')
    context = {
        'gonderenliste': gonderenliste,
    }
    return HttpResponse(template.render(context, request))

def listele2(request):
    gonderenliste = Yuksahibi.objects.all()
    template = loader.get_template('gonderenlistele2.html')
    context = {
        'gonderenliste': gonderenliste,
    }
    return HttpResponse(template.render(context, request))


# def gonderen(request):
#   template = loader.get_template('index1.html')
#   return HttpResponse(template.render())


def detay(request, id):
    gonderenliste = Yuksahibi.objects.all()
    item = Yuksahibi.objects.get(id=id)
    template = loader.get_template('detay.html')
    context = {
        'item': item,
        'gonderenliste': gonderenliste,
    }
    return HttpResponse(template.render(context, request))


def sil(request, id):
    item = Yuksahibi.objects.get(id=id)
    item.delete()
    return redirect('gonderenliste')


def guncelle(request, id):
    
    gonderen = Yuksahibi.objects.get(id=id)
    if request.method == 'POST':
        form = GondericiForm(request.POST, instance=gonderen)
        if form.is_valid():
            # Form verileri işleme
            form.save()  # Veritab. kaydetme
            return redirect('gonderenliste')  #url name
    else:
        form = GondericiForm(instance=gonderen)
    return render(request, 'duzenle.html', {'form': form})
