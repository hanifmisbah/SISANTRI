# Generated by Django 3.2.3 on 2021-12-12 15:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminpondok', '0003_auto_20211211_1930'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='kategori',
            name='id',
        ),
        migrations.AlterField(
            model_name='kategori',
            name='ktgri',
            field=models.CharField(choices=[('Al-Quran', 'Al-Quran'), ('Matan', 'Matan'), ('Nadhom', 'Nadhom')], default='', max_length=8, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='santri',
            name='ktgri',
            field=models.CharField(choices=[('Al-Quran', 'Al-Quran'), ('Matan', 'Matan'), ('Nadhom', 'Nadhom')], default='', max_length=30, unique=True),
        ),
    ]