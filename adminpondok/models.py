from django.db import models

# Create your models here.

class Kategori(models.Model):
    kategori = models.CharField(default='', max_length=10)

class Level(models.Model):
    level = models.CharField(default='', max_length=10)

class Kitab(models.Model):
    nama_kitab = models.CharField(default='', max_length=15)
    kategori = models.ForeignKey(Kategori, on_delete=models.CASCADE, related_name='termasuk')
    level = models.ForeignKey(Level, on_delete=models.CASCADE, related_name='masuk')
    jumlah_bab = models.IntegerField(default=0)
    jumlah_bait = models.IntegerField(default=0, null=True)
    jumlah_halaman = models.IntegerField(default=0, null=True)
    nama_pengarang = models.CharField(max_length=30, null=True)

class Santri(models.Model):
    nis = models.IntegerField(null=False, unique=True)
    nama_santri = models.CharField(max_length=30, null=False, blank=False)
    tempat_lahir = models.CharField(max_length=20, null=False, blank=False)
    tanggal_lahir = models.DateField()
    jk = models.CharField(max_length=10, default='', null=False, blank=False)
    almt = models.TextField(default='', null=False, blank=False)
    telp = models.CharField(max_length=15, null=False, blank=False)
    email = models.CharField(default='', max_length=20, null=False, blank=False)
    kategori = models.ForeignKey(Kategori, on_delete=models.CASCADE, related_name='memilih')

# class SantriNgaji(models.Model):
#     santri = models.ForeignKey(Santri, on_delete=models.CASCADE, related_name='pilih')

# class Pengajar(models.Model):
#     kategori = [
#         ('Quran', 'AlQuran'),
#         ('Matan', 'Matan'),
#         ('Nadzom', 'Nadzom'),
#     ]
#     nip = models.IntegerField(unique=True)
#     nama_pengajar = models.CharField(max_length=30)
#     tempat_lahir = models.CharField(max_length=20)
#     tanggal_lahir = models.DateField()
#     jk = models.CharField(max_length=10, default='', null=False, blank=False)
#     almt = models.TextField(default='')
#     telp = models.CharField(max_length=15, null=False, blank=False)
#     email = models.CharField(default='', max_length=20)
#     kategori = models.CharField(default='', choices=kategori, max_length=30)
#     # kategori = models.ForeignKey(Kategori, on_delete=models.CASCADE, related_name='kategori_pengajar')


# class Alquran(models.Model):
#     surah = models.CharField(default='', max_length=12)
#     ayat = models.IntegerField(default=0)


# class Nadzom(models.Model):
#     nama_kitab = models.CharField(max_length=30, unique=True, null=True)
#     # kategori_kitab = models.ForeignKey(Kategori_Kitab, on_delete=models.CASCADE, related_name='nadzom')
#     jumlah_bab = models.IntegerField(default=0)
#     jumlah_bait = models.IntegerField(default=0, null=True)
#     nama_pengarang = models.CharField(max_length=30, null=True)


# class Matan(models.Model):
#     nama_kitab = models.CharField(max_length=30, unique=True, null=True)
#     # kategori_kitab = models.ForeignKey(Kategori_Kitab, on_delete=models.CASCADE, related_name='matan')
#     jumlah_bab = models.IntegerField(default=0, null=True)
#     jumlah_halaman = models.IntegerField(default=0, null=True)
#     nama_pengarang = models.CharField(max_length=30, null=True)


class Pengumuman(models.Model):
    tgl = models.DateField(auto_now=True, blank=False, null=False)
    judul = models.CharField(max_length=30, default='')
    pengumuman = models.TextField(default='')