# Proyek Akhir - Program Rekap dan Analisis Nilai Matematika
Nama: Siti Nurjanah  
NIM: 2225250110  
Kelas: S1 Pendidikan Matematika - Semester 3  

## Deskripsi
Aplikasi Python berbasis terminal yang dirancang untuk membantu guru matematika dalam mengolah file nilai siswa, memvalidasi rentang nilai, mengkalkulasi statistik kelas, dan mencetak laporan ketuntasan berdasarkan KKM secara otomatis.

## Fitur Utama
- Membaca dan memvalidasi file input nilai siswa.
- Mengabaikan input tidak valid (nilai < 0 atau > 100).
- Menghitung nilai rata-rata, nilai tertinggi, dan nilai terendah.
- Mengelompokkan status ketuntasan siswa berdasarkan batas KKM (60).
- Menyimpan hasil rekapitulasi ke file teks `laporan_rekap.txt`.

## Persyaratan
- Python 3.x

## Cara Menjalankan
Buka terminal VS Code pada direktori utama proyek, lalu jalankan:
```bash
python src/main.py