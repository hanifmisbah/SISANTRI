from django.db import models
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
    santri = models.ForeignKey(
        adminmodels.Santri, on_delete=models.CASCADE, null=True)


class Sorogan(models.Model):
    tgl = models.DateField(auto_now=True, blank=False, null=False)
    kitab = models.CharField(default='', max_length=30)
    bab = models.IntegerField(default=0)
    halaman = models.IntegerField(default=0)
    paragraf = models.CharField(default='', max_length=20)
    pengajar = models.CharField(default=0, max_length=30)
    santri = models.ForeignKey(
        adminmodels.Santri, on_delete=models.CASCADE, null=True)


class Matan(models.Model):
    tgl = models.DateField(auto_now=True, blank=False, null=False)
    kitab = models.CharField(default=0, max_length=30)
    bab = models.IntegerField(default=0)
    halaman = models.IntegerField(default=0)
    paragraf = models.IntegerField(default=0)
    pengajar = models.CharField(default=0, max_length=30)
    keterangan = models.CharField(default=0, max_length=30)
    santri = models.ForeignKey(
        adminmodels.Santri, on_delete=models.CASCADE, null=True)


class Bandongan (models.Model):
    tgl = models.DateField(auto_now=True, blank=False, null=True)
    kitab = models.CharField(default=0, max_length=30)
    bab = models.IntegerField(default=0)
    halaman = models.IntegerField(default=0)
    paragraf = models.IntegerField(default=0)
    pengajar = models.CharField(default=0, max_length=30)
    keterangan = models.CharField(default=0, max_length=30)
    santri = models.ForeignKey(
        adminmodels.Santri, on_delete=models.CASCADE, null=True)


class Nadzom (models.Model):
    tgl = models.DateField(auto_now=True, blank=False, null=True)
    kitab = models.CharField(default=0, max_length=30)
    bab = models.IntegerField(default=0)
    bait = models.IntegerField(default=0)
    kelancaran = models.CharField(default='', max_length=30)
    pengajar = models.CharField(default=0, max_length=30)
    keterangan = models.CharField(default=0, max_length=30)
    santri = models.ForeignKey(
        adminmodels.Santri, on_delete=models.CASCADE, null=True)


class Santri (models.Model):
    santri = models.ForeignKey(adminmodels.Santri, on_delete=models.CASCADE, related_name='termasuk')
    # nama_santri = models.CharField(max_length=30, null=False, blank=False)
    # input_quran = models.ForeignKey(Alquran, on_delete=models.CASCADE)
