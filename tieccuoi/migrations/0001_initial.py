# Generated by Django 4.1.4 on 2022-12-22 00:46

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BaoCaoDoanhSo',
            fields=[
                ('MaBaoCao', models.AutoField(primary_key=True, serialize=False)),
                ('Thang', models.DateField()),
                ('TongDoanhThu', models.DecimalField(decimal_places=2, default=0, max_digits=14)),
            ],
        ),
        migrations.CreateModel(
            name='Ca',
            fields=[
                ('MaCa', models.AutoField(primary_key=True, serialize=False)),
                ('TenCa', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='DatTiec',
            fields=[
                ('MaTiecCuoi', models.AutoField(primary_key=True, serialize=False)),
                ('TenChuRe', models.CharField(max_length=40)),
                ('TenCoDau', models.CharField(max_length=40)),
                ('SDT', models.CharField(max_length=10)),
                ('Ngay', models.DateField(default=datetime.date.today)),
                ('TienDatCoc', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=14, null=True)),
                ('SoLuongBan', models.PositiveIntegerField(default=0)),
                ('SLDuTru', models.PositiveIntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='DichVu',
            fields=[
                ('MaDichVu', models.AutoField(primary_key=True, serialize=False)),
                ('TenDichVu', models.CharField(max_length=20)),
                ('DonGia', models.DecimalField(decimal_places=2, default=0, max_digits=14)),
                ('GhiChu', models.CharField(blank=True, max_length=20, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='LoaiSanh',
            fields=[
                ('MaLoaiSanh', models.AutoField(primary_key=True, serialize=False)),
                ('TenLoaiSanh', models.CharField(max_length=20, unique=True)),
                ('DonGia', models.DecimalField(decimal_places=2, default=0, max_digits=14)),
            ],
        ),
        migrations.CreateModel(
            name='MonAn',
            fields=[
                ('MaMonAn', models.AutoField(primary_key=True, serialize=False)),
                ('TenMonAn', models.CharField(max_length=40)),
                ('DonGia', models.DecimalField(decimal_places=2, default=0, max_digits=14)),
                ('GhiChu', models.CharField(blank=True, max_length=20, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ThamSo',
            fields=[
                ('MaThamSo', models.AutoField(primary_key=True, serialize=False)),
                ('TenThamSo', models.CharField(max_length=20)),
                ('GiaTri', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Sanh',
            fields=[
                ('MaSanh', models.AutoField(primary_key=True, serialize=False)),
                ('TenSanh', models.CharField(max_length=20, unique=True)),
                ('SoLuongBan', models.PositiveIntegerField(default=0)),
                ('GhiChu', models.CharField(blank=True, max_length=40, null=True)),
                ('MaLoaiSanh', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tieccuoi.loaisanh')),
            ],
        ),
        migrations.CreateModel(
            name='HoaDon',
            fields=[
                ('MaHoaDon', models.AutoField(primary_key=True, serialize=False)),
                ('NgayThanhToan', models.DateTimeField(blank=True, null=True)),
                ('TongTienHoaDon', models.DecimalField(decimal_places=2, default=0, max_digits=14)),
                ('ConLai', models.DecimalField(decimal_places=2, default=0, max_digits=14)),
                ('MaTiecCuoi', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tieccuoi.dattiec')),
            ],
        ),
        migrations.AddField(
            model_name='dattiec',
            name='DSDichVu',
            field=models.ManyToManyField(to='tieccuoi.dichvu'),
        ),
        migrations.AddField(
            model_name='dattiec',
            name='DSMonAn',
            field=models.ManyToManyField(to='tieccuoi.monan'),
        ),
        migrations.AddField(
            model_name='dattiec',
            name='MaSanh',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tieccuoi.sanh'),
        ),
        migrations.AddField(
            model_name='dattiec',
            name='TenCa',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='tieccuoi.ca'),
        ),
        migrations.CreateModel(
            name='ChiTietDoanhSo',
            fields=[
                ('MaDoanhThu', models.AutoField(primary_key=True, serialize=False)),
                ('Ngay', models.DateField(auto_now_add=True)),
                ('SLTiecCuoi', models.PositiveIntegerField(default=0)),
                ('DoanhThu', models.DecimalField(decimal_places=2, default=0, max_digits=14)),
                ('TiLe', models.FloatField(max_length=5)),
                ('MaTiecCuoi', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tieccuoi.dattiec')),
            ],
        ),
    ]