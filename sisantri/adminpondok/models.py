from django.db import models
from django.db.models.fields import CharField

# Create your models here.
class Santri(models.Model):
    kelamin = [
        ('Laki-Laki', 'Laki-Laki'),
        ('Perempuan', 'Perempuan'),
    ]
    kategori = [
        ('Al-Quran', 'Al-Quran'),
        ('Matan', 'Matan'),
        ('Nadhom', 'Nadhom'),
    ]

    nis = models.IntegerField()
    nama_santri = models.CharField(max_length=30)
    tempat_lahir = models.CharField(max_length=20)
    tanggal_lahir = models.DateField()
    jk = models.CharField(max_length=9, choices=kelamin, default='')
    almt = models.TextField(default='')
    telp = models.IntegerField(default=0)
    email = models.CharField(default='', max_length=20)
    ktgri = models.CharField(default='', choices=kategori, max_length=8)

class Pengajar(models.Model):
    kelamin = [
        ('Laki-Laki', 'Laki-Laki'),
        ('Perempuan', 'Perempuan'),
    ]
    NIP = models.IntegerField()
    nama_pengajar = models.CharField(max_length=30)
    tempat_lahir = models.CharField(max_length=20)
    tanggal_lahir = models.DateField()
    jk = models.CharField(max_length=9, choices=kelamin, default='')
    almt = models.TextField(default='')
    telp = models.IntegerField(default=0)
    email = models.CharField(default='', max_length=20)
    pngjr = models.CharField(max_length= 10, default='')


class Alquran(models.Model):
    surah = models.CharField(default='', max_length=12)
    ayat = models.IntegerField(default=0)

class Pengumuman(models.Model):
    tgl = models.DateField(blank=False, null=False)
    pngmn = models.CharField(max_length=30, default='')
    
# class Matan(models.Model):
