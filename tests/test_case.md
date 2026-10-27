# Dokumentasi Test Case Proyek

| ID | Fitur | Input | Expected Result | Status |
|---|---|---|---|---|
| TC01 | Validasi Normal | Nilai 85 | Diterima sebagai nilai valid | PASS |
| TC02 | Batas KKM | Nilai 60 | Status: Tuntas | PASS |
| TC03 | Di Bawah KKM | Nilai 58 | Status: Belum Tuntas | PASS |
| TC04 | Nilai Invalid | Nilai 105 / -5 | Ditolak dengan pesan kesalahan | PASS |
| TC05 | File Tidak Ada | `file_palsu.txt` | Error ditangani dengan aman | PASS |