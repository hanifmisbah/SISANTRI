# Generated by Django 3.2.3 on 2021-12-01 02:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Alquran',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('surah', models.CharField(default='', max_length=12)),
                ('ayat', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Kitab',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kode_kitab', models.IntegerField(default=0)),
                ('nama_kitab', models.CharField(max_length=30)),
                ('kategori_kitab', models.CharField(choices=[('Dasar', 'Dasar'), ('Menengah', 'Menengah'), ('Atas', 'Atas')], default='', max_length=9)),
                ('jenis_kitab', models.CharField(choices=[('Al-Quran', 'Al-Quran'), ('Matan', 'Matan'), ('Nadhom', 'Nadhom')], default='', max_length=9)),
                ('nama_pengarang', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Pengajar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('NIP', models.IntegerField()),
                ('nama_pengajar', models.CharField(max_length=30)),
                ('tempat_lahir', models.CharField(max_length=20)),
                ('tanggal_lahir', models.DateField()),
                ('jk', models.CharField(choices=[('Laki-Laki', 'Laki-Laki'), ('Perempuan', 'Perempuan')], default='', max_length=9)),
                ('almt', models.TextField(default='')),
                ('telp', models.IntegerField(default=0)),
                ('email', models.CharField(default='', max_length=20)),
                ('pngjr', models.CharField(default='', max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Pengumuman',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tgl', models.DateField(auto_now=True)),
                ('judul', models.CharField(default='', max_length=30)),
                ('pengumuman', models.TextField(default='')),
            ],
        ),
        migrations.CreateModel(
            name='Santri',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nis', models.IntegerField()),
                ('nama_santri', models.CharField(max_length=30)),
                ('tempat_lahir', models.CharField(max_length=20)),
                ('tanggal_lahir', models.DateField()),
                ('jk', models.CharField(choices=[('Laki-Laki', 'Laki-Laki'), ('Perempuan', 'Perempuan')], default='', max_length=9)),
                ('almt', models.TextField(default='')),
                ('telp', models.IntegerField(default=0)),
                ('email', models.CharField(default='', max_length=20)),
                ('ktgri', models.CharField(choices=[('Quran', 'Al-Quran'), ('Matan', 'Matan'), ('Nadhom', 'Nadhom')], default='', max_length=8)),
            ],
        ),
    ]
