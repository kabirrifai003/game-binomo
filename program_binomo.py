# TUBES DASPRO

# Assyifa Nurfadilah - 16521029
# Muhamad Aji Wibisono - 16521119
# Pinaka Kusumaningtyas - 16521317
# Achmad Kabir Rifa'i - 16521371

# PROGRAM marketplace_game_bnmo
# Spesifikasi dapat diakses melalui https://docs.google.com/document/d/1mqODeKIMLjvRmoUb_XQPK7pOifJb-rma83bMuqE9C1s/edit#
# Beberapa spesifikasi diberi fitur tambahan

#Modul buatan
import utility as u

#Modul utama
import F02_register as f02
import F03_login as f03
import F04_tambah_game as f04
import F05_ubah_game as f05
import F06_ubah_stok as f06
import F07_list_game_toko as f07
import F08_buy_game as f08
import F09_list_game as f09
import F10_search_my_game as f10
import F11_search_game_at_store as f11
import F12_topup as f12
import F13_riwayat as f13
import F14_help as f14
import F15_load as f15
import F16_save as f16
import F17_exit as f17

#Modul Bonus
import B01_magicConch as b01
#B02_cipher digunakan di f02 dan f03 
import B03_tictactoe as b03


#KAMUS
key = 11


#PROGRAM UTAMA
datafile = f15.load()
if datafile[0]:
    userArray = datafile[1]
    gameArray = datafile[2]
    riwayatArray = datafile[3]
    kepemilikanArray = datafile[4]

    userInfo = f03.login(userArray, key)
    state = userInfo[1]
    userid = userInfo[0]

    if state != '0' and userid != '0':
        while True:
            prompt = str(input(">> "))

            if prompt == "exit":
                f17.exit(gameArray, userArray, riwayatArray, kepemilikanArray)
                break

            elif prompt == "save":
                f16.save(gameArray, userArray, riwayatArray, kepemilikanArray)

            else:
                if state == 'Admin':
                        
                    if prompt == "register":
                        userArray = f02.register(userArray, key)
                    elif prompt == "logout":
                        userInfo = f03.login(userArray, key)
                        state = userInfo[1]
                        userid = userInfo[0]
                        if state == '0' and userid == '0':
                            f17.exit(gameArray, userArray, riwayatArray, kepemilikanArray)
                            break
                    elif prompt == "tambah_game":
                        gameArray = f04.tambah_game(gameArray)
                    elif prompt == "ubah_game":
                        gameArray = f05.ubah_game(gameArray)
                    elif prompt == "ubah_stok":
                        gameArray = f06.ubah_stok(gameArray)
                    elif prompt == "list_game_toko":
                        f07.list_game_toko(gameArray)
                    elif prompt == 'buy_game':
                        print("Maaf, hanya user yang dapat melakukan hal tersebut.")
                    elif prompt == 'list_game':
                        print("Maaf, hanya user yang dapat melakukan hal tersebut.")
                    elif prompt == 'search_my_game':
                        print("Maaf, hanya user yang dapat melakukan hal tersebut.")
                    elif prompt == "search_game_at_store":
                        f11.search_game_at_store(gameArray)
                    elif prompt == "topup":
                        userArray = f12.topup(userArray)
                    elif prompt == "riwayat":
                        print("Maaf, hanya user yang dapat melakukan hal tersebut.")
                    elif prompt == "help":
                        f14.help(state)
                    elif prompt == "kerangajaib":
                        b01.magicConch()
                    elif prompt == "tictactoe":
                        b03.tictactoe()
                    else:
                        print("Perintah tidak valid (ketik help untuk mencari command)")



                else: #state == 'User':

                    if prompt == 'register':
                        print("Maaf, user tidak memiliki izin untuk menjalankan perintah berikut. Mintalah ke administrator untuk melakukan hal tersebut.")
                    elif prompt == "logout":
                        userInfo = f03.login(userArray, key)
                        state = userInfo[1]
                        userid = userInfo[0]
                        if state == '0' and userid == '0':
                            f17.exit(gameArray, userArray, riwayatArray, kepemilikanArray)
                            break
                    elif prompt == 'tambah_game':
                        print("Maaf, user tidak memiliki izin untuk menjalankan perintah berikut. Mintalah ke administrator untuk melakukan hal tersebut.")
                    elif prompt == 'ubah_game':
                        print("Maaf, user tidak memiliki izin untuk menjalankan perintah berikut. Mintalah ke administrator untuk melakukan hal tersebut.")
                    elif prompt == 'ubah_stok':
                        print("Maaf, user tidak memiliki izin untuk menjalankan perintah berikut. Mintalah ke administrator untuk melakukan hal tersebut.")
                    elif prompt == "list_game_toko":
                        f07.list_game_toko(gameArray)
                    elif prompt == "buy_game":
                        dataUpdate = f08.buy_game(gameArray, riwayatArray, kepemilikanArray, userArray, userid)
                        riwayatArray = dataUpdate[0]
                        kepemilikanArray = dataUpdate[1]
                    elif prompt == "list_game":
                        arrayMilik = f09.list_game(gameArray, kepemilikanArray, userid)
                        if u.panjangArray(arrayMilik) != 1:
                            print("Daftar game:", end='')
                            u.printRapi(arrayMilik)
                    elif prompt == "search_my_game":
                        f10.search_my_game(gameArray, kepemilikanArray, userid)
                    elif prompt == "search_game_at_store":
                        f11.search_game_at_store(gameArray)
                    elif prompt == 'topup':
                        print("Maaf, user tidak memiliki izin untuk menjalankan perintah berikut. Mintalah ke administrator untuk melakukan hal tersebut.")
                    elif prompt == "riwayat":
                        f13.riwayat(riwayatArray, userid)
                    elif prompt == "help":
                        f14.help(state)
                    elif prompt == "kerangajaib":
                        b01.magicConch()
                    elif prompt == "tictactoe":
                        b03.tictactoe()
                    else:
                        print("Perintah tidak valid (ketik help untuk mencari command)")

    else:
        print("\n\nTerima kasih telah menggunakan BNMO.")