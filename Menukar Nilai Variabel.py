#Mengimput Nilai Variabel

text1=input(" Variabel: ")
text2=input(" Variabel2: ")
text3=input(" Variabel3: ")
text4=input(" Variabel4: ")

#Membuat Variabel Tukar dan Menukar nilai variabel lain
tukar=text1
text1=text2
text2=text1
text2=tukar
tukar=text3
text3=text4
text4=text3
text4=tukar

#menampilkan nilai variabel setelah ditukar
print('nilai variabel1 setelah ditukar adalah:{}'.format(text1))
print('nilai variabel2 setelah ditukar adalah:{}'.format(text2))
print('nilai variabel3 setelah ditukar adalah:{}'.format(text3))
print('nilai variabel4 setelah ditukar adalah:{}'.format(text4))
