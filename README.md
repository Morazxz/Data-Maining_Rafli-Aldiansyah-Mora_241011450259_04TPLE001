Data Mining Siswa SMK
Proyek ini dibuat untuk mempelajari proses pengumpulan (loading), pemeriksaan, pengelompokan, dan visualisasi data menggunakan Python. Proyek utama menggunakan dataset siswa SMK yang disimpan dalam format CSV. Terdapat juga program latihan tambahan untuk menganalisis dataset Iris.
Tujuan Proyek
Memuat dataset CSV menggunakan Pandas.
Mengidentifikasi kolom kategorikal dan numerikal.
Menghitung jumlah nilai unik pada kolom kategorikal dan menampilkan statistik deskriptif kolom numerikal.
Memeriksa data kosong (null), baris duplikat, dan nilai nol (zero).
Mengisi nilai kosong pada salinan data menggunakan metode imputasi jika diperlukan.
Menampilkan ringkasan data melalui visualisasi Matplotlib.
Mempraktikkan analisis statistik sederhana pada dataset Iris.
Struktur Folder
```text
data_mining_smk/
├── .venv/                              # Lingkungan virtual Python (jika digunakan)
├── .gitignore                          # Daftar file/folder yang diabaikan Git
├── dataset_siswa_smk_kuliah_2500.csv   # Dataset utama siswa SMK
├── Iris.csv                            # Dataset Iris untuk latihan tambahan
├── requirements.txt                    # Daftar dependensi Python
├── smk.py                              # Analisis dataset siswa SMK
├── tugas.py                            # Analisis dataset Iris
└── README.md                           # Dokumentasi proyek
```
Teknologi dan Library
Python — bahasa pemrograman.
NumPy — operasi numerik, termasuk menghitung nilai nol.
Pandas — membaca CSV, mengelola data, menghitung nilai kosong dan duplikat, serta statistik deskriptif.
scikit-learn — `SimpleImputer` untuk mengisi nilai kosong pada salinan dataset jika diperlukan.
Matplotlib — membuat grafik ringkasan data.
Persiapan
Pastikan Python sudah terpasang. Buka terminal pada folder proyek, lalu (opsional) buat dan aktifkan lingkungan virtual.
Windows (Git Bash):
```bash
python -m venv .venv
source .venv/Scripts/activate
```
Windows (Command Prompt):
```bat
python -m venv .venv
.venv\Scripts\activate
```
Instal dependensi:
```bash
python -m pip install -r requirements.txt
```
Pastikan `requirements.txt` mencantumkan library yang digunakan, misalnya:
```text
numpy
pandas
matplotlib
scikit-learn
```
Menjalankan Program
1. Analisis dataset siswa SMK
Pastikan file `dataset_siswa_smk_kuliah_2500.csv` berada di folder yang sama dengan `smk.py`. Jalankan:
```bash
python smk.py
```
Program akan menampilkan informasi ukuran dataset, contoh lima baris pertama, jenis kolom, nilai unik pada kolom kategorikal, statistik deskriptif kolom numerikal, jumlah data duplikat, nilai null, dan nilai zero pada kolom numerikal.
Program juga membuat grafik jumlah kolom kategorikal dan numerikal serta grafik nilai null dan zero per kolom.
Catatan: Pengisian nilai null dilakukan pada salinan data (`cleaned_data`), bukan pada file CSV asli. Hasil imputasi tidak disimpan kembali ke CSV. Nilai zero dihitung khusus pada kolom numerikal dan tidak otomatis dianggap sebagai data yang salah.
2. Analisis dataset Iris
Pastikan `Iris.csv` berada di folder yang sama dengan `tugas.py`. Jalankan:
```bash
python tugas.py
```
Program ini menampilkan:
Lima baris pertama dan ukuran dataset.
Informasi kolom serta jumlah nilai kosong.
Jumlah baris duplikat.
Statistik deskriptif.
Jumlah data untuk setiap spesies.
Rata-rata `PetalLengthCm`.
Grafik batang jumlah spesies.
Scatter plot hubungan `PetalLengthCm` dan `PetalWidthCm` untuk setiap spesies.
Ringkasan Fitur
Fitur	`smk.py`	`tugas.py`
Membaca dataset CSV	Dataset siswa SMK	Dataset Iris
Menampilkan contoh data dan ukuran	Ya	Ya
Pemeriksaan nilai null	Ya	Ya
Pemeriksaan baris duplikat	Ya	Ya
Statistik deskriptif	Kolom numerikal	Dataset numerikal
Analisis kolom kategorikal	Ya	Jumlah spesies
Menghitung nilai zero numerikal	Ya	Tidak secara khusus
Imputasi nilai null pada salinan data	Ya	Tidak
Visualisasi	Ringkasan tipe kolom dan kualitas data	Grafik spesies dan scatter plot
Catatan Penggunaan
Nama file dan nama kolom harus sesuai dengan yang digunakan pada kode.
`smk.py` mencari dataset utama berdasarkan lokasi file Python, sehingga program dapat dijalankan dari folder proyek.
`tugas.py` membaca `Iris.csv` menggunakan nama file relatif. Jalankan program dari folder proyek agar file dapat ditemukan.
Jika muncul `FileNotFoundError`, periksa nama file, ejaan, dan lokasi dataset.
Grafik Matplotlib akan muncul dalam jendela terpisah. Tutup jendela grafik untuk melanjutkan atau mengakhiri program.
Hasil analisis mengikuti isi dataset yang digunakan. Periksa sumber dan kualitas dataset sebelum menarik kesimpulan.
Lisensi
Belum ditentukan. Tambahkan informasi lisensi apabila proyek akan dibagikan atau digunakan oleh pihak lain.
