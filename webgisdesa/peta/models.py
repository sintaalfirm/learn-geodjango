from django.db import models

# Create your models here.

class Superhero(models.Model):
    nama = models.CharField(max_length=80)
    asosiasi = models.CharField(max_length=20)

    def __str__(self):
        return self.nama