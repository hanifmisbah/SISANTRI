# Generated by Django 3.2.3 on 2021-12-29 14:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('adminpondok', '0011_alter_pengajar_pngjr'),
        ('pengajar', '0003_alter_nadzom_kelancaran'),
    ]

    operations = [
        migrations.CreateModel(
            name='Santri',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('santri', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='termasuk', to='adminpondok.santri')),
            ],
        ),
    ]
