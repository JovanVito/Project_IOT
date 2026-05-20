from django.contrib import admin
from django.urls import path
from queue_app import views # Memanggil views dari aplikasi queue_app kamu

urlpatterns = [
    # Rute bawaan Django Admin
    path('admin/', admin.site.urls),

    # ================= RUTE HALAMAN WEB (TAMPILAN UI) =================
    path('', views.index_view, name='index'), 
    path('registrasi/', views.registrasi_view, name='registrasi'), 
    path('tiket-mobile/', views.mobile_view, name='mobile'), 
    # ==================================================================

    # ================= RUTE API (UNTUK ESP32 & JAVASCRIPT) =================
    path('api/antrean/ambil/', views.ambil_antrean, name='ambil_antrean'),
    path('api/antrean/status/', views.status_antrean, name='status_antrean'),
    path('api/antrean/panggil/', views.panggil_antrean, name='panggil_antrean'),
    
    path('api/antrean/selesai/', views.selesai_antrean, name='selesai_antrean'),
    path('api/antrean/lewati/', views.lewati_antrean, name='lewati_antrean'),
    path('api/antrean/reset/', views.reset_antrean, name='reset_antrean'), 
    path('api/antrean/panggil/', views.panggil_antrean, name='panggil'),
    path('api/antrean/reset/', views.reset_antrean, name='reset'),
    path('api/antrean/daftar/', views.daftar_antrean_api, name='daftar_antrean_api'),
    
    # ======== RUTE BARU: UNTUK TABEL DI LAYAR TV ========
    path('api/antrean/daftar/', views.daftar_antrean_api, name='daftar_antrean_api'),
    # =======================================================================
]
