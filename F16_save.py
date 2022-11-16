import os
import parserCSV

def save(gameArray, userArray, riwayatArray, kepemilikanArray):
    while True:
        namaFile = str(input("Masukkan nama folder penyimpanan: "))

        path = os.getcwd() + '/' + namaFile

        if os.path.exists(path):
            while True:
                konfirmasi = str(input("Nama file sudah ada, apakah anda ingin mengganti file dengan yang baru? (y/n) "))
                if konfirmasi == 'Y' or konfirmasi == 'y' or konfirmasi == 'N' or konfirmasi == 'n':
                    break
                else:
                    print("Input tidak valid.")

            if konfirmasi == 'Y' or konfirmasi == 'y':
                gameCsv = open(namaFile+'/game.csv', 'w')
                userCsv = open(namaFile+'/user.csv', 'w')
                riwayatCsv = open(namaFile+'/riwayat.csv', 'w')
                kepemilikanCsv = open(namaFile+'/kepemilikan.csv', 'w')
                break
        
        else:
            os.mkdir(namaFile)
            gameCsv = open(namaFile+'/game.csv', 'w')
            userCsv = open(namaFile+'/user.csv', 'w')
            riwayatCsv = open(namaFile+'/riwayat.csv', 'w')
            kepemilikanCsv = open(namaFile+'/kepemilikan.csv', 'w')
            break

    print("\nsaving...")
    savefile = parserCSV.arrayToCsv(gameArray)
    gameCsv.write(savefile)
    savefile = parserCSV.arrayToCsv(userArray)
    userCsv.write(savefile)
    savefile = parserCSV.arrayToCsv(riwayatArray)
    riwayatCsv.write(savefile)
    savefile = parserCSV.arrayToCsv(kepemilikanArray)
    kepemilikanCsv.write(savefile)

    gameCsv.close()
    userCsv.close()
    riwayatCsv.close()
    kepemilikanCsv.close()
    
    print("Data telah disimpan pada folder", namaFile, '\n')
