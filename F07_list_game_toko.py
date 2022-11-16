import utility as u

def list_game_toko(array):
    while True:
        skema = str(input("Skema sorting: "))
        if skema == '':
            u.printRapi(array)
            break
        else:
            temp = ''
            for i in range(u.panjangArray(skema)-1):
                temp += skema[i]
            
            if skema == '':
                u.printRapi(array)
                break
            else:
                cara = skema[u.panjangArray(skema)-1]

                if temp == 'tahun':
                    temp = 'tahun_rilis'

                if not u.adaDiArray(array[0], temp):
                    print("Skema sorting tidak valid.\n")
                elif cara == '+' or cara == '-':
                    if temp == 'id' or temp == 'kategori' or temp == 'nama':
                        u.printRapi(u.sortKategoriHuruf(array, temp, cara))
                        break
                    elif temp == 'tahun_rilis' or 'harga' or 'stok':
                        u.printRapi(u.sortKategoriAngka(array, temp, cara))
                        break
                else:
                    print("Skema sorting tidak valid.\n")
