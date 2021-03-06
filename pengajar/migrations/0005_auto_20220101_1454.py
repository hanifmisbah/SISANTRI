# Generated by Django 3.2.3 on 2022-01-01 07:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('adminpondok', '0015_kitab'),
        ('pengajar', '0004_santri'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alquran',
            name='pengajar',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='adminpondok.pengajar'),
        ),
        migrations.AlterField(
            model_name='alquran',
            name='santri',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='adminpondok.santri'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='bandongan',
            name='pengajar',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='adminpondok.pengajar'),
        ),
        migrations.AlterField(
            model_name='bandongan',
            name='santri',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='adminpondok.santri'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='matan',
            name='pengajar',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='adminpondok.pengajar'),
        ),
        migrations.AlterField(
            model_name='matan',
            name='santri',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='adminpondok.santri'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='nadzom',
            name='pengajar',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='adminpondok.pengajar'),
        ),
        migrations.AlterField(
            model_name='nadzom',
            name='santri',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='adminpondok.santri'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='sorogan',
            name='pengajar',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='adminpondok.pengajar'),
        ),
        migrations.AlterField(
            model_name='sorogan',
            name='santri',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='adminpondok.santri'),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='Santri',
        ),
    ]
