#INPUT SEBELUM CEK UMUR
nama_pembeli = input    ("Masukkan nama pembeli                   : ")
Umur_pembeli = int(input("Masukkan umur anda (angka)              : "))

#VARIABEL TAMBAHAN
harga_tiket = 0
diskon = 0
kembalian = 0
biaya_admin = 0
struk_valid = True

if Umur_pembeli < 13:
    print ("Mohon maaf, anda belum cukup umur untuk menonton")
else:
    #INPUT SETELAH PENGECEKAN UMUR
    Jenis_tiket =  input("Bioskop ini menyediakan 3 jenis tiket, \n" \
                     "Reguler    : Rp.50.000\n" \
                     "Premium    : Rp.75.000\n" \
                     "VIP        : Rp.100.000\n" \
                     "Pilihlah salah satu (misal: 'VIP')      : ")
   
    #Menentukan Harga Tiket
    if Jenis_tiket == "Reguler":
        harga_tiket = 50000
    elif Jenis_tiket == "Premium":
        harga_tiket = 75000
    elif Jenis_tiket == "VIP": #Kenapa nda pake else? karena akan #menimbulkan konflik jika pengguna memasukkan huruf lain
        harga_tiket = 100000
    else:
        print ("Peringatan: karena anda memasukkan data yang salah, kemungkinan besar program akan eror saat pencetakan struk. " \
             "\n            kami sarankan untuk mengulang kembali program dan memasukkan data yang benar!")
        struk_valid = False

    #Pengecekkan status member
    status_member = input         ("Apakah anda member ('ya'/'tidak')       : ")
    if status_member == "tidak":
        print ("karena anda bukan member, anda akan dikenakan biaya admin sebesar Rp.2.000 untuk setiap pembelian")
    elif status_member == "ya":
        print("karena anda member, semua biaya tiket anda akan dikenakan diskon sebesar 20%\n" )
    else:
            print ("Peringatan: karena anda memasukkan data yang salah, kemungkinan besar program akan eror saat pencetakan struk. " \
                 "\n            kami sarankan untuk mengulang kembali program dan memasukkan data yang benar!")
            struk_valid = False
           
   
    #Meminta Uang Pembayaran
    Nominal_uang_bayar = int(input("Masukkan Nominal Uang Bayar(angka)      : "))

    #Memberikan diskon apabila member
    diskon = 0.2 if status_member == "ya" else 0

    #Memberikan biaya_admin apabila suki
    biaya_admin = 2000 if status_member == "tidak" else 0
   
    #Menghitung Harga Akhir
    harga_tiket = harga_tiket + biaya_admin - harga_tiket * diskon #TOTAL HARGA
    kembalian = Nominal_uang_bayar - harga_tiket
    if struk_valid != True:
        print("Salah satu data yang anda masukkan tidak valid. Silahkan ulangi program dan coba lagi!")
    elif kembalian < 0:
        print ("Maaf, uang anda tidak cukup")
    else:
        print ("Terimakasih sudah menggunakan layanan ini. berikut struk anda: \n",
            "Nama         :", nama_pembeli, "\n",
            "Umur         :", Umur_pembeli, "\n",
            "Jenis Tiket  :" ,Jenis_tiket, "\n",
            "Status Member:" ,status_member, "\n",
            "Total Bayar  :" ,harga_tiket, "\n",
            "Kembalian    :", kembalian)
       