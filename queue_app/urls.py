from django.urls import path
from . import views

urlpatterns = [
    # ================= RUTE HALAMAN WEB (TAMPILAN UI) =================
    # Halaman utama (Layar TV Monitor) saat membuka https://iot-4-three.vercel.app/
    path('', views.home, name='index'), # Disesuaikan dengan nama fungsi "home" di views.py
    
    # Halaman Kiosk Registrasi
    path('registrasi/', views.registrasi_view, name='registrasi'), 
    
    # Halaman Tiket di HP Pengunjung
    path('tiket-mobile/', views.mobile_view, name='mobile'), 
    # ==================================================================


    # ================= RUTE API (UNTUK ESP32 & JAVASCRIPT) =================
    path('api/antrean/ambil/', views.ambil_antrean, name='ambil_antrean'),
    path('api/antrean/status/', views.status_antrean, name='status_antrean'),
    path('api/antrean/panggil/', views.panggil_antrean, name='panggil_antrean'),
    
    # Tambahan rute baru untuk fitur Kasir/Admin
    path('api/antrean/selesai/', views.selesai_antrean, name='selesai_antrean'),
    path('api/antrean/lewati/', views.lewati_antrean, name='lewati_antrean'),
    
    path('api/antrean/reset/', views.reset_antrean, name='reset_antrean'), 
    
    # ======== RUTE BARU: UNTUK TABEL DI LAYAR TV ========
    path('api/antrean/daftar/', views.daftar_antrean_api, name='daftar_antrean_api'),
    # =======================================================
]
