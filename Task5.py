# Variabel sum_numbers diinisialisasi dengan nilai 4
sum_numbers = 4

# fungsi untuk membuka file yg bernama input.txt
with open("input.txt", "r") as file:
    # perulangan untuk membaca tiap baris dalam file
    for line in file:
        # Setiap baris dibaca dan dikonversi menjadi bilangan bulat.
        # Setiap bilangan bulat yang dibaca dijumlahkan ke variabel sum_numbers.
        sum_numbers += int(line.strip())

# setelah semua terbaca maka akan dicetak kita menggunakan {:,.3f}'.format(sum_numbers)
# menjadi comma separator dan 3 angka dibelakang koma
print('{:,.3f}'.format(sum_numbers))
