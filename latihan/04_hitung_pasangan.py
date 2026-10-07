n = int(input("n: "))
count = 0
for i in range(1, n + 1):
    for j in range(1, n + 1):
        if i + j <= n:
            count += 1
print(f"Banyak pasangan = {count}")

'''
===================================================================
TRACING MANUAL UNTUK n = 3
===================================================================
Nilai Awal: count = 0

Loop i | Loop j | Cek Kondisi (i + j <= 3) | Efek ke Variabel | Nilai count Baru
--------------------------------------------------------------------------------
1      | 1      | 1 + 1 = 2 <= 3 (Benar)   | count tambah 1   | 1
1      | 2      | 1 + 2 = 3 <= 3 (Benar)   | count tambah 1   | 2
1      | 3      | 1 + 3 = 4 <= 3 (Salah)   | Diabaikan        | 2
2      | 1      | 2 + 1 = 3 <= 3 (Benar)   | count tambah 1   | 3
2      | 2      | 2 + 2 = 4 <= 3 (Salah)   | Diabaikan        | 3
2      | 3      | 2 + 3 = 5 <= 3 (Salah)   | Diabaikan        | 3
3      | 1      | 3 + 1 = 4 <= 3 (Salah)   | Diabaikan        | 3
3      | 2      | 3 + 2 = 5 <= 3 (Salah)   | Diabaikan        | 3
3      | 3      | 3 + 3 = 6 <= 3 (Salah)   | Diabaikan        | 3

Output Akhir Program: Banyak pasangan = 3
===================================================================
'''