# Generated by Django 3.2.8 on 2021-12-28 04:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('adminpondok', '0011_alter_pengajar_pngjr'),
        ('pengajar', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='alquran',
            name='santri',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='adminpondok.santri'),
        ),
        migrations.AddField(
            model_name='alquran',
            name='tgl',
            field=models.DateField(auto_now=True),
        ),
        migrations.CreateModel(
            name='Sorogan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tgl', models.DateField(auto_now=True)),
                ('kitab', models.CharField(default='', max_length=30)),
                ('bab', models.IntegerField(default=0)),
                ('halaman', models.IntegerField(default=0)),
                ('paragraf', models.CharField(default='', max_length=20)),
                ('pengajar', models.CharField(default=0, max_length=30)),
                ('santri', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='adminpondok.santri')),
            ],
        ),
        migrations.CreateModel(
            name='Nadzom',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tgl', models.DateField(auto_now=True, null=True)),
                ('kitab', models.CharField(default=0, max_length=30)),
                ('bab', models.IntegerField(default=0)),
                ('bait', models.IntegerField(default=0)),
                ('kelancaran', models.CharField(default=0, max_length=30)),
                ('pengajar', models.CharField(default=0, max_length=30)),
                ('keterangan', models.CharField(default=0, max_length=30)),
                ('santri', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='adminpondok.santri')),
            ],
        ),
        migrations.CreateModel(
            name='Matan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tgl', models.DateField(auto_now=True)),
                ('kitab', models.CharField(default=0, max_length=30)),
                ('bab', models.IntegerField(default=0)),
                ('halaman', models.IntegerField(default=0)),
                ('paragraf', models.IntegerField(default=0)),
                ('pengajar', models.CharField(default=0, max_length=30)),
                ('keterangan', models.CharField(default=0, max_length=30)),
                ('santri', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='adminpondok.santri')),
            ],
        ),
        migrations.CreateModel(
            name='Bandongan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tgl', models.DateField(auto_now=True, null=True)),
                ('kitab', models.CharField(default=0, max_length=30)),
                ('bab', models.IntegerField(default=0)),
                ('halaman', models.IntegerField(default=0)),
                ('paragraf', models.IntegerField(default=0)),
                ('pengajar', models.CharField(default=0, max_length=30)),
                ('keterangan', models.CharField(default=0, max_length=30)),
                ('santri', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='adminpondok.santri')),
            ],
        ),
    ]
