import os

BATAS_KKM = 60

def baca_data(path_file):
    if not os.path.exists(path_file):
        print(f"[ERROR] File '{path_file}' tidak ditemukan.")
        return None
    
    data_siswa = {}
    with open(path_file, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            parts = line.split(',')
            if len(parts) == 2:
                nama, str_nilai = parts[0].strip(), parts[1].strip()
                try:
                    nilai = float(str_nilai)
                    if 0 <= nilai <= 100:
                        data_siswa[nama] = nilai
                    else:
                        print(f"[ABAIKAN] Nilai {nama} ({nilai}) di luar rentang 0-100.")
                except ValueError:
                    print(f"[ABAIKAN] Format nilai {nama} tidak valid.")
    return data_siswa

def hitung_statistik(data_siswa):
    if not data_siswa:
        return {"rata_rata": 0, "min": 0, "max": 0, "total_siswa": 0}
    
    nilai_list = list(data_siswa.values())
    return {
        "total_siswa": len(nilai_list),
        "rata_rata": sum(nilai_list) / len(nilai_list),
        "min": min(nilai_list),
        "max": max(nilai_list)
    }

def analisis_ketuntasan(data_siswa, kkm=BATAS_KKM):
    tuntas = {nama: val for nama, val in data_siswa.items() if val >= kkm}
    belum_tuntas = {nama: val for nama, val in data_siswa.items() if val < kkm}
    return tuntas, belum_tuntas

def simpan_laporan(path_output, statistik, tuntas, belum_tuntas):
    with open(path_output, 'w', encoding='utf-8') as f:
        f.write("=== LAPORAN REKAPITULASI NILAI MATEMATIKA ===\n")
        f.write(f"Total Siswa Valid : {statistik['total_siswa']}\n")
        f.write(f"Rata-Rata Kelas   : {statistik['rata_rata']:.2f}\n")
        f.write(f"Nilai Tertinggi   : {statistik['max']}\n")
        f.write(f"Nilai Terendah    : {statistik['min']}\n\n")
        
        f.write(f"--- SISWA TUNTAS (>= {BATAS_KKM}) : {len(tuntas)} Siswa ---\n")
        for nama, val in tuntas.items():
            f.write(f"- {nama}: {val}\n")
            
        f.write(f"\n--- SISWA BELUM TUNTAS (< {BATAS_KKM}) : {len(belum_tuntas)} Siswa ---\n")
        for nama, val in belum_tuntas.items():
            f.write(f"- {nama}: {val}\n")
    print(f"[BERHASIL] Laporan disimpan ke '{path_output}'.")

def main():
    path_input = os.path.join("data", "nilai_contoh.txt")
    path_output = "laporan_rekap.txt"
    
    print("--- Memulai Program Rekap Nilai Matematika ---")
    data = baca_data(path_input)
    if data is None or len(data) == 0:
        print("[GAGAL] Tidak ada data valid untuk diproses.")
        return

    stats = hitung_statistik(data)
    tuntas, belum_tuntas = analisis_ketuntasan(data)

    print("\n--- RINGKASAN HASIL ANALISIS ---")
    print(f"Total Siswa Valid : {stats['total_siswa']}")
    print(f"Rata-Rata Kelas   : {stats['rata_rata']:.2f}")
    print(f"Nilai Maksimum    : {stats['max']}")
    print(f"Nilai Minimum     : {stats['min']}")
    print(f"Jumlah Tuntas     : {len(tuntas)}")
    print(f"Belum Tuntas      : {len(belum_tuntas)}")

    simpan_laporan(path_output, stats, tuntas, belum_tuntas)

if __name__ == "__main__":
    main()