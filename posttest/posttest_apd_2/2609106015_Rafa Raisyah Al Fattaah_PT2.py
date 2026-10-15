#kamus dan variabel
Barang_1 = 15000
Barang_2 = 25000
Barang_3 = 10000
Barang_4 = 5500
Barang_5 = 5000
Barang_6 = 20000
LBarang = [Barang_1, Barang_2, Barang_3, Barang_4, Barang_5,  Barang_6]                   
LNamaBarang =["Barang_1","Barang_2","Barang_3","Barang_4","Barang_5","Barang_6"]        
total_bayar = LBarang[0]+LBarang[1]+LBarang[2]+LBarang[3]+LBarang[4]+LBarang[5]
pajak_kopdes = 15/100                                                                      #15/100      = 15%
total_bayar += total_bayar * pajak_kopdes
totalBarang = len(LBarang)                 
rata_rata = total_bayar/totalBarang
nim = 15
bolean = nim < rata_rata

#fotokopi/print-an
print ("\n                              PROGRAM MENGHITUNG TOTAL HARGA BELANJAAN\n")
print ("List Nama Barang                : " + str(LNamaBarang[0:6:1]))
print ("List Harga Barang               : " + str(LBarang[0:6:1]))
print ("Pajak Kopdes                    : " + str(pajak_kopdes * 100) + "%")
print ("Total Sebelum Pajak             : " + str(total_bayar - 12075))
print ("Total Setelah Pajak             : " + str(total_bayar))
print ("Rata-Rata Harga Barang          : " + str(rata_rata))
print ("Nim Mahasiswa(saya)             : " + str(nim))
print ("Apakah Nim saya < Rata-Rata     : " + str(bolean))

#Area Poin Plus

#konversi mata uang
kurs_dolar = 17706
kurs_ringgit = 4377
print ("\n      Tahukah kamu, Total harga barang anda dalam mata uang lain ialah\n\n"
       "Dolar    (USD)                  : $" +   str(total_bayar/kurs_dolar) + "\n"
       "Ringgit  (RM)                   : RM" + str(total_bayar/kurs_ringgit) + "\n")


#tampilkan Barang_1, barang1+2 dengan list slicing
print ("Barang-barang spesial ialah     : " + str(LNamaBarang[0:6:2]))
print ("Harga setiap barang spesial     : " + str(LBarang[0:6:2]) +
       "\n\n               Terima kasih sudah menggunakan program ini <3\n")
