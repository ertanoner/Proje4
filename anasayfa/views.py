from django.shortcuts import render
from django.http import HttpResponse

def anasayfa_f(request):
  return HttpResponse("Web sitesine hoş geldiniz.")

def anasayfa_f_en(request):
  return HttpResponse("Welcome to the website.")
