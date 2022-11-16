# Program membuat kalkulator sederhana, yang dapat menambah,mengurangi, mengalikan dan membagi menggunakan fingsi
# Fungsi ini menambahkan dua angka
def add(x, y):
   return x + y
# Fungsi ini mengurangi dua angka
def subtract(x, y):
   return x - y
# Fungsi ini mengalikan dua angka
def multiply(x, y):
   return x * y
# Fungsi ini membagi dua bilangan
def divide(x, y):
   return x / y
print("Pilih Operasi.")
print("1.Tmbah")
print("2.Kurang")
print("3.Kali")
print("4.Bagi")
# Menerima masukan dari pengguna
choice = input("Masukkan Pilihan(1/2/3/4):")
num1 = int(input("Masukkan Angka Pertama: "))
num2 = int(input("asukkan Angka Kedua: "))
if choice == '1':
   print(num1,"+",num2,"=", add(num1,num2))
elif choice == '2':
   print(num1,"-",num2,"=", subtract(num1,num2))
elif choice == '3':
   print(num1,"*",num2,"=", multiply(num1,num2))
elif choice == '4':
   print(num1,"/",num2,"=", divide(num1,num2))
else:
   print("Invalid input")
