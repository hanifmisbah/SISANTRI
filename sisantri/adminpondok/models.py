from django.db import models

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


# class Alquran(models.Model):
#     surah = models.CharField(default='', max_length=12)
#     ayat = models.IntegerField(default=0, max_length=12)


# class Matan(models.Model):
