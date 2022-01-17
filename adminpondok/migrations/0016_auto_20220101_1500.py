# Generated by Django 3.2.3 on 2022-01-01 08:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('adminpondok', '0015_kitab'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='kategori',
            name='kategori',
        ),
        migrations.AlterField(
            model_name='santri',
            name='kategori',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='kategori_santri', to='adminpondok.kategori'),
        ),
    ]