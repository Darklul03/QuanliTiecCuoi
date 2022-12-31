from django import forms
from django.forms import ModelForm
from django.forms import formset_factory
from django.contrib.auth.models import User
from .models import *
import datetime
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.forms import AuthenticationForm

class TiepNhanSanh(ModelForm):
    # TenLoaiSanh = forms.ModelChoiceField(queryset=LoaiSanh.objects.all())
    class Meta:
        model = Sanh
        fields = ('TenSanh', 'SoLuongBan', 'MaLoaiSanh', 'GhiChu')
        labels = {
            'TenSanh': 'Tên sảnh',
            'SoLuongBan': 'Số lượng bàn',
            'GhiChu': 'Ghi chú',
            'MaLoaiSanh': 'Tên loại sảnh'
        }

class ThemLoaiSanh(ModelForm):
    class Meta:
        model = LoaiSanh
        fields = ('TenLoaiSanh', 'DonGia')
        labels = {
            'TenLoaiSanh': 'Tên loại sảnh',
            'DonGia': 'Đơn giá tối thiểu'
        }

class DatTiecCuoi(ModelForm):
    class Meta:
        model = DatTiec
        fields = ('TenChuRe', 'TenCoDau', 'SDT', 'TenCa', 'TienDatCoc', 'SoLuongBan', 'SLDuTru', 'MaSanh', 'DSMonAn', 'DSDichVu', 'Ngay')
        widgets = {
            'Ngay': forms.DateInput(format='%d-%m-%Y', attrs={'class':'form-control', 'type': 'date'}),
            'DSMonAn': forms.CheckboxSelectMultiple(),
            'DSDichVu': forms.CheckboxSelectMultiple()
        }
        labels = {
            'TenChuRe': 'Tên chú rể',
            'TenCoDau': 'Tên cô dâu',
            'SDT': 'Số điện thoại',
            'TenCa': 'Ca',
            'TienDatCoc': 'Tiền đặt cọc',
            'SoLuongBan': 'Số lượng bàn',
            'SLDuTru': 'Số lượng dự trữ',
            'MaSanh': 'Tên sảnh',
            'Ngay': 'Ngày đãi tiệc',
            'DSMonAn': 'Danh sách món ăn',
            'DSDichVu': 'Danh sách dịch vụ'
        }

class ThemMonAn(ModelForm):
    class Meta:
        model = MonAn
        fields = ('TenMonAn', 'DonGia', 'GhiChu')
        labels = {
            'TenMonAn': 'Tên món ăn',
            'DonGia': 'Đơn giá',
            'GhiChu': 'Ghi chú'
        }

class ThemDichVu(ModelForm):
    class Meta:
        model = DichVu
        fields = ('TenDichVu', 'DonGia', 'GhiChu')
        labels = {
            'TenDichVu': 'Tên dịch vụ',
            'DonGia': 'Đơn giá',
            'GhiChu': 'Ghi chú'
        }

class TraCuu(forms.Form):
    ChuRe = forms.CharField(max_length=40, required=False, label='Tên chú rể')
    CoDau = forms.CharField(max_length=40, required=False, label='Tên cô dâu')
    SDT = forms.CharField(max_length=10, required=False, label='SĐT')
    Sanh = forms.ModelChoiceField(queryset=Sanh.objects.all(), required=False, label='Sảnh')
    Ngay = forms.DateField(widget=forms.DateInput(attrs={'class':'form-control', 'type': 'date'}), required=False, label='Ngày')

class LapHoaDon(forms.Form):
    MaTiecCuoi = forms.IntegerField(label='Mã tiệc cưới')
    SoTien = forms.IntegerField(label='Số tiền', validators=[validatePositive])

# class 