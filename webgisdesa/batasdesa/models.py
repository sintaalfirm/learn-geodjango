from django.db import models
from django.contrib.gis.db import models as gismodels

# Create your models here.
class BangunanPogung(models.Model):
    nama = gismodels.CharField(max_length=254, null=True, blank=True)
    jenis = gismodels.CharField(max_length=254, null=True, blank=True)
    pemilik = models.ForeignKey("peta.Superhero", on_delete=models.CASCADE, null=True, blank=True)
    geom = gismodels.MultiPolygonField(srid=4326)

