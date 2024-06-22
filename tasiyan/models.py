from django.db import models


# Create your models here.
class Tasiyan(models.Model):
  TC = models.CharField(max_length=11)
  AdiSoyadi = models.CharField(max_length=50)
  TelNo = models.CharField(max_length=50, null=True)
  Firma = models.CharField(max_length=50)
  Aciklama = models.CharField(max_length=255)
