print("Tabel Perkalian dan Statistik")
n = int(input("n: "))

# 1. Baca dan validasi n. Jika n <= 0, minta n kembali sampai valid.
while n <= 0:
    n = int(input("n: "))

# 2. Set total_semua = 0 dan count_genap = 0.
total_semua = 0
count_genap = 0

# 3. Ulangi i dari 1 sampai n.
for i in range(1, n + 1):
    # 4. Set total_baris = 0 untuk baris i.
    total_baris = 0
    
    # 5. Ulangi j dari 1 sampai n.
    for j in range(1, n + 1):
        # 6. Hitung hasil = i * j.
        hasil = i * j
        print(hasil, end=" ")
        
        # 7. Tambahkan hasil ke total_baris dan total_semua.
        total_baris += hasil
        total_semua += hasil
        
        # 8. Jika hasil genap, tambah count_genap.
        if hasil % 2 == 0:
            count_genap += 1
            
    # 9. Setelah loop dalam selesai, tampilkan total_baris.
    print(total_baris)

# 10. Setelah kedua loop selesai, tampilkan total_semua dan count_genap.
print(total_semua)
print(count_genap)