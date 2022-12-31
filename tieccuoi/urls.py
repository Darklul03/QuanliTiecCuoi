from django.urls import path
# from django.conf.urls import include, url
from . import views
from django.contrib.auth import views as auth_views
from django.contrib import admin

app_name='tieccuoi'

urlpatterns = [
    path('', views.view_Default, name='default'),
    path('tiepnhansanh', views.view_TiepNhanSanh, name="tiepNhan"),
    path('themloaisanh', views.view_ThemLoaiSanh, name="themSanh"),
    path('dattieccuoi', views.view_DatTiec, name="datTiec"),
    path('themmonan', views.view_ThemMonAn, name='themMonAn'),
    path('themdichvu', views.view_ThemDichVu, name='themDichVu'),
    path('tracuu', views.view_TraCuu, name='traCuu'),
    path('hoadon', views.view_HoaDon, name='hoaDon'),
]