# AAS Shimadzu AA-7000 — Virtual Lab

Aplikasi pembelajaran Spektrofotometri Serapan Atom (AAS) dengan halaman HTML, grafik, kalkulator analitik, dan model instrumen 3D berbasis Three.js. Streamlit berfungsi sebagai pembungkus untuk menjalankan halaman ini dan mempermudah deployment ke Streamlit Community Cloud.

## Isi repositori

- `app.py` — aplikasi Streamlit yang memuat halaman HTML.
- `index.html` — antarmuka Virtual Lab dan logika JavaScript/Three.js.
- `requirements.txt` — dependensi Python.

## Jalankan di komputer sendiri

Gunakan Python yang kompatibel dengan Streamlit 1.56.0.

```bash
python -m venv .venv
```

Aktifkan lingkungan virtual:

**Windows (PowerShell)**

```powershell
.\.venv\Scripts\Activate.ps1
```

**macOS/Linux**

```bash
source .venv/bin/activate
```

Pasang dependensi dan jalankan:

```bash
python -m pip install -r requirements.txt
streamlit run app.py
```

Streamlit akan memberikan alamat lokal yang dapat dibuka di browser.

## Unggah ke GitHub

1. Ekstrak folder proyek ini.
2. Buat repositori baru di GitHub.
3. Unggah **isi folder proyek** (bukan hanya file ZIP): `app.py`, `index.html`, `requirements.txt`, `README.md`, dan `.gitignore`.
4. Pastikan `app.py` dan `index.html` berada pada folder yang sama di root repositori.

## Deploy ke Streamlit Community Cloud

1. Buka <https://share.streamlit.io/> dan masuk dengan akun Anda.
2. Pilih **Create app**.
3. Pilih repositori GitHub, branch (umumnya `main`), dan entrypoint `app.py`.
4. Tekan **Deploy**. Setelah proses selesai, Streamlit akan memberikan URL publik berakhiran `streamlit.app` yang dapat dibagikan.

Panduan resmi: <https://docs.streamlit.io/deploy/streamlit-community-cloud/deploy-your-app/deploy>

## Catatan teknis

- Browser pengunjung memerlukan akses internet karena Tailwind CSS, Chart.js, Three.js, Font Awesome, dan font dimuat dari CDN.
- Visualisasi 3D memerlukan dukungan WebGL pada browser/perangkat.
- Ini adalah simulator pembelajaran, bukan pengganti instrumen AAS atau hasil pengujian laboratorium terverifikasi.
- Daftar nama lengkap dan NIM Kelompok 5 tetap ditampilkan di halaman beranda untuk keperluan penilaian dosen. Karena repositori dan aplikasi publik dapat diakses umum, pastikan publikasi identitas ini sesuai dengan persetujuan anggota kelompok.
- Jangan memasukkan kata sandi, token, data laboratorium rahasia, atau data pribadi ke repositori publik.
