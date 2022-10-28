from turtle import pen
print("implementasi logika fuzzy")
a_kinerjakaryawan = input("masukkan kinerja karyawan :")

kinerjakaryawan = float(a_kinerjakaryawan)

if kinerjakaryawan < 1.01:
    k_alpa = 7
    k_sakit = 3
    k_terlambat = 5

if kinerjakaryawan == 1.01 and kinerjakaryawan <2.10:
    k_alpa = 2
    k_sakit = 0
    k_terlambat = 1

if kinerjakaryawan  > 0.75:
    k_alpa = 1
    k_sakit = 0
    k_terlambat = 3

if kinerjakaryawan < 0.87:
    k_alpa = 2
    k_sakit = 0
    k_terlambat = 0

if kinerjakaryawan < 0.7:
    k_alpa = 1
    k_sakit = 2
    k_terlambat = 0
    
print("penilaian kinerjakaryawan :")
print("karyawan rajin =", k_alpa)
print("karyawan sehat =", k_sakit)
print("karyawan tepat waktu =", k_terlambat)
