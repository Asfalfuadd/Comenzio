# Mengambil input untuk soal 1
soal_1 = input('''
Cari hasil penjumlahan di bawah ini
2 + 3 ?
a. 3
b. 5
c. 6

Jawab: ''')

# Mengambil input untuk soal 2
soal_2 = input('''
Cari hasil perkalian di bawah ini
10 x 2 x 2 ? 
a. 40
b. 90
c. 400

Jawab: ''')

# Menentukan nilai berdasarkan jawaban
nilai_soal_1 = 0
nilai_soal_2 = 0

# Cek jawaban soal 1
if soal_1 == 'b':
    nilai_soal_1 = 50  # Jawaban benar
else:
    nilai_soal_1 = 0   # Jawaban salah

# Cek jawaban soal 2
if soal_2 =='a':
    nilai_soal_2 = 50  # Jawaban benar
else:
    nilai_soal_2 = 0   # Jawaban salah

# Menghitung total nilai
total_nilai = nilai_soal_1 + nilai_soal_2

# Menampilkan hasil
print(f"Total Nilai:", total_nilai)
