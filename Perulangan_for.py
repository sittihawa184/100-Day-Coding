baris = 7
for baris in range(1, baris+1):
    for kolom in range(1, baris+ 1):
        print(kolom, end= '   ')
    print("   ")

for angka in range(kolom):
    for i in range(angka):
        print(angka,  end= '   ')
    print("    ")

for i in range(kolom,0, -1):
    angka = i
    for j in  range(0,i):
        print(angka,  end= '   ')
    print("    ")
