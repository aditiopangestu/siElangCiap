# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-05 19:43
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('allInOne', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='HistoriAksesoris',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tanggal', models.DateField(help_text='Tanggal')),
                ('nomor_bukti', models.CharField(help_text='Nomor Bukti', max_length=10)),
                ('id_aksesoris', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='allInOne.Aksesoris')),
            ],
            options={
                'ordering': ['tanggal'],
            },
        ),
        migrations.CreateModel(
            name='HistoriBahan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tanggal', models.DateField(help_text='Tanggal')),
                ('nomor_bukti', models.CharField(help_text='Nomor Bukti', max_length=10)),
                ('id_bahan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='allInOne.Bahan')),
            ],
            options={
                'ordering': ['tanggal'],
            },
        ),
        migrations.CreateModel(
            name='KebutuhanAksesoris',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pemakaian_di', models.TextField(help_text='Pemakaian di', max_length=100)),
                ('jumlah_per_lusin', models.IntegerField(help_text='Jumlah/Lusin')),
                ('x', models.IntegerField(default=1, help_text='Faktor Pengali(X)')),
                ('marker', models.FloatField(default=1, help_text='Marker')),
                ('lembar_bahan', models.IntegerField(default=12, help_text='Lembar Bahan')),
                ('art', models.ManyToManyField(to='allInOne.Produk')),
                ('id_aksesoris', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='allInOne.Aksesoris')),
            ],
            options={
                'ordering': ['id_aksesoris'],
            },
        ),
        migrations.CreateModel(
            name='KebutuhanBahan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pemakaian_untuk', models.TextField(help_text='Pemakaian untuk', max_length=100)),
                ('jumlah_per_lusin', models.IntegerField(help_text='Jumlah/Lusin')),
                ('x', models.IntegerField(default=1, help_text='Faktor Pengali(X)')),
                ('marker', models.FloatField(default=1, help_text='Marker')),
                ('lembar_bahan', models.IntegerField(default=12, help_text='Lembar Bahan')),
                ('art', models.ManyToManyField(to='allInOne.Produk')),
                ('id_bahan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='allInOne.Bahan')),
            ],
            options={
                'ordering': ['id_bahan'],
            },
        ),
        migrations.CreateModel(
            name='ProductionOrder',
            fields=[
                ('no_po', models.IntegerField(default=0, help_text='Production Order Number', primary_key=True, serialize=False)),
                ('cust', models.CharField(help_text='Cust', max_length=40)),
                ('tanggal', models.DateField(help_text='Tanggal')),
            ],
            options={
                'ordering': ['tanggal'],
            },
        ),
    ]