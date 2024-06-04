from django.db import models

# Create your models here.

class Owner(models.Model):
  TC = models.CharField(max_length=11)
  AdiSoyadi = models.CharField(max_length=50)
  Aciklama = models.CharField(max_length=255)


class Yuksahibi(models.Model):
  TC = models.CharField(max_length=11)
  AdiSoyadi = models.CharField(max_length=50)
  Aciklama = models.CharField(max_length=255)

  def __str__(self):
    return f"{self.TC} {self.AdiSoyadi} {self.Aciklama}"


class Gonderici(models.Model):
  TC = models.CharField(max_length=11)
  Adi = models.CharField(max_length=30)
  Soyadi = models.CharField(max_length=20)
