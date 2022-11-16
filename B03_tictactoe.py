import utility as u

def kondisiMenang(array):
#untuk bonus tiktaktu
    menang = False
    pemain = ' '
    for i in range(3):
        if array[i][0] == array[i][1] and array[i][0] == array[i][2] and (array[i][0] =='O' or array[i][0] == 'X'):
            menang = True
            pemain = array[i][0]

    if menang == False:
        for i in range(3):
            if array[0][i] == array[1][i] and array[0][i] == array[2][i] and (array[0][i] =='O' or array[0][i] == 'X'):
                menang = True
                pemain = array[0][i]
        if menang == False:
            if array[0][0] == array[1][1] and array[0][0] == array[2][2] and (array[0][0] =='O' or array[0][0] == 'X'):
                menang = True
                pemain = array[0][0]
            else:
                if array[0][2] == array[1][1] and array[0][2] == array[2][0] and (array[0][2] =='O' or array[0][2] == 'X'):
                    menang = True
                    pemain = array[0][2]
    
    return (menang, pemain)

def tictactoe():
    arraytictactoe = [['#' for i in range(3)] for i in range(3)]
    print("Legenda:")
    print("# kosong")
    print("O pemain 1")
    print("X pemain 2")

    while True:
        print("\nStatus papan:")
        for i in range(3):
            for j in range(3):
                print(arraytictactoe[i][j], end='')
            print()
        print()

        while True:
            print("Giliran Pemain O")
            X = input("X: ")
            Y = input("Y: ")
            if not u.angkaSemua(X) or not u.angkaSemua(Y):
                print("Masukan salah.\n")
            else:
                X = int(X)
                Y = int(Y)
                if not ((X <= 3 and X>=1) and (Y <=3 and Y >= 1)):
                    print("Masukan salah.\n")
                else:
                    if arraytictactoe[Y-1][X-1] != '#':
                        print("Masukan salah.\n")
                    else:
                        arraytictactoe[Y-1][X-1] = 'O'
                        break
        kondisi = kondisiMenang(arraytictactoe)
        
        penuh = True
        for i in range(3):
            for j in range(3):
                if arraytictactoe[i][j] == '#':
                    penuh = False
                    break
        if kondisi[0]:
            break
        elif penuh:
            break
        else:
            print("\nStatus papan:")
            for i in range(3):
                for j in range(3):
                    print(arraytictactoe[i][j], end='')
                print()
            print()

            while True:
                print("Giliran Pemain X")
                X = input("X: ")
                Y = input("Y: ")
                if not u.angkaSemua(X) or not u.angkaSemua(Y):
                    print("Masukan salah.\n")
                else:
                    X = int(X)
                    Y = int(Y)
                    if not ((X <= 3 and X>=1) and (Y <=3 and Y >= 1)):
                        print("Masukan salah.\n")
                    else:
                        if arraytictactoe[Y-1][X-1] != '#':
                            print("Masukan salah.\n")
                        else:
                            arraytictactoe[Y-1][X-1] = 'X'
                            break
            kondisi = kondisiMenang(arraytictactoe)
            penuh = True
            for i in range(3):
                for j in range(3):
                    if arraytictactoe[i][j] == '#':
                        penuh = False
                        break
            if kondisi[0]:
                break
            elif penuh:
                break
                
    
    print("\nStatus papan:")
    for i in range(3):
        for j in range(3):
            print(arraytictactoe[i][j], end='')
        print()
    print()

    if kondisi[0]:
        print("\nPemain", kondisi[1], 'menang.\n')
    else:
        print("Permainan berakhir seri.")
