from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse


def tasiyanf(request):
  template = loader.get_template('tasiyanT.html')
  return HttpResponse(template.render())

from tasiyan.models import Tasiyan
from django import forms
from django.shortcuts import redirect


def listele(request):
  tasiyanliste = Tasiyan.objects.all()
  template = loader.get_template('tasiyanliste.html')
  context = {
      'tasiyanliste': tasiyanliste,
  }
  return HttpResponse(template.render(context, request))


class TasiyanForm(forms.ModelForm):

  class Meta:
    model = Tasiyan
    fields = ['TC', 'AdiSoyadi','TelNo', 'Firma', 'Aciklama']


def ekle(request):
  if request.method == 'POST':
    xx = TasiyanForm(request.POST)
    if xx.is_valid():
      # Form verileri işleme
      xx.save()  # Veritabanına kaydetme
      return redirect('tasiyanliste')  #url name
  else:
    xx = TasiyanForm()
  return render(request, 'tasiyanekle.html', {'form': xx})

def sil(request, id):
  item = Tasiyan.objects.get(id=id)
  item.delete()
  return redirect('tasiyanliste')

