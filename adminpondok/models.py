from django.db import models

# Create your models here.


class Kategori(models.Model):
    kategori_kitab = [
        ('Dasar', 'Dasar'),
        ('Menengah', 'Menengah'),
        ('Atas', 'Atas'),
    ]
    ktgri = models.CharField(default='', choices=kategori_kitab, max_length=20)


class Santri(models.Model):
    kelamin = [
        ('Laki-Laki', 'Laki-Laki'),
        ('Perempuan', 'Perempuan'),
    ]
    Quran = 'qr'
    Matan = 'mt'
    Nadhom = 'nd'
    kategori = [
        (Quran, 'Al-Quran'),
        (Matan, 'Matan'),
        (Nadhom, 'Nadhom'),
    ]

    nis = models.IntegerField(null=False, unique=True)
    nama_santri = models.CharField(max_length=30, null=False, blank=False)
    tempat_lahir = models.CharField(max_length=20, null=False, blank=False)
    tanggal_lahir = models.DateField()
    jk = models.CharField(max_length=9, choices=kelamin,
                          default='', null=False, blank=False)
    almt = models.TextField(default='', null=False, blank=False)
    telp = models.CharField(max_length=15, null=False, blank=False)
    email = models.CharField(default='', max_length=20,
                             null=False, blank=False)
    # ktgri = models.CharField(default='', choices=kategori, max_length=30)
    ktgri = models.CharField(default='', choices=kategori, max_length=30)

    def Kategori(self):
        return self.ktgri


class Pengajar(models.Model):
    kelamin = [
        ('Laki-Laki', 'Laki-Laki'),
        ('Perempuan', 'Perempuan'),
    ]
    Quran = 'qr'
    Matan = 'mt'
    Nadhom = 'nd'
    kategori = [
        (Quran, 'Al-Quran'),
        (Matan, 'Matan'),
        (Nadhom, 'Nadhom'),
    ]

    NIP = models.IntegerField(unique=True)
    nama_pengajar = models.CharField(max_length=30)
    tempat_lahir = models.CharField(max_length=20)
    tanggal_lahir = models.DateField()
    jk = models.CharField(max_length=9, choices=kelamin, default='')
    almt = models.TextField(default='')
    telp = models.CharField(max_length=15, null=False, blank=False)
    email = models.CharField(default='', max_length=20)
    # pngjr = models.CharField(max_length=50, default='')
    pngjr = models.CharField(default='', choices=kategori, max_length=30)


class Alquran(models.Model):
    surah = models.CharField(default='', max_length=12)
    ayat = models.IntegerField(default=0)


class Pengumuman(models.Model):
    tgl = models.DateField(auto_now=True, blank=False, null=False)
    judul = models.CharField(max_length=30, default='')
    pengumuman = models.TextField(default='')


class Nadzom(models.Model):
    kategori_kitab = [
        ('Dasar', 'Dasar'),
        ('Menengah', 'Menengah'),
        ('Atas', 'Atas'),
    ]

    kode_kitab = models.IntegerField(default=0, unique=True, null=True)
    nama_kitab = models.CharField(max_length=30, unique=True, null=True)
    kategori_kitab = models.CharField(
        max_length=9, choices=kategori_kitab, default='', null=True)
    jumlah_bab = models.IntegerField(default=0)
    jumlah_fashol = models.IntegerField(default=0, null=True)
    jumlah_bait = models.IntegerField(default=0, blank=True, null=True)
    nama_pengarang = models.CharField(max_length=30, null=True)


class Matan(models.Model):
    kategori_kitab = [
        ('Dasar', 'Dasar'),
        ('Menengah', 'Menengah'),
        ('Atas', 'Atas'),
    ]

    kode_kitab = models.IntegerField(default=0, unique=True, null=True)
    nama_kitab = models.CharField(max_length=30, unique=True, null=True)
    kategori_kitab = models.CharField(
        max_length=9, choices=kategori_kitab, default='', null=True)
    jumlah_bab = models.IntegerField(default=0, null=True)
    jumlah_fashol = models.IntegerField(default=0, null=True)
    jumlah_bait = models.IntegerField(default=0, null=True)
    nama_pengarang = models.CharField(max_length=30, null=True)
