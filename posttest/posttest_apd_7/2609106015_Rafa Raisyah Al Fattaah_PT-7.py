#CRUD
#Toko mancing
#POSTTEST_7
#Added: more than 5 Procedur (login, menu_admin, menu_user, admin_login, user_login, Klasifikasi_user, dst...)
#       2 Parameterized Function (NUH_DiksiJoran, New_Joran)
#       2 Free range all natural no preservatve non parameterized function (User_Check, Edit_Diksi)
#       Variabel Global: DiksiUser, DiksiJoran, UkuranDiksiJoran
#       Variabel Lokal: Pilihan, PilihanX, PilihanY, ListX, StatusDuplikat
#       Implemented Error Handling
#       Penerapan fungsi rekursif (Tampilkan_Edit)
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

def Dupe_Check(PilihanX : str):
    global DiksiUser
    StatusDuplikat = 0
    for keys in DiksiUser.keys():
        if keys != PilihanX:
            StatusDuplikat = 0
        else:
            StatusDuplikat = 1
            print ("Akun dengan nama itu sudah ada, silahkan coba lagi!")
            break
    return StatusDuplikat

def Create_Account(DiksiUser : dict):
    print("Anda mau buat akun baru? silahkan silahkan!")
    PilihanX = ""
    while PilihanX != "n":
        PilihanX = input("Masukkan Nama     : ")
        PilihanY = input("Masukkan Password : ")
        if Dupe_Check(PilihanX) == 0:
            DiksiUser.update({PilihanX : PilihanY})

        PilihanX = input("ketik apapun untuk membuat akun lagi!\n" \
                         "ketik n untuk kembali ke menu: ")
    #Sistem Registrasi

def User_Check():
    PilihanA = ""
    StatusUser = ""
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
            Create_Account(DiksiUser)
        elif PilihanA == "4":
            StatusUser = "none"
        else:
            print("Jangan Masukkan hal lain. Be a human")
    return StatusUser

def NUH_DiksiJoran(DiksiJoran : int, PilihanX : int):
    NUH_Diksi = ("Nama     :" + DiksiJoran["Joran_" + str(PilihanX)][0] + "\n"
                 "Ukuran   :" + DiksiJoran["Joran_" + str(PilihanX)][1] + "\n"
                 "Harga    :" + DiksiJoran["Joran_" + str(PilihanX)][2])
    return NUH_Diksi

#Pilihan 1
def New_Joran(PilihanX):
    ListX = []
    PilihanX = input("Masukkan Nama Joran Baru: ")
    ListX.append(PilihanX)
    PilihanX = input("Masukkan Panjang Joran (cm):")
    ListX.append(PilihanX + "cm")
    PilihanX = input("Masukkkan Harga Joran (Rp): ")
    ListX.append("Rp." + PilihanX)  
    return ListX

def Add_Joran(DiksiJoran : dict):
    PilihanX = ""
    while PilihanX != 'n':
        UkuranDiksiJoran = len(DiksiJoran)
        DiksiJoran.update({"Joran_" + str(UkuranDiksiJoran + 1) : New_Joran(PilihanX)})
        print("Joran Berhasil ditambahkan ke dalam katalog!")
        PilihanX = input("apakah anda ingin menambahkan joran lagi?\n" \
                         "ketik 'y' atau huruf lain jika iya\n" #disini kenapa eror pas '\' diletakan, saya tidak tau
                         "ketik 'n' jika tidak: " )
                         #Jika itu bekerja, jangan disentuh
#Pilihan 1

#Pilihan 2

def View_Joran(DiksiJoran : dict):
    PilihanX = ""
    while PilihanX != "n":
        print ("Nama-Nama Joran di Inventori")
        count = 0
        for key in DiksiJoran:
            count += 1
            print(str(count) + ".", DiksiJoran[key][0])
                        
        PilihanX = input("Untuk mengetahui lebih lanjut mengenai joran, ketik 'y', " \
                        "Untuk kembali ke menu, ketik 'n'\n" \
                        "Pilihan                          : ")    
        if PilihanX == 'y':
            while PilihanX != "n":
                PilihanX = input(
                            "Pilih angka Joran                : ")
                try:
                    print (NUH_DiksiJoran(DiksiJoran, PilihanX))
                    PilihanX = input("Ketik huruf apapun untuk lanjut, huruf 'n' untuk ke menu utama: ")
                    if PilihanX == 'n':
                        break
                except KeyError:
                    print ("Jangan masukkan angka negatif, string, atau angka yang tidak ada didalam dictionary!")
        elif PilihanX != "n":
            print ("Jangan masukkan huruf lain selain (y/n)")
#Pilihan 2

#Pilihan 3

def Tampilkan_Edit(iterasi: int, ListX : list):
    ListEdit = ["Nama baru     ", "Ukuran baru   ", "Harga baru    "]
    if iterasi == 0:
        print(ListEdit[0] + ": " + ListX[0])
        return 1
    else:
        Tampilkan_Edit(iterasi-1, ListX)
        print(ListEdit[iterasi] + ": " + ListX[iterasi])


def Edit_Diksi():
    PilihanY = ""
    ListX = []
    PilihanY = input("Nama          : ")
    ListX.append(PilihanY)
    PilihanY = input("Ukuran        : ")
    ListX.append(PilihanY + "cm")
    PilihanY = input("Harga         : ")
    ListX.append("Rp." + PilihanY)
    print ("Mengedit Joran.............")
    Tampilkan_Edit(2, ListX)
    return ListX

def Edit_Joran(DiksiJoran : dict):
    PilihanX = ""
    while PilihanX != "n":
        print("||||FORMAT PENYIMPANAN KATALOG||||")
        print(">>>>Nama, Ukuran, Harga<<<")
        count = 0
        for item in DiksiJoran:
            count += 1
            print(str(count) + ".", DiksiJoran[item][0], DiksiJoran[item][1], DiksiJoran[item][2])
        PilihanX = input("Pilih nomor item joran yang ingin diedit: ")
        try:
            print ("Data Joran:", DiksiJoran["Joran_" + str(PilihanX)])
            DiksiJoran["Joran_" + str(PilihanX)] = Edit_Diksi()
            print("Nama sukses terganti!")
            print ("apakah anda ingin mengedit lagi?\n" \
                    "ketik 'y' atau huruf selain 'n' jika iya\n" \
                    "ketik 'n' jika tidak")
            PilihanX = input(": ")
        except KeyError:
            print("Jangan masukkan angka negatif, string, atau angka yang tidak ada didalam dictionary!")
#Pilihan 3

#Pilihan 4
def Remove_Joran():
    global DiksiJoran
    PilihanX = ""
    while PilihanX != "n":
        DiksiX = {}
        try:
            PilihanX = input("Pilih nomor item joran yang ingin dihapus dari list: ")
            KeyX = "Joran_" + str(PilihanX)
            print("Menghapus Joran", DiksiJoran[KeyX])
        except KeyError:
            print("Jangan masukkan angka negatif, string, atau angka yang tidak ada didalam dictionary!")
        else:
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
                    
#Pilihan 4

def menu_admin():
    global DiksiJoran
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
            Add_Joran(DiksiJoran)
                    
        elif Pilihan == "2":
            View_Joran(DiksiJoran)
                
        elif Pilihan == "3": #Edit Joran
            Edit_Joran(DiksiJoran)
                        
        elif Pilihan == "4": #Menghapus Joran dari List
            Remove_Joran()

        elif Pilihan == "5":
            os.system("cls")
                
        elif Pilihan == "6":
            print("Terimakasih sudah menggunakan program ini !")
        else:
            print("Tolong Masukkan Input Yang Benar!")
    #MENU ADMIN

def menu_user():
    global DiksiJoran
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
        print ("Apa yang ingin anda lakukan?\n" \
               "1. Lihat Katalog Joran Yang Ada\n" \
               "2. Bersihkan Layar\n" \
               "3. Keluar Dari Aplikasi")
        Pilihan = input("Pilih Aksi: ")
        if Pilihan == "1":
            View_Joran(DiksiJoran)
        elif Pilihan == "2":
            os.system("cls")
    #MENU USER
    print("Terimakasih Sudah Menggunakan Layanan Kami!")

def admin_login():
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
        print("Silahkan renungkan kembali pilihan hidupmu, dan coba lah mengingat apa passwordmu")
        return
    else:
        menu_admin()
    #ADMIN LOGIN

def user_login():
    global StatusUser
    count = 0
    while count < 3:
        PilihanX = input("Username: ")
        PilihanY = input("Password: ")
        bogos_binted = 0 #photos_printed?
        for keys in DiksiUser:
            if keys != PilihanX and DiksiUser[keys] != PilihanY:
                StatusUser = "noob"
                if bogos_binted != 1:
                    print("Gagal login, silahkan coba lagi!")
                    bogos_binted = 1 
                continue
            elif keys == PilihanX and DiksiUser[keys] == PilihanY:
                StatusUser = "user"
                count += 3
                break
        count += 1
    #USER LOGIN

def klasifikasi_user():
    if StatusUser == "admin":
        admin_login()
    elif StatusUser == "user":
        user_login()
        #Jika login sukses, StatusUser tidak akan berubah
        if StatusUser == "user":
            menu_user()
        else:
            print("Gagal Login, Silahkan reboot aplikasi dan buat akun baru!")
            #Selesai
    elif StatusUser == "none":
        print("Terimakasih Sudah Menggunakan Layanan Kami!")
    
#Program Utama
def login():
    global StatusUser
    while StatusUser != "none":
        StatusUser = User_Check()
        klasifikasi_user()

login()