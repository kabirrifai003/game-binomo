import utility as u

def topup(array):
    while True:
        username = str(input("Masukkan username: "))
        saldo = str(input("Masukkan saldo: "))

        temp = ''

        if saldo == '' or username == '':
            print("\nMasukkan saldo atau username tidak valid.\n")
        else:
            if saldo[0] == '-':
                for i in range(1, u.panjangArray(saldo)):
                    temp += saldo[i]
            else:
                temp = saldo

            if not u.adaDiArray(u.kolom(array, 'username'), username):
                print("\nUsername salah atau tidak ditemukan.\n")
            elif not u.inputHargaBenar(temp):
                print("\nMasukkan saldo tidak valid.\n")
            else:
                lokasi = u.urutanDiArray(u.kolom(array, 'username'), username)
                saldoSekarang = array[lokasi][u.kodeKategori(array, 'saldo')]
                if saldo[0] == '-':
                    if int(u.angka(saldoSekarang)) - int(u.angka(temp)) < 0:
                        print("\nPengurangan saldo dibatalkan, saldo tidak mencukupi (saldo sekarang", saldoSekarang, ')\n')
                    else:
                        saldoSekarang = int(u.angka(saldoSekarang)) - int(u.angka(temp))
                        print("\nSaldo berhasil dikurangi, saldo sekarang", saldoSekarang)
                        break
                else:
                    saldoSekarang = int(u.angka(saldoSekarang)) + int(u.angka(temp))
                    print("\nSaldo berhasil ditambah, saldo sekarang", saldoSekarang)
                    break

    array[lokasi][u.kodeKategori(array, 'saldo')] = u.tambahTitikHarga(str(saldoSekarang))
    
    return array
