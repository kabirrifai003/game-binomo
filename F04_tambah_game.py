import utility as u
import time

def tambah_game(array):
    array = u.salin(array)
    sukses = False

    namaGame = str(input("Masukkan nama game: "))
    kategori = str(input("Masukkan kategori: "))
    tahunRilis = str(input("Masukkan tahun rilis: "))
    harga = str(input("Masukkan harga: "))
    stok = str(input("Masukkan stok awal: "))
    if namaGame == '' or kategori == '' or tahunRilis == '' or harga == '' or stok == '':
        print("Mohon masukkan semua informasi mengenai game agar dapat disimpan BNMO\n")
    else:
        if not u.angkaSemua(tahunRilis) or not u.angkaSemua(stok) or not u.inputHargaBenar(harga):
            print("Terdapat input tidak valid, mohon cek tahun rilis, harga, dan stok.\n")
        else:
            tahunRilis = u.angka(tahunRilis)
            stok = u.angka(stok)
            harga = u.angka(harga)
                
            if int(tahunRilis) < 1900:
                 print("Game apaan yang rilis tahun segitu?\n")
            elif int(tahunRilis) > int(time.strftime("%Y")):
                print("Gak terima jualan pre-order bang\n")
            else:
                sukses = True

    if sukses:
        if u.panjangArray(array) == 1:
            generatedId = 'GAME001'

        else:
            tempArray = u.sortKategoriHuruf(array, 'id', '-')
            generatedId = tempArray[1][u.kodeKategori(array, 'id')]
            temp = ''
            for i in range(4, u.panjangArray(generatedId)):
                temp += generatedId[i]
            temp = int(temp) + 1
            temp = str(temp)
            if u.panjangArray(temp) <= 3:
                temp2 = 'GAME'
                for i in range(3-u.panjangArray(temp)):
                    temp2 += '0'
                for i in range(u.panjangArray(temp)):
                    temp2 += temp[i]
            generatedId = temp2

        array = u.tambahBarisKosong(array)
        array[u.panjangArray(array)-1][u.kodeKategori(array, 'id')] = generatedId
        array[u.panjangArray(array)-1][u.kodeKategori(array, 'nama')] = namaGame
        array[u.panjangArray(array)-1][u.kodeKategori(array, 'kategori')] = kategori
        array[u.panjangArray(array)-1][u.kodeKategori(array, 'tahun_rilis')] = tahunRilis
        array[u.panjangArray(array)-1][u.kodeKategori(array, 'harga')] = u.tambahTitikHarga(harga)
        array[u.panjangArray(array)-1][u.kodeKategori(array, 'stok')] = stok
        
        print("\nSelamat! Berhasil menambahkan game", namaGame, '\n')

    return array
