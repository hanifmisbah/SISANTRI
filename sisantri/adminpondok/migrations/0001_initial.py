# Generated by Django 3.2.3 on 2021-11-25 17:37

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
                ('ktgri', models.CharField(choices=[('Al-Quran', 'Al-Quran'), ('Matan', 'Matan'), ('Nadhom', 'Nadhom')], default='', max_length=8)),
            ],
        ),
    ]
