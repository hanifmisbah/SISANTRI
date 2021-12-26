from django.db import models
import adminpondok

import pengajar
from adminpondok import models as adminmodels

# Create your models here.


class Alquran(models.Model):
    tgl = models.DateField(auto_now=True, blank=False, null=False)
    surah = models.CharField(default='', max_length=12)
    ayat = models.IntegerField(default=0)
    juz = models.IntegerField(default=0)
    halaman = models.IntegerField(default=0)
    pengajar = models.CharField(default='', max_length=30)
    keterangan = models.CharField(default=0, max_length=120)


class Sorogan(models.Model):
    kitab = models.CharField(default='', max_length=30)
    bab = models.IntegerField(default=0)
    halaman = models.IntegerField(default=0)
    paragraf = models.CharField(default='', max_length=20)
    pengajar = models.CharField(default=0, max_length=30)


class Matan(models.Model):
    kitab = models.CharField(default=0, max_length=30)
    bab = models.IntegerField(default=0)
    halaman = models.IntegerField(default=0)
    paragraf = models.IntegerField(default=0)
    pengajar = models.CharField(default=0, max_length=30)
    keterangan = models.CharField(default=0, max_length=30)


class Bandongan (models.Model):
    tgl = models.DateField(auto_now=True, blank=False, null=True)
    kitab = models.CharField(default=0, max_length=30)
    bab = models.IntegerField(default=0)
    halaman = models.IntegerField(default=0)
    paragraf = models.IntegerField(default=0)
    pengajar = models.CharField(default=0, max_length=30)
    keterangan = models.CharField(default=0, max_length=30)


class Nadzom (models.Model):
    kitab = models.CharField(default=0, max_length=30)
    bab = models.IntegerField(default=0)
    bait = models.IntegerField(default=0)
    kelancaran = models.CharField(default=0, max_length=30)
    pengajar = models.CharField(default=0, max_length=30)
    keterangan = models.CharField(default=0, max_length=30)


class Santri (models.Model):
    santri = models.ForeignKey(
        adminmodels.Santri, on_delete=models.CASCADE, related_name='termasuk')
    nama_santri = models.CharField(max_length=30, null=False, blank=False)
