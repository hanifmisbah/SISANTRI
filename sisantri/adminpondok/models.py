from django.db import models

# Create your models here.


class Santri(models.Model):
    kelamin = [
        ('Laki-Laki', 'Laki-Laki'),
        ('Perempuan', 'Perempuan'),
    ]
    kategori = [
        ('Quran', 'Al-Quran'),
        ('Matan', 'Matan'),
        ('Nadhom', 'Nadhom'),
    ]

    nis = models.IntegerField()
    nama_santri = models.CharField(max_length=30, null=False, blank=False)
    tempat_lahir = models.CharField(max_length=20, null=False, blank=False)
    tanggal_lahir = models.DateField()
    jk = models.CharField(max_length=9, choices=kelamin, default='', null=False, blank=False)
    almt = models.TextField(default='', null=False, blank=False)
    telp = models.IntegerField(default=0, null=False, blank=False)
    email = models.CharField(default='', max_length=20, null=False, blank=False)
    ktgri = models.CharField(default='', choices=kategori, max_length=8, null=False, blank=False)


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
    pngjr = models.CharField(max_length=10, default='')


class Alquran(models.Model):
    surah = models.CharField(default='', max_length=12)
    ayat = models.IntegerField(default=0)


class Pengumuman(models.Model):
    tgl = models.DateField(blank=False, null=False)
    pngmn = models.CharField(max_length=30, default='')


class Kitab(models.Model):
    kategori_kitab = [
        ('Dasar', 'Dasar'),
        ('Menengah', 'Menengah'),
        ('Atas', 'Atas'),
    ]
    jenis = [
        ('Al-Quran', 'Al-Quran'),
        ('Matan', 'Matan'),
        ('Nadhom', 'Nadhom'),
    ]
    kode_kitab = models.IntegerField(default=0)
    nama_kitab = models.CharField(max_length=30)
    kategori_kitab = models.CharField(max_length=9, choices=kategori_kitab, default='')
    jenis_kitab = models.CharField(max_length=9, choices=jenis, default='')
    nama_pengarang = models.CharField(max_length=30)


# class Matan(models.Model):
