# Generated by Django 3.2.8 on 2021-12-26 03:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pengajar', '0009_auto_20211224_2130'),
    ]

    operations = [
        migrations.AddField(
            model_name='alquran',
            name='tgl',
            field=models.DateField(auto_now=True),
        ),
    ]
