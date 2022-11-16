import utility as u

def help(role):
    helpArray = ['=============== HELP ===============',
    'register - Untuk melakukan registrasi user baru',
    'logout - Untuk melakukan login ke dalam akun lain',
    'tambah_game - Untuk menambahkan game yang dijual pada toko',
    'ubah_game - Untuk mengubah informasi game yang dijual pada toko',
    'ubah_stok - Untuk mengubah stok game yang dijual pada toko',
    'list_game_toko - Untuk melihat daftar game yang dijual pada toko',
    'buy_game - Untuk membeli game yang dijual pada toko',
    'list_game - Untuk melihat game yang dimiliki',
    'search_my_game - Untuk mencari game yang dimiliki berdasarkan kriteria',
    'search_game_at_store - Untuk mencari game yang dijual pada toko berdasarkan kriteria',
    'topup - Untuk menambahkan saldo pada user',
    'riwayat - Untuk melihat daftar riwayat pembelian game',
    'help - Untuk melihat daftar command yang tersedia',
    'save - Untuk menyimpan data agar perubahan menjadi permanen',
    'exit - Untuk keluar dari aplikasi BNMO',
    'kerangajaib - Untuk memanggil kulit kerang ajaib',
    'tictactoe - Untuk bermain tic-tac-toe']

    print(helpArray[0])
    nomor = 1
    for i in range(1, u.panjangArray(helpArray)):
        if role == 'Admin':
            if i == 1 or i == 2 or i == 3 or i == 4 or i == 5 or i == 6 or i == 10 or i == 11 or i == 13 or i == 14 or i == 15 or i == 16 or i == 17:
                print(str(nomor) + '. ' + helpArray[i])
                nomor += 1
        elif role == 'User':
            if  i == 2 or i == 6 or i == 7 or i == 8 or i == 9 or i == 10 or i == 12 or i == 13 or i == 14 or i == 15 or i == 16 or i == 17:
                print(str(nomor) + '. ' + helpArray[i])
                nomor += 1
    print()
