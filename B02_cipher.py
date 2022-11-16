import utility as u

def encrypt(text, key):
#Metode yang digunakan adalah keyed caesar cipher
    temp =''
    for i in range(u.panjangArray(text)):
        if ord(text[i]) + key > 126:
            temp += chr(ord(text[i]) + key - 127 + 32)
        else:
            temp += chr(ord(text[i]) + key)
    return temp

def decrypt(text, key):
    temp =''
    for i in range(u.panjangArray(text)):
        if ord(text[i]) - key < 32:
            temp += chr(ord(text[i]) - key + 126 - 31)
        else:
            temp += chr(ord(text[i]) - key)
    return temp
