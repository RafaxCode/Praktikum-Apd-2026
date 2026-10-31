#CRUD
#Toko mancing
#Cara Membaca List = [nama, ukuran, harga]
#Penggunaan nama #USER xxx #USER Berfungsi untuk mengsubstitusi fungsinya fungsi
#Agar Sang Dev tidak kebingungan dalam mengeread baca kode kodingannya
#POSTTEST_6
#NEW EDIT : Mengganti list menjadi dictionary
#           Target yang mau diganti: DiksiJoran, DiksiUser
#           Hal Baru yang ditambahkan : sistem login user non user
#Reworked deleting mechanism (New Flowchart)
#You know what, all of CRUD and login mechanism is getting reworked
import os
DiksiJoran = { #Diksi Joran
            'Joran_1'   : ['shimano', '150cm', 'RP.200.000'], #<--------- Termasuk Nested List
            'Joran_2'   : ['daiwa', '130cm', 'Rp.125.000'], 
            'Joran_3'   : ['relix nusantara','150cm', 'RP.200.000'],
            'Joran_4'   : ['daido' , '150cm', 'RP.200.000'],
            'Joran_5'   : ['sougayilang', '150cm', 'RP.200.000']
    }

UkuranDiksiJoran = len(DiksiJoran)
DiksiUser = {"Daniel" : "Danie123"}#Username, Password
StatusUser = ""

#Data Admin
username = "John BatuBara"
password = "Tongkang123"


#LOGIN
PilihanA = ""
while PilihanA != "4":
    print("<||||[Selamat Datang Toko Pancing Mahakam Jaya]||||>\n" \
        "Saat ini, anda login sebagai:\n" \
        "1. User\n" \
        "2. Admin \n" \
        "3. Buat Akun\n" \
        "4. Keluar")
    PilihanA = input("Masukkan Pilihan: ")
    if PilihanA == "1":
        StatusUser = "user"
        break
    elif PilihanA == "2":
        StatusUser = "admin"
        break
    elif PilihanA == "3": #Fitur ini cuma untuk mengisi kuota nilai plus
        #Sistem Registrasi
        print("Anda mau buat akun baru? silahkan silahkan!")
        PilihanX = ""
        while PilihanX != "n":
            PilihanX = input("Masukkan Nama     : ")
            PilihanY = input("Masukkan Password : ")
            StatusDuplikat = 0
            for keys in DiksiUser.keys():
                if keys != PilihanX:
                    StatusDuplikat = 0
                else:
                    StatusDuplikat = 1
                    print ("Akun dengan nama itu sudah ada, silahkan coba lagi!")
                    break
            
            if StatusDuplikat == 0:
                DiksiUser.update({PilihanX : PilihanY})

            PilihanX = input("ketik apapun untuk membuat akun lagi!\n" \
                             "ketik n untuk kembali ke menu: ")
        #Sistem Registrasi
    elif PilihanA == "4":
        StatusUser = "none"
    else:
        print("Jangan Masukkan hal lain. Be a human")
#LOGIN

#KLASIFIKASI USER
#ADMIN LOGIN
if StatusUser == "admin":
    StatusLogin = 0 #0 false, 1 true
    percobaan = 0
    while percobaan < 3:
        PilihanX = input("Username: ")
        PilihanY = input("Password: ")
        if PilihanX == username and PilihanY == password:
            StatusLogin = 1
            percobaan += 3                                                                           
            print("                                                         LOGIN BERHASIL")
            print("░███     ░███    ░███    ░██     ░██    ░███    ░██     ░██    ░███    ░███     ░███        ░█████    ░███    ░██     ░██    ░███    \n" \
                  "░████   ░████   ░██░██   ░██     ░██   ░██░██   ░██    ░██    ░██░██   ░████   ░████          ░██    ░██░██    ░██   ░██    ░██░██   \n" \
                  "░██░██ ░██░██  ░██  ░██  ░██     ░██  ░██  ░██  ░██   ░██    ░██  ░██  ░██░██ ░██░██          ░██   ░██  ░██    ░██ ░██    ░██  ░██  \n" \
                  "██ ░████ ░██ ░█████████ ░██████████ ░█████████ ░███████    ░█████████ ░██ ░████ ░██          ░██  ░█████████    ░████    ░█████████\n"   \
                  "░██  ░██  ░██ ░██    ░██ ░██     ░██ ░██    ░██ ░██   ░██   ░██    ░██ ░██  ░██  ░██    ░██   ░██  ░██    ░██     ░██     ░██    ░██ \n" \
                  "░██       ░██ ░██    ░██ ░██     ░██ ░██    ░██ ░██    ░██  ░██    ░██ ░██       ░██    ░██   ░██  ░██    ░██     ░██     ░██    ░██\n"  \
                  "░██       ░██ ░██    ░██ ░██     ░██ ░██    ░██ ░██     ░██ ░██    ░██ ░██       ░██     ░██████   ░██    ░██     ░██     ░██    ░██ ")
        else:
            print("Login Gagal, Silahkan coba lagi")
            percobaan += 1
    if percobaan >= 3 and StatusLogin == 0:
        print("'Karena anda mencoba memasuki laman SAYA, dan gagal secara menyedihkan\n" \
               "saya akan blokir anda' -sincerely, John Sawit")
    #ADMIN LOGIN
    else:
        #menu_admin
        print ("<||||[Selamat Datang menu admin]||||>")
        Pilihan = ""
        while Pilihan != "6":
            print ("Apa yang ingin anda lakukan?\n" \
                "1. Buat Kategori Joran Baru\n" \
                "2. Lihat Joran Yang Sudah Ada\n" \
                "3. Edit Nama Joran\n" \
                "4. Hapus Joran Dari Toko\n" \
                "5. Bersihkan Layar\n" \
                "6. Keluar Dari Aplikasi")
            Pilihan = input("Pilih Aksi: ")

            if Pilihan == "1": #Menambahkan Joran Baru
                PilihanX = ""
                while PilihanX != 'n':
                    UkuranDiksiJoran = len(DiksiJoran) #mengupdate setiap loop
                    ListX = []
                    PilihanX = input("Masukkan Nama Joran Baru: ")
                    ListX.append(PilihanX)
                    PilihanX = input("Masukkan Panjang Joran (cm):")
                    ListX.append(PilihanX + "cm")
                    PilihanX = input("Masukkkan Harga Joran (Rp): ")
                    ListX.append("Rp." + PilihanX)
                    DiksiJoran.update({"Joran_" + str(UkuranDiksiJoran + 1) : ListX})
                    print("Joran Berhasil ditambahkan ke dalam katalog!")
                    PilihanX = input("apakah anda ingin menambahkan joran lagi?\n" \
                                    "ketik 'y' atau huruf lain jika iya\n" #disini kenapa eror pas '\' diletakan, saya tidak tau
                                    "ketik 'n' jika tidak: " )
                                    #Jika itu bekerja, jangan disentuh
                
            elif Pilihan == "2":
                #Melihat Katalog Joran
                PilihanX = ""
                while PilihanX != "n":
                    UkuranDiksiJoran = len(DiksiJoran) #mengupdate setiap loop
                    print ("Nama-Nama Joran di Inventori")
                    count = 0
                    for key in DiksiJoran:
                        count += 1
                        print(str(count) + ".", DiksiJoran[key][0])
                    
                    PilihanX = input("Untuk mengetahui lebih lanjut mengenai joran, ketik 'y', " \
                                    "Untuk kembali ke menu, ketik 'n'\n" \
                                    "Pilihan                          : ")    
                    if PilihanX == 'y':
                        PilihanX = UkuranDiksiJoran 
                        while PilihanX <= UkuranDiksiJoran or PilihanX > 0:
                            PilihanX = input("Pilih Nomor Joran: ")
                            if PilihanX.isdigit():
                                PilihanX = int(PilihanX)
                                if PilihanX > UkuranDiksiJoran or PilihanX < 1:
                                    print("Masukkan Nomor Yang Ada!")
                                else:
                                    print("Nama     :" + DiksiJoran["Joran_" + str(PilihanX)][0] + "\n"
                                          "Ukuran   :" + DiksiJoran["Joran_" + str(PilihanX)][1] + "\n"
                                          "Harga    :" + DiksiJoran["Joran_" + str(PilihanX)][2])
                                    PilihanX = input("Ketik huruf apapun untuk lanjut, huruf 'n' untuk ke menu utama: ")
                                    if PilihanX == 'n':
                                        break
                                    else:
                                        PilihanX = UkuranDiksiJoran
                            elif PilihanX == "n":
                                break
                            else:
                                print("JANGAN MASUKKAN STRING, ANGKA ONLY!")
                                PilihanX = UkuranDiksiJoran
                    else:
                        if PilihanX != 'n':
                            print("Jangan masukkan huruf lain!")
            
            elif Pilihan == "3": #Edit Joran
                PilihanX = ""
                while PilihanX != "n":
                    UkuranDiksiJoran = len(DiksiJoran) #mengupdate setiap loop
                    print("||||FORMAT PENYIMPANAN KATALOG||||")
                    print(">>>>Nama, Ukuran, Harga<<<")
                    count = 0
                    for item in DiksiJoran:
                        count += 1
                        print(str(count) + ".", DiksiJoran[item][0], DiksiJoran[item][1], DiksiJoran[item][2])
                    PilihanX = input("Pilih nomor item joran yang ingin diedit: ")
                    #Disclaimer: jika pilihanX > 0 pesan peringatan akan ditampilkan, jika < 0 ia tidak mau, saya tidak tau kenapa
                    #dikarenakan tidak menyebabkan eror, saya akan biarkan, if it works dont fix it
                    if PilihanX.isdigit():
                        PilihanX = int(PilihanX)
                        if PilihanX <= UkuranDiksiJoran and PilihanX != 0: 
                            PilihanY = ""
                            ListX = []
                            print ("Data Joran:", DiksiJoran["Joran_" + str(PilihanX)])
                            PilihanY = input("Nama Baru     : ")
                            ListX.append(PilihanY)
                            PilihanY = input("Ukuran Baru   : ")
                            ListX.append(PilihanY)
                            PilihanY = input("Harga Baru    : ")
                            ListX.append(PilihanY)
                            DiksiJoran["Joran_" + str(PilihanX)] = ListX
                            print("Nama sukses terganti!")
                            print ("apakah anda ingin mengedit lagi?\n" \
                                "ketik 'y' atau huruf selain 'n' jika iya\n" \
                                "ketik 'n' jika tidak")
                            PilihanX = input(": ")
                        else:
                            print("Angka tidak ada di dalam list!")
                    else:
                        print("Jangan Masukkan String!")
                    
            elif Pilihan == "4": #Menghapus Joran dari List
                PilihanX = ""
                while PilihanX != "n":
                    DiksiX = {}
                    UkuranDiksiJoran = len(DiksiJoran) #mengupdate setiap loop
                    PilihanX = input("Pilih nomor item joran yang ingin dihapus dari list: ")
                    if PilihanX.isdigit() != True:
                        print("Tolong mengetik dengan serius!")
                    else:
                        PilihanX = int(PilihanX)
                        KeyX = "Joran_" + str(PilihanX)
                        if PilihanX > UkuranDiksiJoran or PilihanX <= 0:
                            print("Joran dengan nomor tsb. tidak ada!")
                        else:
                            print("Menghapus Joran", DiksiJoran[KeyX])
                            DiksiJoran.pop(KeyX) 
                            print("Joran telah dihapus!")
                            #Menyusun Ulang Urutan Joran
                            count = 1
                            for x in DiksiJoran.values():
                                DiksiX["Joran_" + str(count)] = x
                                count += 1
                            DiksiJoran = DiksiX
                            print ("apakah anda ingin menghapus lagi?\n" \
                                    "ketik 'y' jika iya\n" \
                                    "ketik 'n' jika tidak")
                            PilihanX = input(": ")
                
            elif Pilihan == "5":
                os.system("cls")
            
            elif Pilihan == "6":
                print("Terimakasih sudah menggunakan program ini !")
            else:
                print("Tolong Masukkan Input Yang Benar!")
        #MENU ADMIN
elif StatusUser == "user":
    #USER LOGIN
    count = 0
    while count < 3:
        PilihanX = input("Username: ")
        PilihanY = input("Password: ")
        for keys in DiksiUser:
            if keys != PilihanX and DiksiUser[keys] != PilihanY:
                print("Username atau Password salah!, Silahkan Coba Lagi")
                StatusUser = "noob"
            elif keys == PilihanX and DiksiUser[keys] == PilihanY:
                StatusUser = "user"
                count += 3
                break
        count += 1
    #USER LOGIN
    if StatusUser == "user":
        #MENU USER
        print("░███     ░███    ░███    ░██     ░██    ░███    ░██     ░██    ░███    ░███     ░███        ░█████    ░███    ░██     ░██    ░███    \n" \
                        "░████   ░████   ░██░██   ░██     ░██   ░██░██   ░██    ░██    ░██░██   ░████   ░████          ░██    ░██░██    ░██   ░██    ░██░██   \n" \
                        "░██░██ ░██░██  ░██  ░██  ░██     ░██  ░██  ░██  ░██   ░██    ░██  ░██  ░██░██ ░██░██          ░██   ░██  ░██    ░██ ░██    ░██  ░██  \n" \
                        "██ ░████ ░██ ░█████████ ░██████████ ░█████████ ░███████    ░█████████ ░██ ░████ ░██          ░██  ░█████████    ░████    ░█████████\n" \
                        "░██  ░██  ░██ ░██    ░██ ░██     ░██ ░██    ░██ ░██   ░██   ░██    ░██ ░██  ░██  ░██    ░██   ░██  ░██    ░██     ░██     ░██    ░██ \n" \
                        "░██       ░██ ░██    ░██ ░██     ░██ ░██    ░██ ░██    ░██  ░██    ░██ ░██       ░██    ░██   ░██  ░██    ░██     ░██     ░██    ░██\n" \
                        "░██       ░██ ░██    ░██ ░██     ░██ ░██    ░██ ░██     ░██ ░██    ░██ ░██       ░██     ░██████   ░██    ░██     ░██     ░██    ░██ ")
        print ("<||||[Selamat Datang di Toko Pancing Mahakam Jaya]||||>")
        Pilihan = ""
        while Pilihan != "3":
            UkuranDiksiJoran = len(DiksiJoran) #mengupdate setiap loop
            print ("Apa yang ingin anda lakukan?\n" \
                "1. Lihat Katalog Joran Yang Ada\n" \
                "2. Bersihkan Layar\n" \
                "3. Keluar Dari Aplikasi")
            Pilihan = input("Pilih Aksi: ")
            if Pilihan == "1":
                #Melihat Katalog Joran
                PilihanX = ""
                while PilihanX != "n":
                    UkuranDiksiJoran = len(DiksiJoran) #mengupdate setiap loop
                    print ("Nama-Nama Joran di Inventori")
                    count = 0
                    for key in DiksiJoran:
                        count += 1
                        print(str(count) + ".", DiksiJoran[key][0])
                                    
                    PilihanX = input("Untuk mengetahui lebih lanjut mengenai joran, ketik 'y', " \
                                     "Untuk kembali ke menu, ketik 'n'\n" \
                                     "Pilihan                          : ")    
                    if PilihanX == 'y':
                        PilihanX = UkuranDiksiJoran 
                        while PilihanX <= UkuranDiksiJoran or PilihanX > 0:
                            PilihanX = input("Pilih Nomor Joran: ")
                            if PilihanX.isdigit():
                                PilihanX = int(PilihanX)
                                if PilihanX > UkuranDiksiJoran or PilihanX < 1:
                                    print("Masukkan Nomor Yang Ada!")
                                else:
                                    print("Nama     :" + DiksiJoran["Joran_" + str(PilihanX)][0] + "\n"
                                          "Ukuran   :" + DiksiJoran["Joran_" + str(PilihanX)][1] + "\n"
                                          "Harga    :" + DiksiJoran["Joran_" + str(PilihanX)][2])
                                    PilihanX = input("Ketik huruf apapun untuk lanjut, huruf 'n' untuk ke menu utama: ")
                                    if PilihanX == 'n':
                                        break
                                    else:
                                        PilihanX = UkuranDiksiJoran
                            elif PilihanX == "n":
                                break
                            else:
                                print("JANGAN MASUKKAN STRING, ANGKA ONLY!")
                                PilihanX = UkuranDiksiJoran
                    elif PilihanX != "n":
                        print("Jangan masukkan huruf lain!")
            elif Pilihan == "2":
                os.system("cls")
        #MENU USER
        print("Terimakasih Sudah Menggunakan Layanan Kami!")
    else:
        print("Gagal Login, Silahkan reboot aplikasi dan buat akun baru!")
        #Selesai
elif StatusUser == "none":
    print("Terimakasih Sudah Menggunakan Layanan Kami!")
