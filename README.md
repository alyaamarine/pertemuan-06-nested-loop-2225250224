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

## Refleksi Teknis
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

---

## 11 Kuis Formatif
1. **Total iterasi badan loop dalam:** 24 kali (hasil dari 4 kali loop luar \(\times\) 6 kali loop dalam).
2. **Kapan loop dalam kembali ke nilai awal:** Setiap kali loop luar melangkah ke iterasi atau baris baru berikutnya.
3. **Fungsi `print()` setelah loop dalam pada pola simbol:** Untuk mencetak karakter pindah baris baru (*newline*), sehingga baris simbol berikutnya tercetak di bawahnya secara rapi.
4. **Lokasi inisialisasi `total_baris`:** Di dalam loop luar, tepat sebelum loop dalam dimulai.
5. **Lokasi inisialisasi `total_semua`:** Di luar loop, tepat sebelum seluruh rangkaian perulangan dimulai.
6. **Perbedaan counter dengan accumulator:** Counter digunakan untuk mencacah atau menghitung seberapa banyak suatu kondisi terjadi (bertambah tetap \(+1\)), sedangkan accumulator digunakan untuk menimbun atau menjumlahkan nilai numerik bervariasi secara kumulatif.
7. **Banyak pasangan yang diperiksa jika i dan j dari 1 sampai 3:** 9 pasangan koordinat.
8. **Penggabungan if dengan nested loop untuk pencacahan:** Struktur `if` diletakkan di dalam badan loop terdalam untuk menyaring pasangan indeks yang memenuhi syarat, kemudian jika benar, nilai counter akan dinaikkan.
9. **Arti "working tree clean" pada `git status`:** Semua modifikasi file telah berhasil direkam (di-commit) dan tidak ada perubahan file tersisa yang belum disimpan di repositori lokal.
10. **Perintah mengirim commit lokal terbaru ke GitHub:** `git push origin main` (atau `git push origin master`).

---

## Exit Ticket
*   **Hal yang paling menentukan jumlah iterasi nested loop adalah...** Batas akhir (*range*) iterasi pada kondisi perulangan di loop luar dan loop dalam.
*   **Perbedaan akumulasi per baris dan akumulasi keseluruhan adalah...** Akumulasi per baris selalu direset ke angka 0 setiap kali baris berganti untuk menghitung nilai per kelompok, sedangkan akumulasi keseluruhan nilainya terus bertambah dari awal hingga akhir tanpa pernah direset.
*   **Bagian program Pertemuan 6 yang paling tepat dijadikan fungsi pada Pertemuan 7 adalah...** Blok kode utama *nested loop* yang memproses pembuatan tabel perkalian serta perhitungan statistiknya, karena logika tersebut bersifat modular dan menerima input parameter dinamis berupa nilai variabel `n`.