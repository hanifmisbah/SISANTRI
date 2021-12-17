from django.db import models

import pengajar

# Create your models here.


class Alquran(models.Model):
    surah = models.CharField(default='', max_length=12)
    ayat = models.IntegerField(default=0)
    juz = models.IntegerField(default=0)
    halaman = models.IntegerField(default=0)
    pengajar = models.CharField(default='', max_length=30)
    keterangan = models.CharField(default=0, max_length=120)
