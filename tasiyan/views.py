from django.shortcuts import render

# Create your views here.
from django.template import loader
from django.http import HttpResponse


def tasiyanf(request):
  template = loader.get_template('tasiyanT.html')
  return HttpResponse(template.render())

