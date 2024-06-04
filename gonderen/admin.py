from django.contrib import admin

# Register your models here.
from .models import Yuksahibi


class YuksahibiAdmin(admin.ModelAdmin):
  list_display = (
      "TC",
      "AdiSoyadi",
      "Aciklama",
  )


admin.site.register(Yuksahibi, YuksahibiAdmin)