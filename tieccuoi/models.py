from django.db import models
from django.core.exceptions import ValidationError
from djmoney.models.fields import MoneyField
from django.utils import timezone
import datetime
import decimal

from django.contrib.auth.models import User

def validatePositive(val):
    if val > 0:
        return val
    else:
        raise ValidationError("Vui lòng nhập số dương")

def validateNonNeg(val):
    if val >= 0:
        return val
    else:
        raise ValidationError("Vui lòng nhập số không âm")

class Ca(models.Model):
    MaCa = models.AutoField(primary_key=True)
    TenCa = models.CharField(max_length=10)

    def __str__(self):
        return self.TenCa

class LoaiSanh(models.Model):
    MaLoaiSanh = models.AutoField(primary_key=True)
    TenLoaiSanh = models.CharField(max_length=20, unique=True)
    DonGia = models.DecimalField(decimal_places=2, default=0, max_digits=14, validators=[validatePositive])

    def __str__(self):
        return self.TenLoaiSanh

class Sanh(models.Model):
    MaSanh = models.AutoField(primary_key=True)
    TenSanh = models.CharField(max_length=20, unique=True)
    SoLuongBan = models.PositiveIntegerField(default=0, validators=[validatePositive])
    MaLoaiSanh = models.ForeignKey(LoaiSanh, on_delete=models.CASCADE)
    GhiChu = models.CharField(max_length=40, blank=True, null=True)

    def __str__(self):
        return self.TenSanh

class MonAn(models.Model):
    MaMonAn = models.AutoField(primary_key=True)
    TenMonAn = models.CharField(max_length=40)
    DonGia = models.DecimalField(decimal_places=2, default=0, max_digits=14, validators=[validatePositive])
    GhiChu = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return self.TenMonAn

class DichVu(models.Model):
    MaDichVu = models.AutoField(primary_key=True)
    TenDichVu = models.CharField(max_length=20)
    DonGia = models.DecimalField(decimal_places=2, default=0, max_digits=14, validators=[validatePositive])
    GhiChu = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return self.TenDichVu

class DatTiec(models.Model):
    MaTiecCuoi = models.AutoField(primary_key=True)
    TenChuRe = models.CharField(max_length=40)
    TenCoDau = models.CharField(max_length=40)
    SDT = models.CharField(max_length=10)
    Ngay = models.DateField(default=datetime.date.today)
    TenCa = models.ForeignKey(Ca, on_delete=models.DO_NOTHING)
    TienDatCoc = models.DecimalField(decimal_places=2, default=0, max_digits=14, null=True, blank=True, validators=[validateNonNeg])
    SoLuongBan = models.PositiveIntegerField(default=0, validators=[validatePositive])
    SLDuTru = models.PositiveIntegerField(default=0, validators=[validateNonNeg])
    MaSanh = models.ForeignKey(Sanh, on_delete=models.CASCADE)
    DSMonAn = models.ManyToManyField(MonAn)
    DSDichVu = models.ManyToManyField(DichVu, blank=True)

    def __str__(self):
        return str(self.MaTiecCuoi)

class HoaDon(models.Model):
    MaHoaDon = models.AutoField(primary_key=True)
    NgayThanhToan = models.DateTimeField(blank=True, null=True)
    # TongTienBan = models.DecimalField(decimal_places=2, default=0, max_digits=14)
    # TongTienDV = models.DecimalField(decimal_places=2, default=0, max_digits=14)
    # TienDatCoc = models.DecimalField(decimal_places=2, default=0, max_digits=14)
    TongTienHoaDon = models.DecimalField(decimal_places=2, default=0, max_digits=14)
    ConLai = models.DecimalField(decimal_places=2, default=0, max_digits=14)
    MaTiecCuoi = models.ForeignKey(DatTiec, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.MaHoaDon)

class BaoCaoDoanhSo(models.Model):
    MaBaoCao = models.AutoField(primary_key=True)
    Thang = models.DateField()
    TongDoanhThu = models.DecimalField(decimal_places=2, default=0, max_digits=14)

class ChiTietDoanhSo(models.Model):
    MaDoanhThu = models.AutoField(primary_key=True)
    Ngay = models.DateField(auto_now_add=True)
    SLTiecCuoi = models.PositiveIntegerField(default=0)
    DoanhThu = models.DecimalField(decimal_places=2, default=0, max_digits=14)
    TiLe = models.FloatField(max_length=5)
    MaTiecCuoi = models.ForeignKey(DatTiec, on_delete=models.CASCADE)

class ThamSo(models.Model):
    MaThamSo = models.AutoField(primary_key=True)
    TenThamSo = models.CharField(max_length=20)
    GiaTri = models.IntegerField()

    def __str__(self):
        return self.TenThamSo