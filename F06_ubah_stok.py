import utility as u

def ubah_stok(array):

    sukses = False

    sesuai1 = False
    sesuai2 = False
        
    idgame = str(input("Masukkan ID game: "))

    if u.idSesuai(array, idgame, 'id'):
        sesuai1 = True

    if sesuai1:
        ubahanstok = str(input("Masukkan Jumlah: "))

        if ubahanstok == '':
            print("input stok tidak valid.\n")
        else:

            if ubahanstok[0] == '-':
                temp = ''
                for i in range(1, u.panjangArray(ubahanstok)):
                    temp += ubahanstok[i]
            else:
                temp = ubahanstok

            if not u.angkaSemua(temp):
                print("input stok tidak valid.\n")
            else:
                sesuai2 = True
        
    if sesuai2:
        lokasi = u.cariId(array, idgame, 'id')
        stokSekarang = int(array[lokasi][u.kodeKategori(array, 'stok')])
        stokBaru = stokSekarang + int(ubahanstok)
        if stokBaru < 0:
            print("\nStok game", array[lokasi][u.kodeKategori(array, 'nama')], 'gagal dikurangi karena stok kurang. Stok sekarang:', stokSekarang, '(<', temp, ').\n')
        else:
            array[lokasi][u.kodeKategori(array, 'stok')] = str(stokBaru)
            sukses = True
    
    if sukses:
        if int(ubahanstok) == 0:
            print("\nKok gak ngubah apa apa? suka buang - buang waktu ya?\n")
        else:
            if int(ubahanstok) < 0:
                print("\nStok game", array[lokasi][u.kodeKategori(array, 'nama')], 'berhasil dikurangi. Stok sekarang:', stokBaru, '.\n')
            else:
                print("\nStok game", array[lokasi][u.kodeKategori(array, 'nama')], 'berhasil ditambah. Stok sekarang:', stokBaru, '.\n')

    return array
