import utility as u

def riwayat(array, userid):
    array = u.cariKategori(array, 'user_id', userid)

    panjangArrayBaru = u.panjangArray(array)
    jumlahKategoriArrayBaru = u.panjangArray(array[0])-1

    arrayBaru = [['0' for i in range(jumlahKategoriArrayBaru)] for i in range(panjangArrayBaru)]

    for line in range(panjangArrayBaru):
        i = 0
        j = 0
        while i < u.panjangArray(array[0]):
            if i == u.kodeKategori(array, 'user_id'):
                i += 1
            else:
                arrayBaru[line][j] = array[line][i]
                i += 1
                j += 1
    
    if u.panjangArray(arrayBaru) > 1:
        u.printRapi(arrayBaru)
    else:
        print("\nMaaf, kamu belum memiliki game. Ketik perintah beli_game untuk beli.\n")
