# Proposal Proyek Akhir - Algoritma dan Pemrograman

## 1. Judul Proyek
Program Rekap dan Analisis Nilai Matematika Kelas

## 2. Latar Belakang
Guru matematika memerlukan program berbasis terminal yang efisien untuk membaca data nilai siswa, memvalidasi rentang nilai, menghitung statistik kelas, menentukan status ketuntasan berdasarkan KKM, serta menyimpan laporan ringkas secara otomatis.

## 3. Pengguna dan Tujuan
* **Pengguna:** Guru Matematika / Pengajar.
* **Tujuan:** Otomatisasi kalkulasi statistik nilai dan rekapitulasi kelulusan siswa secara tepat dan konsisten.

## 4. Ruang Lingkup
* **Fitur Wajib:** Membaca file nilai, memvalidasi input nilai (0-100), menghitung rata-rata/min/max, menentukan jumlah tuntas/belum tuntas (KKM = 60), dan menyimpan laporan ke file teks.
* **Batasan:** Program berbasis terminal Python tanpa antarmuka grafis (GUI).

## 5. Input, Proses, Output (IPO)
* **Input:** File data teks berisi nama dan nilai siswa (`data/nilai_contoh.txt`).
* **Proses:** Validasi nilai (0-100), kalkulasi statistik dasar, filter batas KKM.
* **Output:** Ringkasan di terminal dan penulisan file laporan (`laporan_rekap.txt`).

## 6. Pseudocode Ringkas

MULAI
    baca data dari file
    jika file tidak ditemukan:
        tampilkan pesan error
        SELESAI
    untuk setiap baris:
        validasi nilai 0-100
    hitung rata-rata, min, max
    hitung status KKM (>=60)
    tampilkan ringkasan di terminal
    simpan laporan ke file
SELESAI

## 7. Pembagian Tugas & PIC
- **Siti Nurjanah (NIM: 2225250110):** Programmer Logika & Data I/O (Penyusunan modul, validasi, penulisan laporan, & testing).