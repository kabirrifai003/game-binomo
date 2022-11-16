import utility as u
import B02_cipher as ciph

def login(array, key):
    while True:
        inputUsername = str(input("Masukan username : "))
        inputPassword = str(input("Masukan password : "))
        if inputUsername == 'exit' and inputPassword == 'exit':
            userid = '0'
            state = '0'
            break
        elif not u.adaDiArray(u.kolom(array, 'username'), inputUsername) or not u.adaDiArray(u.kolom(array, 'password'), ciph.encrypt(inputPassword, key)):
            print("Password atau username salah atau tidak ditemukan. (ketik exit pada username dan password untuk keluar).\n")
        else:
            lokasi = u.urutanDiArray(u.kolom(array, 'username'), inputUsername)
    
            state = array[lokasi][u.kodeKategori(array, 'role')]
            userid = array[lokasi][u.kodeKategori(array, 'id')]
            nama = array[lokasi][u.kodeKategori(array, 'nama')]

            print("\nHalo " + nama + "!" + " Selamat datang di Binomo!\n")
            break

    return(userid, state)
