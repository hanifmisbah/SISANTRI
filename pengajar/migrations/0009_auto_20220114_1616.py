# Generated by Django 3.2.3 on 2022-01-14 09:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pengajar', '0008_auto_20220114_1614'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='alquran',
            name='santri',
        ),
        migrations.RemoveField(
            model_name='bandongan',
            name='santri',
        ),
        migrations.RemoveField(
            model_name='matan',
            name='santri',
        ),
        migrations.RemoveField(
            model_name='nadzom',
            name='santri',
        ),
        migrations.RemoveField(
            model_name='sorogan',
            name='santri',
        ),
    ]