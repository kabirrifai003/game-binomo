import utility as u
#ParserCsv

def jumlahKategori(arrayCSV):
#menghitung jumlah kategori csv
#fungsi antara parsedCsv, gak guna di luar itu
    kategori = 1
    i = 0
    while arrayCSV[i] != '\n':
        if arrayCSV[i] == ',':
            kategori += 1
        i += 1
    return kategori

def jumlahData(arrayCSV):
#menghitung jumlah data csv (termasuk kategorial)
#fungsi antara parsedCsv, gak guna di luar itu
    jumlahData = 0
    for i in range(u.panjangArray(arrayCSV)):
        if arrayCSV[i] == '\n':
            jumlahData += 1
    return jumlahData

def parsedCsv(csv):
#membaca csv sebagai array
#menutup csv secara otomatis
    arrayCsv = csv.read()
    csv.close()

    kategori = jumlahKategori(arrayCsv)
    Data = jumlahData(arrayCsv)
    matriks = [[0 for i in range(kategori)] for i in range(Data)]

    aksesData = 0
    marker = 0
    for i in range(Data):

        temporary = ''
        comma = 0
        while True:
            if arrayCsv[marker] == ',':
                matriks[aksesData][comma] = temporary
                comma += 1
                temporary = ''

            elif arrayCsv[marker] == '\n':
                matriks[aksesData][comma] = temporary
                comma += 1
                temporary = ''

                marker += 1
                break

            else:
                temporary += arrayCsv[marker]

            marker += 1

        aksesData += 1
    return(matriks)

def arrayToCsv(array):
    temp = ''
    for i in range(u.panjangArray(array)):
        for j in range(u.panjangArray(array[i])):
            for k in array[i][j]:
                temp += str(k)
            if not j == u.panjangArray(array[i])-1:
                temp += ','
        temp += '\n'
    return temp
