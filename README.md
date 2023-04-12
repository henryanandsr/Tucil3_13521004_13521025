# Implementasi Algoritma UCS dan A* untuk Menentukan Lintasan Terpendek
Tugas Kecil 3 IF2211 Strategi Algoritma "Implementasi Algoritma *UCS* dan *A**".

## Authors

| Nama                  | NIM      |
| --------------------- | -------- |
| Henry Anand Septian Radityo | 13521004 |
| Muhammad Haidar Akita Tresnadi          | 13521025 |

## Deskripsi
Pencarian rute terpendek menjadi dasar dalam banyak aplikasi, seperti perencanaan rute pada navigasi GPS, optimasi pengiriman barang, pengaturan lalu lintas, dan sebagainya. Algoritma A* dan UCS digunakan untuk mencari rute terpendek antara dua titik dalam suatu graf atau peta yang direpresentasikan sebagai sebuah graf. Graf tersebut terdiri dari simpul (node) yang mewakili lokasi atau titik dalam peta, dan tepi (edge) yang menghubungkan antara dua simpul yang dapat dilalui. Program ini dibuat menggunakan bahasa python dan divisualisasikan dengan flask web framework serta Tailwindcss.

## Requirement
- Python
```bash
Python Library : 
- Matplotlib
- flask
- NetworkX
- Folium
```
- Tailwind
- Nodejs

## Run Program
1. Git clone atau download zip file
2. Pastikan node js sudah terinstall, buka command prompt atau terminal pada directory static
3. Jalankan perintah: npx tailwindcss -i ./src/input.css -o ./dist/output.css --watch
4. Setelah selesai, jalankan program app.py yang ada pada folder src
5. Jika Berhasil, tampilan program dapat dilihat di browser pada localhost dengan port 5000 (http://127.0.0.1:5000)

