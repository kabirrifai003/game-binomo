import F16_save as f16

def exit(gameArray, userArray, riwayatArray, kepemilikanArray):
    while True:
        saveBeforeExit = str(input("Apakah Anda mau melakukan penyimpanan file yang sudah diubah? (y/n) "))
        if saveBeforeExit == "y" or saveBeforeExit == "Y":
            f16.save(gameArray, userArray, riwayatArray, kepemilikanArray)
        elif saveBeforeExit == "n" or saveBeforeExit == "N":
            break
        else:
            print("Input tidak valid.\n")
    print("\n\nTerima kasih telah menggunakan BNMO.")
