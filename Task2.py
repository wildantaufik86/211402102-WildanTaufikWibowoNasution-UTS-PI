# Membuat fungsi inputan untuk memasukan angka
num = int(input("Enter a number: "))

# inisiai variable product dengan nilai 1
product = 1

# perulangan untuk melakukan perkalian
for i in range(1, num+1):
    # setiap interasi i dikalikan dengan produck menggunakan operator *=
    product *= i

# cetak hasil program dengan f string
print(f"Product: {product}")
