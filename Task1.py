# Pertama, program mengimpor modul datetime untuk dapatkan tahun saat ini.
from datetime import datetime

# fungsi input untuk inputan whole number
num = int(input("Enter a whole number: "))

# fungsi untuk  menampilkan tanggal dan waktu
tahun_sekarang = datetime.now().year

# fungsi cek perhitungan hari per tahun kabisat atau bukan jika tahun kabisat maka jumlah hari 366 bukan 365
hari_dalam_setahun = 365 if tahun_sekarang % 4 != 0 else 366

# hasil pembagian bilangan bulan
result = num / hari_dalam_setahun

# print hasil
print(f"Result: {result}")
