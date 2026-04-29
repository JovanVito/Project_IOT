from django.urls import path
from . import views

urlpatterns = [
    path('antrean/ambil/', views.ambil_antrean, name='ambil_antrean'),
    path('antrean/status/', views.status_antrean, name='status_antrean'),
    path('antrean/panggil/', views.panggil_antrean, name='panggil_antrean'),
    
    # ================= TAMBAHAN RUTE BARU =================
    path('antrean/selesai/', views.selesai_antrean, name='selesai_antrean'),
    path('antrean/lewati/', views.lewati_antrean, name='lewati_antrean'),
    # ======================================================

    path('antrean/reset/', views.reset_antrean, name='reset_antrean'), 
]