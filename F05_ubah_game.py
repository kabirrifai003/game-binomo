import utility as u
import time

def ubah_game(array):

    sukses = False

    idgame = str(input('Masukkan id game: '))
    namaGame = str(input("Masukkan nama game: "))
    kategori = str(input("Masukkan kategori: "))
    tahunRilis = str(input("Masukkan tahun rilis: "))
    harga = str(input("Masukkan harga: "))

    if idgame == '':
        print("Harap masukkan idgame.\n")
    elif (tahunRilis != '' and not u.angkaSemua(tahunRilis) ):
        print("Input tahun rilis tidak sesuai.\n")
    elif (harga != '' and not u.inputHargaBenar(harga)):
        print("input harga tidak sesuai.\n")
    else:
        if u.idSesuai(array, idgame, 'id'):
            if tahunRilis != '':
                tahunRilis = int(tahunRilis)
                if tahunRilis < 1900:
                    print("Game apaan yang rilis tahun segitu?\n")
                elif tahunRilis > int(time.strftime("%Y")):
                    print("Gak terima jualan pre-order bang\n")
                else:
                    tahunRilis = str(tahunRilis)
                    sukses = True
            else:
                 sukses = True
    
    if sukses:
        lokasi = u.cariId(array, idgame, 'id')

        if u.panjangArray(idgame) == 3:
                temp2 = 'GAME' + idgame
        elif u.panjangArray(idgame) == 4:
                temp = ''
                for i in range(1, 4):
                    temp += idgame[i]
                temp2 = 'GAME' + temp
        else:
            temp2 = idgame

        ubah = False
        if namaGame != '':
            array[lokasi][u.kodeKategori(array, 'nama')] = namaGame
            ubah = True
        if kategori != '':
            array[lokasi][u.kodeKategori(array, 'kategori')] = kategori
            ubah = True
        if tahunRilis != '':
            array[lokasi][u.kodeKategori(array, 'tahun_rilis')] = u.angka(tahunRilis)
            ubah = True
        if harga != '':
            array[lokasi][u.kodeKategori(array, 'harga')] = u.tambahTitikHarga(u.angka(harga))
            ubah = True

        if ubah:
            print("\nSelamat! Game dengan id", temp2, 'berhasil diubah\n')
        else:
            print("\nKok gak ngubah apa apa? suka buang - buang waktu ya?\n")

    return array
