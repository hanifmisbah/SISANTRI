# Generated by Django 3.2.3 on 2021-12-11 12:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('adminpondok', '0002_alter_santri_ktgri'),
    ]

    operations = [
        migrations.CreateModel(
            name='Kategori',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ktgri', models.CharField(choices=[('Al-Quran', 'Al-Quran'), ('Matan', 'Matan'), ('Nadhom', 'Nadhom')], default='', max_length=8, unique=True)),
            ],
        ),
        migrations.AlterField(
            model_name='santri',
            name='ktgri',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='adminpondok.kategori'),
        ),
    ]
