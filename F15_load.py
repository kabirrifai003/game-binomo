import argparse
import os
import parserCSV

def load():
    parser = argparse.ArgumentParser(description='Load data ke sistem', exit_on_error=False)
    parser.add_argument('nama_folder', type=str, metavar='<nama_folder>')
    
    try:
        parser.error = print('', end='')
        args = parser.parse_args()

    except:
        parser.error = print("\nTidak ada nama folder yang diberikan!\nUsage: python program_binomo.py <nama_folder>")
        return False, [], [], [], []

    folder = args.nama_folder
    path = os.getcwd() + '/' + folder
    if os.path.exists(path):
        print('\nLoading...')
        userArray = open(folder+'\\'+'user.csv')
        gameArray = open(folder+'\\'+'game.csv')
        riwayatArray = open(folder+'\\'+'riwayat.csv')
        kepemilikanArray = open(folder+'\\'+'kepemilikan.csv')
        print('Selamat datang di antarmuka \'Binomo\'!')
        return True, parserCSV.parsedCsv(userArray), parserCSV.parsedCsv(gameArray), parserCSV.parsedCsv(riwayatArray), parserCSV.parsedCsv(kepemilikanArray)
    else:
        print("\nFolder", folder, "tidak ditemukan.")
        return False, [], [], [], []
