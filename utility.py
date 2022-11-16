#Berisi subfungsi buatan

def panjangArray(array):
#pengganti len()
    panjang = 0
    for i in array:
        panjang += 1
    return panjang

def adaDiArray(array, anggota):
#pengganti boolean (anggota) in (array)
    panjang = panjangArray(array)
    ada = False
    for i in range(panjang):
        if array[i] == anggota:
            ada = True
    return ada

def urutanDiArray(array, anggota):
#mencari urutan anggota di array, anggota harus diverifikasi ada
    for i in range(panjangArray(array)):
        if anggota == array[i]:
            lokasi = i
            break
    return lokasi

def kodeKategori(array, namaKategori):
#mengembalikan index kategori berdasarkan namanya
    for i in range(panjangArray(array[0])):
        if namaKategori == array[0][i]:
            markerKategori = i
    return markerKategori

def kolom(array, namaKategori):
#mengembalikan satu kolom berdasarkan kategori array
    arrayKolom = [0 for i in array]

    for i in range(panjangArray(array)):
        arrayKolom[i] = array[i][kodeKategori(array, namaKategori)]
    
    return arrayKolom

def salin(array):
#membuat salinan suatu array
    kategori = panjangArray(array[0])
    baris = panjangArray(array)
    arrayBaru = [['0' for i in range(kategori)] for i in range(baris)]

    for i in range(baris):
        for j in range(kategori):
            arrayBaru[i][j] = array[i][j]
    
    return arrayBaru

def kalimat2Lebih(kalimat1, kalimat2):
#True kalau kalimat2 harus keluar lebih awal dari kalimat1
#Fungsinya untuk sorting huruf
    ya = False
    if kalimat1 == kalimat2:
        ya = False
    else:
        if panjangArray(kalimat1) > panjangArray(kalimat2):
            limit = panjangArray(kalimat2)
        else:
            limit = panjangArray(kalimat1)
        
        for i in range(limit):
            mentok = False
            if i == limit - 1:
                mentok = True

            if kalimat1[i] == kalimat2[i]:
                pass

            elif (ord(kalimat1[i]) >= 65 and ord(kalimat1[i]) <= 90) or (ord(kalimat1[i]) - 32 >= 65 and ord(kalimat1[i]) - 32 <= 90):
                if (ord(kalimat1[i]) - 32 >= 65 and ord(kalimat1[i]) - 32 <= 90):
                    urutan1 = ord(kalimat1[i]) - 32
                else:
                    urutan1 = ord(kalimat1[i])

                if (ord(kalimat2[i]) >= 65 and ord(kalimat2[i]) <= 90) or (ord(kalimat2[i]) - 32 >= 65 and ord(kalimat2[i]) - 32 <= 90):
                    if (ord(kalimat2[i]) - 32 >= 65 and ord(kalimat2[i]) - 32 <= 90):
                        urutan2 = ord(kalimat2[i]) - 32
                    else:
                        urutan2 = ord(kalimat2[i])

                    if urutan2 < urutan1:
                        ya = True
                        break
                    elif urutan2 > urutan1:
                        ya = False
                        break
                    
                else:
                    ya = True
                    break
            
            elif (ord(kalimat1[i]) >= 48 and ord(kalimat1[i]) <= 57):
                if (ord(kalimat2[i]) >= 65 and ord(kalimat2[i]) <= 90) or (ord(kalimat2[i]) - 32 >= 65 and ord(kalimat2[i]) - 32 <= 90):
                    ya = False
                    break
                elif (ord(kalimat2[i]) >= 48 and ord(kalimat2[i]) <= 57):

                    if ord(kalimat1[i]) > ord(kalimat2[i]):
                        ya = True
                        break
                    elif ord(kalimat1[i]) < ord(kalimat2[i]):
                        ya = False
                        break

                else:
                    ya = True
                    break
                
            else:
                ya = False
                break

        if mentok == True and panjangArray(kalimat2) < panjangArray(kalimat1):
            ya = True

    return ya

def sortKategoriAngka(array, namaKategori, cara):
#sorting array, pastikan kategori isinya angka semua
#sorting dilakukan dengan cara bubblesort
    array = salin(array)
    kategori = kodeKategori(array, namaKategori)

    if cara == '+':
        swap = True
        while swap == True:
            swap = False
            for i in range(1, panjangArray(array)-1):
                if float(angka(array[i][kategori])) > float(angka(array[i+1][kategori])):
                    cacheSwap = array[i]

                    array[i] = array[i+1]
                    array[i+1] = cacheSwap

                    swap = True

    else: #cara == '-':
        swap = True
        while swap == True:
            swap = False
            for i in range(1, panjangArray(array)-1):
                if float(angka(array[i][kategori])) < float(angka(array[i+1][kategori])):
                    cacheSwap = array[i]

                    array[i] = array[i+1]
                    array[i+1] = cacheSwap

                    swap = True

    return array

def sortKategoriHuruf(array, namaKategori, cara):
#sorting array, pastikan kategori isinya huruf semua
#sorting dilakukan dengan cara bubblesort
    array = salin(array)
    kategori = kodeKategori(array, namaKategori)

    if cara == '+':
        swap = True
        while swap == True:
            swap = False
            for i in range(1, panjangArray(array)-1):
                if kalimat2Lebih(array[i][kategori], array[i+1][kategori]):
                    cacheSwap = array[i]

                    array[i] = array[i+1]
                    array[i+1] = cacheSwap

                    swap = True

    else: #cara == '-':
        swap = True
        while swap == True:
            swap = False
            for i in range(1, panjangArray(array)-1):
                if not kalimat2Lebih(array[i][kategori], array[i+1][kategori]):
                    if array[i][kategori] == array[i+1][kategori]:
                        pass
                    else:
                        cacheSwap = array[i]

                        array[i] = array[i+1]
                        array[i+1] = cacheSwap

                        swap = True

    return array

def cariKategori(array, namaKategori, namaJenis):
#mengembalikan array berdasarkan satu jenis kolom yang berisi kategori(misal dalam game kategori : rpg)
    kategori = kodeKategori(array, namaKategori)

    if angkaSemua(namaJenis) and (namaKategori == 'harga' or namaKategori == 'saldo'):
        namaJenis = tambahTitikHarga(namaJenis)

    panjangArrayBaru = 1
    for i in range(panjangArray(array)):
        if array[i][kategori] == namaJenis:
            panjangArrayBaru += 1
    
    arrayBaru = ['' for i in range(panjangArrayBaru)]
    arrayBaru[0] = array[0]

    indeksArrayBaru = 1
    for i in range(panjangArray(array)):
        if array[i][kategori] == namaJenis:
            arrayBaru[indeksArrayBaru] = array[i]
            indeksArrayBaru += 1
    
    return arrayBaru


#subfungsi perihal penambahan game
def angkaSemua(kalimat):
#mengecek apakah input berupa angka semua
    ya = True
    for i in range(panjangArray(kalimat)):
        if not ( (ord(kalimat[i]) >= 48 and ord(kalimat[i]) <= 57) ) :
            ya = False
            break
    return ya

def inputHargaBenar(kalimat):
#mengecek apakah input sesuai dengan penulisan atau berisi angka semua
    ya = True
    if angkaSemua(kalimat):
        pass
    else:
        for i in range( (panjangArray(kalimat)-1) , -1, -1):
            if (panjangArray(kalimat) - i)%4 == 0:
                if ord(kalimat[i]) == 46:
                    pass
                elif not ord(kalimat[i]) == 46:
                    ya = False
                    break
            elif not ( (ord(kalimat[i]) >= 48 and ord(kalimat[i]) <= 57) ) :
                ya = False
                break
    return ya

def angka(kalimat):
#mengubah input menjadi angka semua secara proper (tidak ada 0 di depan)
    temp = ''
    for i in range(panjangArray(kalimat)):
        if not ( (ord(kalimat[i]) >= 48 and ord(kalimat[i]) <= 57) ):
            pass
        else:
            temp += kalimat[i]
    
    temp = int(temp)
    temp = str(temp)

    return temp

def tambahTitikHarga(angka):
#menambahkan titik setiap 3 angka
#input berupa angka semua
    temp = ''
    for i in range(panjangArray(angka)):
        temp += angka[i]
        if ( 2 + panjangArray(angka)-i ) % 3 == 0 and i != panjangArray(angka)-1:
            temp += '.'
    return temp

def tambahBarisKosong(array):
#menambah satu baris kosong di ujung array
    kategori = panjangArray(array[0])
    jumlahDataBaru = panjangArray(array) + 1
    arrayBaru = [['0' for i in range(kategori)] for i in range(jumlahDataBaru)]

    for i in range(panjangArray(array)):
        arrayBaru[i] = array[i]
    
    return arrayBaru


#subfungsi perihal pengubahan data array
def idSesuai(array, idgame, namaKategoriId):
#menentukan apabila id game yang ditulis sesuai dan terdapat pada array
    sesuai = False
    if idgame == '':
        print("Harap masukkan idgame.\n")
    else:
        if panjangArray(idgame) == 3:
                if not angkaSemua(idgame):
                    print("Masukkan idgame dengan format G000, GAME000, atau 000 dengan 000 berupa kode angka game yang diinginkan.\n")
                else:
                    temp2 = 'GAME' + idgame
                    
                    ada = False
                    for i in range(1, panjangArray(array)):
                        if temp2 == array[i][kodeKategori(array, namaKategoriId)]:
                            ada = True

                    if not ada:
                        print("Id tidak terdapat pada daftar game.\n")
                    else:
                        sesuai = True

        elif panjangArray(idgame) == 4:
            temp = ''
            for i in range(1, 4):
                temp += idgame[i]
            if not angkaSemua(temp) or idgame[0] != 'G':
                print("Masukkan idgame dengan format G000, GAME000, atau 000 dengan 000 berupa kode angka game yang diinginkan.\n")
            else:
                temp2 = 'GAME' + temp
                
                ada = False
                for i in range(1, panjangArray(array)):
                    if temp2 == array[i][kodeKategori(array, namaKategoriId)]:
                        ada = True

                if not ada:
                    print("Id tidak terdapat pada daftar game.\n")
                else:
                    sesuai = True
            
        elif panjangArray(idgame) == 7:
            temp = ''
            temp3 = ''
            for i in range(4, 7):
                temp += idgame[i]
            for i in range(0, 4):
                temp3 += idgame[i]
                
            if not angkaSemua(temp) or temp3 != 'GAME':
                print("Masukkan idgame dengan format G000, GAME000, atau 000 dengan 000 berupa kode angka game yang diinginkan.\n")
            else:
                temp2 = 'GAME' + temp
                    
                ada = False
                for i in range(1, panjangArray(array)):
                    if temp2 == array[i][kodeKategori(array, namaKategoriId)]:
                        ada = True

                if not ada:
                    print("Id tidak terdapat pada daftar game.\n")
                else:
                    sesuai = True
            
        else:
            print("Masukkan idgame dengan format G000, GAME000, atau 000 dengan 000 berupa kode game yang diinginkan.\n")

    return sesuai

def cariId(array, idgame, namaKategoriId):
#mencari letak id di array
#id harus ada di array dan sudah disesuaikan oleh fungsi idSesuai
    kolomId = kolom(array, namaKategoriId)

    if panjangArray(idgame) == 3:
        temp2 = 'GAME' + idgame
    elif panjangArray(idgame) == 4:
            temp = ''
            for i in range(1, 4):
                temp += idgame[i]
            temp2 = 'GAME' + temp
    else:
        temp2 = idgame

    lokasi = urutanDiArray(kolomId, temp2)

    return lokasi

def usernameValid(kalimat):

    valid = True

    for i in kalimat:
        if ord(i) >= 48 and ord(i) <= 57:
            pass
        elif ord(i) >= 65 and ord(i) <= 90:
            pass
        elif ord(i) >=97 and ord(i) <= 122:
            pass
        elif ord(i) == 95 or ord(i) == 126:
            pass
        else:
            valid = False
    
    return valid


#Fungsi printing
def printRapi(array):
#output array dengan jarak rapi
    arrayCache = salin(array)

    print()
    for line in range(panjangArray(arrayCache)):
        for anggota in range(panjangArray(arrayCache[0])):
            arrayCache[line][anggota] = arrayCache[line][anggota] + '    '
    
    for anggota in range(panjangArray(array[0])):
        
        panjangMaks = 0
        for line in range(panjangArray(arrayCache)):
            if panjangArray(arrayCache[line][anggota]) > panjangMaks:
                panjangMaks = panjangArray(arrayCache[line][anggota])
        
        for line in range(panjangArray(arrayCache)):
            while panjangArray(arrayCache[line][anggota]) < panjangMaks:
                arrayCache[line][anggota] = arrayCache[line][anggota] + ' '

    nomor = 1
    for i in range(panjangArray(arrayCache)):
        if i == 0:
            print("No     ", end = '')
        else:
            nomorPrint = str(nomor)
            while panjangArray(nomorPrint) < (panjangArray("No     ")):
                nomorPrint += ' '
            print(nomorPrint, end = '')
            nomor += 1
        for j in range(panjangArray(arrayCache[0])):
            print(arrayCache[i][j], end = '')
        print()
    print()