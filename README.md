# Pertemuan 06 Nested Loop Python

Nama: Alya Mutiara Marine
NIM: 2225250224
Kelas: 3A

## Tujuan
Menggunakan nested loop, pola, akumulasi, dan pencacahan.

## Cara Menjalankan
```bash
python tugas/tabel_perkalian_dan_statistik.py
```

## Algoritma Tugas 3
1. **Loop Luar (i):** Mengontrol baris dari 1 sampai n.
2. **Loop Dalam (j):** Mengontrol kolom dari 1 sampai n untuk setiap baris i.
3. **Akumulator:** `total_baris` menjumlahkan hasil perkalian di baris aktif, dan `total_semua` menjumlahkan seluruh hasil perkalian tabel.
4. **Counter:** `count_genap` bertambah 1 setiap kali variabel `hasil` (i * j) bernilai genap.

## Hasil Pengujian
Berdasarkan pengujian di terminal, program berjalan sukses dan sesuai dengan *Test Case Wajib*:

*   **Input `n = 1`** -> Keluaran Aktual: `1 1`, Total: `1`, Genap: `0` (Status: **Lolos**)
*   **Input `n = 2`** -> Keluaran Aktual: baris 1 (`1 2 3`), baris 2 (`2 4 6`), Total Keseluruhan: `9`, Genap: `3` (Status: **Lolos**)
*   **Input `n = 3`** -> Keluaran Aktual: baris 1 (`1 2 3 6`), baris 2 (`2 4 6 12`), baris 3 (`3 6 9 18`), Total Keseluruhan: `36`, Genap: `5` (Status: **Lolos**)

## Analisis Efisiensi
Untuk input `n`, badan loop dalam akan berjalan sebanyak **\(n^2\)** (n kuadrat) kali. Hal ini karena loop luar berjalan sebanyak `n` kali, dan di setiap iterasinya, loop dalam juga berjalan sebanyak `n` kali.

## Refleksi
### Refleksi Teknis
*   **Mengapa `total_baris` direset di setiap iterasi loop luar?** 
    Agar perhitungan jumlah nilai hanya berlaku untuk baris yang sedang diproses saat itu, sehingga tidak bercampur dengan jumlah dari baris sebelumnya.
*   **Mengapa `total_semua` tidak direset di setiap baris?** 
    Karena `total_semua` berfungsi sebagai akumulator global untuk menghitung total keseluruhan nilai dari semua baris di tabel dari awal sampai akhir.
*   **Untuk n, berapa kali pernyataan `hasil = i * j` dieksekusi?** 
    Dieksekusi sebanyak **\(n \times n\)** atau **\(n^2\)** kali.
*   **Bagaimana Anda membuktikan `count_genap` benar?** 
    Dengan memeriksa kondisi operasi modulus `hasil % 2 == 0`. Jika sisa bagi hasil perkalian dengan 2 adalah 0, maka angka tersebut terbukti genap dan counter bertambah.
*   **Apa bagian program yang akan paling banyak melakukan operasi ketika n membesar?** 
    Bagian operasi di dalam blok loop paling dalam (nested loop), yaitu baris: `hasil = i * j`, akumulasi variabel, dan pengecekan kondisi `if`.

### Perbaikan Kesalahan
Salah satu kesalahan *nested loop* yang ditemukan sebelumnya adalah penutupan blok komentar multi-baris (`'''`) yang sempat tertulis salah menggunakan tanda titik (`...`), yang menyebabkan munculnya `SyntaxError`. Masalah ini diperbaiki dengan memastikan karakter penutup string multi-baris ditulis secara tepat menggunakan tiga tanda petik tunggal (`'''`).