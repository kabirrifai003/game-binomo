import utility as u
import B02_cipher as ciph

def register(array, key):
    array = u.salin(array)
    sukses = False
    
    nama = str(input("Masukan nama: "))
    username = str(input("Masukan username: "))
    password = str(input("Masukkan password: "))
    if nama == '' or username == '' or password == '':
        print("Nama atau username atau password kosong.\n")
    elif username == 'exit' and password == 'exit':
        print("Username dan password tidak dapat digunakan.\n")
    else:
        if u.usernameValid(username):
            if u.adaDiArray(u.kolom(array, 'username'), username):
                print("Username", username, "sudah dipakai, gunakan username yang lain.\n")
            else:
                sukses = True
        else:
            print("Username menggunakan karakter yang tidak valid (Username hanya dapat mengandung alfabet A-Z/a-z, underscore “_”, strip “-”, dan angka 0-9. )\n")

    if sukses:
        userId = int(u.sortKategoriAngka(array, 'id', '-')[1][u.kodeKategori(array, 'id')]) +1
        userId = str(userId)

        array = u.tambahBarisKosong(array)
        lokasi = u.panjangArray(array)-1
        array[lokasi][u.kodeKategori(array, 'id')] = userId
        array[lokasi][u.kodeKategori(array, 'nama')] = nama
        array[lokasi][u.kodeKategori(array, 'username')] = username
        array[lokasi][u.kodeKategori(array, 'password')] = ciph.encrypt(password, key)
        array[lokasi][u.kodeKategori(array, 'role')] = 'User'
        array[lokasi][u.kodeKategori(array, 'saldo')] = '0'

        print("\nAkun berhasil ditambah.\n")
    
    return array