# Generated by Django 3.2.8 on 2021-12-24 14:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pengajar', '0008_bandongan_tgl'),
    ]

    operations = [
        migrations.RenameField(
            model_name='nadzom',
            old_name='halaman',
            new_name='bait',
        ),
        migrations.RemoveField(
            model_name='nadzom',
            name='paragraf',
        ),
        migrations.AddField(
            model_name='nadzom',
            name='kelancaran',
            field=models.CharField(default=0, max_length=30),
        ),
    ]