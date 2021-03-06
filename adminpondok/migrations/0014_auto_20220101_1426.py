# Generated by Django 3.2.3 on 2022-01-01 07:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminpondok', '0013_auto_20220101_1412'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pengajar',
            old_name='NIP',
            new_name='nip',
        ),
        migrations.AlterField(
            model_name='pengajar',
            name='kategori',
            field=models.CharField(choices=[('Quran', 'AlQuran'), ('Matan', 'Matan'), ('Nadzom', 'Nadzom')], default='', max_length=30),
        ),
        migrations.AlterField(
            model_name='santri',
            name='kategori',
            field=models.CharField(choices=[('Quran', 'AlQuran'), ('Matan', 'Matan'), ('Nadzom', 'Nadzom')], default='', max_length=30),
        ),
    ]
