# Generated by Django 3.2.3 on 2021-12-06 06:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminpondok', '0003_auto_20211206_0832'),
    ]

    operations = [
        migrations.AlterField(
            model_name='santri',
            name='ktgri',
            field=models.CharField(choices=[('Al-Quran', 'Al-Quran'), ('Matan', 'Matan'), ('Nadhom', 'Nadhom')], default='', max_length=8, unique=True),
        ),
    ]
