from django.db import models

class Antrean(models.Model):
    STATUS_CHOICES = (
        ('menunggu', 'Menunggu'),
        ('proses', 'Sedang Proses'), 
        ('selesai', 'Selesai'),
        ('terlewati', 'Terlewat / Tidak Hadir'), 
    )
    
    nomor_antrean = models.IntegerField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='menunggu')
    waktu_dibuat = models.DateTimeField(auto_now_add=True)
    waktu_dipanggil = models.DateTimeField(null=True, blank=True)

    # Data Pengunjung
    nama = models.CharField(max_length=100, null=True, blank=True)
    nim = models.CharField(max_length=50, null=True, blank=True)
    keperluan = models.CharField(max_length=100, null=True, blank=True)

    class Meta:
        ordering = ['waktu_dibuat']

    def __str__(self):
        nama_tampil = self.nama if self.nama else 'Anonim'
        return f"Antrean {self.nomor_antrean} - {nama_tampil} ({self.get_status_display()})"