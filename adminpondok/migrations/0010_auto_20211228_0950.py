# Generated by Django 3.2.8 on 2021-12-28 02:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminpondok', '0009_kategori'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pengajar',
            name='telp',
            field=models.CharField(max_length=15),
        ),
        migrations.AlterField(
            model_name='santri',
            name='telp',
            field=models.CharField(max_length=15),
        ),
    ]