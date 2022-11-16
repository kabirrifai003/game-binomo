import utility as u
import F09_list_game as f09

def search_my_game(arraygame, arraykepemilikan, userid):
    array = f09.list_game(arraygame, arraykepemilikan, userid)

    if not u.panjangArray(array) == 1:
        idgame = str(input("Masukkan ID game: "))
        nama = str(input("Masukkan nama game: "))
        harga = str(input("Masukkan harga game: "))
        kategori = str(input("Masukkan kategori game: "))
        tahun = str(input("Masukkan tahun game: "))

        if idgame != '':
            if u.idSesuai(array, idgame, 'id'):

                if u.panjangArray(idgame) == 3:
                    temp2 = 'GAME' + idgame
                elif u.panjangArray(idgame) == 4:
                        temp = ''
                        for i in range(1, 4):
                            temp += idgame[i]
                        temp2 = 'GAME' + temp
                else:
                    temp2 = idgame
                array = u.cariKategori(array, 'id', temp2)

            else:
                array = u.cariKategori(array, 'id', idgame)

        if nama != '':
            array = u.cariKategori(array, 'nama', nama)
        if harga != '':
            array = u.cariKategori(array, 'harga', harga)
        if kategori != '':
            array = u.cariKategori(array, 'kategori', kategori)
        if tahun != '':
            array = u.cariKategori(array, 'tahun_rilis', tahun)
        
        if u.panjangArray(array) == 1:
            print("\nTidak ada game di inventory yang memenuhi kriteria.\n")
        else:
            u.printRapi(array)
