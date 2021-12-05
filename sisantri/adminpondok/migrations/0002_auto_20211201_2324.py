# Generated by Django 3.2.3 on 2021-12-01 16:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminpondok', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Kategori',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ktgri', models.CharField(choices=[('Quran', 'Al-Quran'), ('Matan', 'Matan'), ('Nadhom', 'Nadhom')], default='', max_length=8)),
            ],
        ),
        migrations.RemoveField(
            model_name='santri',
            name='ktgri',
        ),
    ]
