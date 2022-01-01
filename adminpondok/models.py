from django.db import models

# Create your models here.


class Kategori_Kitab(models.Model):
    kategori_kitab = [
        ('Dasar', 'Dasar'),
        ('Menengah', 'Menengah'),
        ('Atas', 'Atas'),
    ]
    kategori_kitab = models.CharField(default='', choices=kategori_kitab, max_length=20)

    # def __str__(self):
    #     return self.kategori_kitab

class Kategori(models.Model):
    kategori = [
        ('Quran', 'AlQuran'),
        ('Matan', 'Matan'),
        ('Nadzom', 'Nadzom'),
    ]

    kategori = models.CharField(default='', choices=kategori, max_length=30)

    # def __repr__(self):
    #     return self.kategori


class Santri(models.Model):
    kategori = [
        ('Quran', 'AlQuran'),
        ('Matan', 'Matan'),
        ('Nadzom', 'Nadzom'),
    ]

    nis = models.IntegerField(null=False, unique=True)
    nama_santri = models.CharField(max_length=30, null=False, blank=False)
    tempat_lahir = models.CharField(max_length=20, null=False, blank=False)
    tanggal_lahir = models.DateField()
    jk = models.CharField(max_length=10, default='', null=False, blank=False)
    almt = models.TextField(default='', null=False, blank=False)
    telp = models.CharField(max_length=15, null=False, blank=False)
    email = models.CharField(default='', max_length=20, null=False, blank=False)
    kategori = models.CharField(default='', choices=kategori, max_length=30)
    # kategori = models.ForeignKey(Kategori, on_delete=models.CASCADE, related_name='kategori_santri')


class Pengajar(models.Model):
    kategori = [
        ('Quran', 'AlQuran'),
        ('Matan', 'Matan'),
        ('Nadzom', 'Nadzom'),
    ]
    nip = models.IntegerField(unique=True)
    nama_pengajar = models.CharField(max_length=30)
    tempat_lahir = models.CharField(max_length=20)
    tanggal_lahir = models.DateField()
    jk = models.CharField(max_length=10, default='', null=False, blank=False)
    almt = models.TextField(default='')
    telp = models.CharField(max_length=15, null=False, blank=False)
    email = models.CharField(default='', max_length=20)
    kategori = models.CharField(default='', choices=kategori, max_length=30)
    # kategori = models.ForeignKey(Kategori, on_delete=models.CASCADE, related_name='kategori_pengajar')


class Alquran(models.Model):
    surah = models.CharField(default='', max_length=12)
    ayat = models.IntegerField(default=0)


class Nadzom(models.Model):
    nama_kitab = models.CharField(max_length=30, unique=True, null=True)
    kategori_kitab = models.ForeignKey(Kategori_Kitab, on_delete=models.CASCADE, related_name='nadzom')
    jumlah_bab = models.IntegerField(default=0)
    jumlah_bait = models.IntegerField(default=0, null=True)
    nama_pengarang = models.CharField(max_length=30, null=True)


class Matan(models.Model):
    nama_kitab = models.CharField(max_length=30, unique=True, null=True)
    kategori_kitab = models.ForeignKey(Kategori_Kitab, on_delete=models.CASCADE, related_name='matan')
    jumlah_bab = models.IntegerField(default=0, null=True)
    jumlah_halaman = models.IntegerField(default=0, null=True)
    nama_pengarang = models.CharField(max_length=30, null=True)


class Kitab(models.Model):
    matan = models.ForeignKey(Matan, on_delete=models.CASCADE, related_name='kitab_matan')
    nadzom = models.ForeignKey(Nadzom, on_delete=models.CASCADE, related_name='kitab_nadzom')

class Pengumuman(models.Model):
    tgl = models.DateField(auto_now=True, blank=False, null=False)
    judul = models.CharField(max_length=30, default='')
    pengumuman = models.TextField(default='')