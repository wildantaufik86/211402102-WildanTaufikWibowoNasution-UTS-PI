# import library atau module yang dibutuhkan
from datetime import datetime, timedelta

# Membuat fungsi input
days = int(input("Enter number of days: "))

# fungsi untuk menghitung tanggal di saat ini menuju ke tanggal masa depan
# tanggal sekarang di tambah dengan tanggal inputan menghasilkan output tanggal masadepan
tanggal_future = datetime.now() + timedelta(days=days)

# Tanggal di masa depan dicetak dalam format yang diminta (%A on %d %B %Y) menggunakan metode strftime
# atau sebagai date parser
print(f"Date {days} days from now: {tanggal_future.strftime('%A on %d %B %Y')}")
