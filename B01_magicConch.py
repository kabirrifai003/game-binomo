import time
import utility as u

def magicConch():
    input("Apa pertanyaanmu pada kulit kerang ajaib? ")

    randomNumber = str(time.time())
    randomNumber = randomNumber[u.panjangArray(randomNumber)-1]

    print("\nKulit kerang ajaib berkata: ", end='')
    if randomNumber == '0':
        print("kali.")
    elif randomNumber == '1':
        print("Ya.")
    elif randomNumber == '2':
        print("Mungkin?")
    elif randomNumber == '3':
        print("Yakali.")
    elif randomNumber == '4':
        print("ga.")
    elif randomNumber == '5':
        print("Tidak.")
    elif randomNumber == '6':
        print("Bisa Jadi.")
    elif randomNumber == '7':
        print("Tentunya.")
    elif randomNumber == '8':
        print("Tidak Mungkin.")
    elif randomNumber == '9':
        print("Ahahaha, Serius?")
    print()
