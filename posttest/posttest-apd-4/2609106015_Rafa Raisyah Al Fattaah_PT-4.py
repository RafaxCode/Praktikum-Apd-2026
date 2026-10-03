#Variable awal
#Halaman 1
NamaPanggilan = "Pasyah"
Nim = "015"
Pin = 2 * Nim #"015015"
Saldo = 5000000 #Rp.5.000.000

Percobaan = 0
print ("___________________________________________________________________________")
print ("Sebelum menggunakan layanan Bank Malas, masukkan username dan password anda!")
print ("---------------------------------------------------------------------------")
while Percobaan < 3:
    username = input("Masukkan Username anda   :")
    password = input("Masukkan Password anda   :")
    if username == NamaPanggilan and password == Nim:
        Percobaan = 3
    elif username != NamaPanggilan or password != Nim:
        if username != NamaPanggilan and password != Nim:
            print("Login gagal, Username dan Password anda salah!")
        elif username != NamaPanggilan:
            print("Login gagal, Username anda salah!")
        elif password != Nim:
            print("Login gagal, Password anda salah!")
        #Fun fact, sistem seperti ini akan sangat gampang untuk dibobol dengan metode brute force
        
        print(2-Percobaan, "Percobaan lagi")
    Percobaan += 1
#Halaman 1

#Halaman 2
if username != NamaPanggilan or password != Nim:
    print ("Anda telah diblokir")
    exit()

print("---------------------------------------------------------------")
print("[||Selamat datang di Bank Malas, Apa yang ingin anda lakukan||]")
print("---------------------------------------------------------------")

Input_Pengguna = 0

while Input_Pengguna != "2":
    print                 ("    Bank Malas\n" \
                           "   Opsi Pilihan")
    Input_Pengguna = input("1. Transfer Uang\n"
                           "2. Logout/Keluar\n"
                           "Ketik 1/2                      :")
    if Input_Pengguna == "1":
        #Proses transfer
        print            ( "Saldo saat ini                 :Rp.",Saldo)
        if Saldo < 0:
            print ("Saldo anda habis, silahkan melakukan pengisian ulang di cabang terdekat")
            break
        Penerima =  input( "Masukkan Username Penerima     : ")
        Input_Pengguna2 = " "       #Input_Pengguna2 hanya merepresentasikan yes/no, saya belum dapat nama yang cocok
        while Input_Pengguna2 != "n":
            NominalTF = int(input("Masukkan Nominal Transfer\n" \
                              "(Minimal  Rp.50.000 )\n" \
                              "(Maksimal Rp.1.000.000)\n"
                              "Nominal                   :")) 
            if NominalTF < 50000:
                print ("Nominal terlalu kecil, silahkan coba lagi")
            elif NominalTF > 1000000:
                print ("Nominal terlalu besar, silahkan coba lagi")
            elif NominalTF > Saldo:
                print("Saldo tidak cukup, silahkan masukkan ulang Nominal transfernya")
            elif NominalTF >= 50000 and NominalTF <= 1000000 and NominalTF <= Saldo:
                PercobaanPin = 0
                Input_Pin = 0
                while PercobaanPin < 3:
                    Input_Pin = input("Masukkan pin anda untuk mengkonfirmasi transaksi!\n" \
                                    "Pin anda: ")
                    if Input_Pin != str(Pin):
                        PercobaanPin += 1
                        print ("Pin salah! Silahkan coba lagi\n" \
                        "Sisa ", 3-PercobaanPin, "Percobaan")
                    elif Input_Pin == str(Pin):
                        PercobaanPin = 0
                        "Pin benar, transaksi akan diproses"
                        break

                if PercobaanPin == 3 and Input_Pin != Pin:
                    print("Anda telah diblokir, silahkan hubungi cabang terdekat!")
                    exit()
                
                Saldo -= NominalTF
                #Menampilkan struk
                print ("----------------STRUK PEMBAYARAN----------------\n" \
                       "Nama Pengiim     :", username, "\n" \
                       "Nama Penerima    :", Penerima, "\n" \
                       "Nominal Transaksi:", NominalTF, "\n" \
                       "Sisa saldo       :", Saldo, "\n" \
                       "-------------------------------------------------") #Saldo hanya sebagai pelengkap struk
                #Separate function
                print("Apakah anda ingin melakukan transaksi ke penerima yang sama lagi?")
                while Input_Pengguna2 != "n":
                    Input_Pengguna2 = input("(y/n): ")
                    if Input_Pengguna2 == "y":
                        break
                    elif Input_Pengguna2 != "y" and Input_Pengguna2 != "n":
                        print("tolong jangan masukkan kata selain y atau n!") 
    elif Input_Pengguna != "1" and Input_Pengguna != "2":
        print("Tolong jangan masukkan angka/huruf yang lain selain 1 atau 2!")
    #Klarifikasi: untuk 2 elif diatas ini jangan dihapus soalnya penting (Belajar dari kesalahan)
print("Terimakasih sudah menggunakan layanan ini!")
