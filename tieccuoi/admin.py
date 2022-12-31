from django.contrib import admin
from django.contrib.auth.models import User
from .models import *
# Register your models here.
admin.site.register(Sanh)
admin.site.register(LoaiSanh)
admin.site.register(DatTiec)
admin.site.register(Ca)
admin.site.register(MonAn)
admin.site.register(DichVu)
admin.site.register(HoaDon)
admin.site.register(ThamSo)