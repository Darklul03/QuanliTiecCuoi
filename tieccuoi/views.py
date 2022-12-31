from django.shortcuts import render, redirect, get_object_or_404
from .models import *
# from datetime import date
from .forms import *
from django.db.models import F
# from django.contrib.auth.decorators import login_required, user_passes_test
# from django.contrib.auth.models import User, Group
# from django.contrib.auth import authenticate, login, logout
# from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
# from django.http import HttpResponseRedirect, HttpResponse
from imp import C_BUILTIN
# from django.db.models import Sum, Count
# import pandas as pd

def view_Default(request):
    return redirect('../tracuu')

def view_TiepNhanSanh(request):
    if request.method == 'POST':
        form = TiepNhanSanh(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Tiếp nhận thành công")
        else:
            messages.warning(request, "Thông tin sảnh không hợp lệ")
    else:
        form = TiepNhanSanh()

    q = Sanh.objects.all().annotate(LoaiSanh=F('MaLoaiSanh__TenLoaiSanh'))

    return render(request, 'tieccuoi/tiepnhansanh.html', {'form': form, 'table': q})


def view_ThemLoaiSanh(request):
    if request.method == 'POST':
        form = ThemLoaiSanh(request.POST)
        if form.is_valid():
            num = ThamSo.objects.filter(TenThamSo='MaxLoaiSanh')[0].GiaTri
            if LoaiSanh.objects.count() >= num:
                messages.warning(request, 'Vượt quá giới hạn loại sảnh')
            else:
                form.save()
                messages.success(request, "Thêm loại sảnh thành công")
        else:
            messages.warning(request, "Thông tin loại sảnh không hợp lệ")
    else:
        form = ThemLoaiSanh()
    
    return render(request, 'tieccuoi/themloaisanh.html', {'form': form})

def view_DatTiec(request):
    if request.method == 'POST':
        form = DatTiecCuoi(request.POST)
        if form.is_valid():
            ngay = form.cleaned_data['Ngay']
            ca = form.cleaned_data['TenCa']
            q = DatTiec.objects.filter(Ngay=ngay, TenCa=ca)
            if not q:
                SLToiDa = Sanh.objects.get(TenSanh=form.cleaned_data['MaSanh']).SoLuongBan
                SoBan = form.cleaned_data['SoLuongBan'] + form.cleaned_data['SLDuTru']
                if SoBan > SLToiDa:
                    messages.warning(request, f'Sảnh không đủ lượng bàn ({SLToiDa})')
                else:
                    m = form.save()

                    tongMonAn = sum([x.DonGia for x in m.DSMonAn.all()]) * SoBan
                    tongDichVu = sum([x.DonGia for x in m.DSDichVu.all()])
                    tongTienBan = tongMonAn + tongDichVu
                    print(tongTienBan)
                    
                    if tongTienBan < m.TienDatCoc:
                        messages.success(request, f'Thêm tiệc thành công (tiền thừa {m.TienDatCoc-tongTienBan})')
                    else:
                        hd = HoaDon(MaTiecCuoi=m, TongTienHoaDon=tongTienBan, ConLai=tongTienBan-m.TienDatCoc)
                        hd.save()
                        messages.success(request, 'Thêm tiệc cưới thành công')
            else:
                messages.warning(request, 'Đã tồn tại ca trong ngày')
        else:
            messages.warning(request, "Thông tin tiệc cưới không hợp lệ")

    else:
        form = DatTiecCuoi()

    return render(request, 'tieccuoi/dattieccuoi.html', {'form': form})

def view_ThemMonAn(request):
    if request.method == 'POST':
        form = ThemMonAn(request.POST)
        if form.is_valid():
            num = ThamSo.objects.filter(TenThamSo='MaxMonAn')[0].GiaTri
            if MonAn.objects.count() >= num:
                messages.warning(request, 'Vượt quá giới hạn món ăn')
            else:
                form.save()
                messages.success(request, 'Thêm món ăn thành công')
        else:
            messages.warning(request, 'Thông tin không hợp lệ')
    else:
        form = ThemMonAn()

    table = MonAn.objects.all()
    return render(request, 'tieccuoi/themmonan.html', {'form': form, 'table': table})

def view_ThemDichVu(request):
    if request.method == 'POST':
        form = ThemDichVu(request.POST)
        if form.is_valid():
            num = ThamSo.objects.filter(TenThamSo='MaxDichVu')[0].GiaTri
            if DichVu.objects.count() >= num:
                messages.warning(request, 'Vượt quá giới hạn dịch vụ')
            else:
                form.save()
                messages.success(request, 'Thêm dịch vụ thành công')
        else:
            messages.warning(request, 'Thông tin không hợp lệ')
    else:
        form = ThemDichVu()

    table = DichVu.objects.all()
    return render(request, 'tieccuoi/themdichvu.html', {'form': form, 'table': table})

def view_TraCuu(request):
    q = DatTiec.objects.select_related('MaSanh').annotate(Sanh=F('MaSanh__TenSanh')).order_by('-Ngay')[:20]
    if request.method == 'POST':
        q = DatTiec.objects.select_related('MaSanh').annotate(Sanh=F('MaSanh__TenSanh'))
        form = TraCuu(request.POST)
        if form.is_valid():
            print(q[0].Ngay)
            print(form.cleaned_data['Ngay'])
            if day := form.cleaned_data['Ngay']:
                q = q.filter(Ngay=day)
            if CoDau := form.cleaned_data['CoDau']:
                q = q.filter(TenCoDau=CoDau)
            if ChuRe := form.cleaned_data['ChuRe']:
                q = q.filter(TenChuRe=ChuRe)
            if Sanh := form.cleaned_data['Sanh']:
                q = q.filter(MaSanh__TenSanh=Sanh)
            if dt := form.cleaned_data['SDT']:
                q = q.filter(SDT=dt)
        else:
            messages.warning(request, 'Không hợp lệ')
    else:
        form = TraCuu()

    return render(request, 'tieccuoi/tracuu.html', {'form': form, 'table': q})

def view_HoaDon(request):
    table = HoaDon.objects.filter().annotate(Ngay=F('MaTiecCuoi__Ngay')).order_by('-ConLai')[:20]
    if request.method == 'POST':
        form = LapHoaDon(request.POST)
        if form.is_valid():
            id = form.cleaned_data['MaTiecCuoi']
            thanhtoan = form.cleaned_data['SoTien']

            if q := HoaDon.objects.filter(MaTiecCuoi=id):
                if q[0].ConLai > 0:
                    if (q[0].ConLai > thanhtoan):
                        q[0].ConLai -= thanhtoan
                        q[0].save()
                        messages.success(request, f'Thanh toán số tiền {thanhtoan} cho tiệc cưới {id}')
                    else:
                        messages.success(request, f'Thanh toán tiệc cưới {id}, tiền thừa {thanhtoan - q[0].ConLai}')
                        q[0].ConLai = 0
                        q[0].save()
                else:
                    messages.warning(request, 'Hóa đơn đã thanh toán')
            else:
                messages.warning(request, 'Tiệc cưới không tồn tại')
        else:
            messages.warning(request, 'Thông tin không hợp lệ')
    else:
        form = LapHoaDon()

    return render(request, 'tieccuoi/hoadon.html', {'form': form, 'table': table})