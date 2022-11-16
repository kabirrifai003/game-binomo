import utility as u
import time

def buy_game(arraygame, arrayriwayat, arraykepemilikan, arrayuser, userid):
    while True:
        informasiUser = u.cariKategori(arrayuser, 'id', userid)
        print("Saldo kamu saat ini:", informasiUser[1][u.kodeKategori(informasiUser, 'saldo')])
        idgame = str(input("Masukkan idgame (ketik cancel untuk menggagalkan): "))
        
        if idgame == 'cancel' or idgame == 'Cancel' or idgame == 'CANCEL':
            print("\nTransaksi digagalkan.\n")
            break
    
        if u.idSesuai(arraygame, idgame, 'id'):
            gamePunya = u.cariKategori(arraykepemilikan, 'user_id', userid)

            if u.panjangArray(idgame) == 3:
                temp2 = 'GAME' + idgame
            elif u.panjangArray(idgame) == 4:
                    temp = ''
                    for i in range(1, 4):
                        temp += idgame[i]
                    temp2 = 'GAME' + temp
            else:
                temp2 = idgame

            punya = False
            for i in range(u.panjangArray(gamePunya)):
                if temp2 == u.kolom(gamePunya, 'game_id')[i]:
                    print("Game sudah dimiliki.\n")
                    punya = True

            if not punya:
                saldo = int(u.angka(informasiUser[1][u.kodeKategori(informasiUser, 'saldo')]))
                lokasigame = u.cariId(arraygame, idgame, 'id')
                harga = int(u.angka(arraygame[lokasigame][u.kodeKategori(arraygame, 'harga')]))
                stok = int(arraygame[u.urutanDiArray(u.kolom(arraygame, 'id'), temp2)][u.kodeKategori(arraygame, 'stok')])

                if saldo - harga < 0:
                    print("Saldo tidak mencukupi.\n")
                elif stok == 0:
                    print("Stok game habis.\n")
                else:
                    arraykepemilikan = u.tambahBarisKosong(arraykepemilikan)
                    arrayriwayat = u.tambahBarisKosong(arrayriwayat)
                    
                    arraykepemilikan[u.panjangArray(arraykepemilikan)-1][u.kodeKategori(arraykepemilikan, 'user_id')] = userid
                    arraykepemilikan[u.panjangArray(arraykepemilikan)-1][u.kodeKategori(arraykepemilikan, 'game_id')] = temp2

                    arrayriwayat[u.panjangArray(arrayriwayat)-1][u.kodeKategori(arrayriwayat, 'user_id')] = userid
                    arrayriwayat[u.panjangArray(arrayriwayat)-1][u.kodeKategori(arrayriwayat, 'game_id')] = temp2
                    arrayriwayat[u.panjangArray(arrayriwayat)-1][u.kodeKategori(arrayriwayat, 'nama')] = arraygame[lokasigame][u.kodeKategori(arraygame, 'nama')]
                    arrayriwayat[u.panjangArray(arrayriwayat)-1][u.kodeKategori(arrayriwayat, 'harga')] = arraygame[lokasigame][u.kodeKategori(arraygame, 'harga')]
                    arrayriwayat[u.panjangArray(arrayriwayat)-1][u.kodeKategori(arrayriwayat, 'tahun_beli')] = time.strftime("%Y")

                    arrayuser[u.urutanDiArray(u.kolom(arrayuser, 'id'), userid)][u.kodeKategori(arrayuser, 'saldo')] = u.tambahTitikHarga(str(saldo - harga))
                    arraygame[u.urutanDiArray(u.kolom(arraygame, 'id'), temp2)][u.kodeKategori(arraygame, 'stok')] = str(stok-1)

                    print("\nSelamat,", arraygame[lokasigame][u.kodeKategori(arraygame, 'nama')], "berhasil dibeli. Saldo kamu sekarang: ", u.tambahTitikHarga(str(saldo - harga)), "\n")

                    break

    return(arrayriwayat, arraykepemilikan)
