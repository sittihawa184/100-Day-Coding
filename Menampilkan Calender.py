#Mengimport Calendar
import  calendar

#mengimput Tahun dan Bulan

tahun= int(input("Masukkan Tahun: "))
bulan= int(input("Masukkan Bulan: "))

#menampilkan Kelender Bulanan
print(calendar.month(tahun,bulan))
