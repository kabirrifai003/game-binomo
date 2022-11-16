import utility as u

def list_game(arraygame, arraykepemilikan, userid):
    arraymilik = u.cariKategori(arraykepemilikan, 'user_id', userid)
    if u.panjangArray(arraymilik) == 1:
        print("\nMaaf, kamu belum memiliki game. Ketik perintah beli_game untuk beli.\n")
        
    panjangArrayBaru = u.panjangArray(arraymilik)
    jumlahKategoriArrayBaru = u.panjangArray(arraygame[0])-1
        
    arrayBaru = [['0' for i in range(jumlahKategoriArrayBaru)] for i in range(panjangArrayBaru)]

    for line in range(panjangArrayBaru):
        if line > 0:
            idgame = arraymilik[line][u.kodeKategori(arraymilik, 'game_id')]
            lokasi = u.urutanDiArray(u.kolom(arraygame, 'id'), idgame)
        else:
            lokasi = line
        i = 0
        j = 0
        while i < u.panjangArray(arraygame[0]):
            if i == u.kodeKategori(arraygame, 'stok'):
                i += 1
            else:
                arrayBaru[line][j] = arraygame[lokasi][i]
                i += 1
                j += 1

    return arrayBaru
