#Mengimput Angka ganjil atau genap
angka1 = int(input("Masukkan Angka : "))
angka2 = int(input("Masukkan Angka2 : "))

#jika angka habis dibagi dengan Nol, Maka genap
if (angka1 % 2) == 0:
    print("{0} adalah bilangan Genap".format(angka1))

#jika tidak habis dibagi Nol, maka Ganjil
else:
    print("{0} Adalah Bilangan Ganjil".format(angka1))

#jika angka habis dibagi dengan Nol, Maka genap
if (angka2 % 2) == 0:
    print("{0} adalah bilangan Genap".format(angka2))

#jika tidak habis dibagi Nol, maka Ganjil
else:
    print("{0} Adalah Bilangan Ganjil".format(angka2))

