#!/usr/bin/python
import os
import sys
from cryptography.fernet import Fernet

def write_key():
    key = Fernet.generate_key()
    with open(sys.argv[2], 'wb') as key_file:
        key_file.write(key)

def encrypt(filename, key):
    f = Fernet(key)
    with open(filename, 'rb') as file:
        file_data = file.read()

    encrypted_data = f.encrypt(file_data)
    with open(filename, 'wb') as file:
        file.write(encrypted_data)

def load_key(keyname):
    return open(keyname, 'rb').read()

def decrypt(filename, key):
    f = Fernet(key)
    with open(filename, 'rb') as file:
        encrypted_data = file.read()
    decrypted_data = f.decrypt(encrypted_data)
    with open(filename, 'wb') as file:
        file.write(decrypted_data)

try:
    if __name__ == "__main__":
        
        if sys.argv[1] == '--generate' or sys.argv[1] == '-gen':
            write_key()
            print('created', sys.argv[2])

        elif sys.argv[1] == '-e' or sys.argv[1] == '--encrypt':
            if os.path.exists(sys.argv[3]):
                key = load_key(sys.argv[3])
            else:
                print('cryptkey not exists')
                quit()
            if os.path.exists(sys.argv[2]):
                if os.path.isfile(sys.argv[2]):
                    encrypt(sys.argv[2], key)
                    print('encrypted', sys.argv[2])

                elif os.path.isdir(sys.argv[2]):
                    folder = []
                    for i in os.walk('aesc'):
                        folder.append(i)

                    for address, dirs, files in folder:
                        for file in files:
                            file = address+'/'+file
                            encrypt(file, key)
                            print('encrypted', file)
            else:
                print('''file or dir not exists
type:
aesc --help''')

        elif sys.argv[1] == '-d' or sys.argv[1] == '--decrypt':
            if os.path.exists(sys.argv[3]):
                key = load_key(sys.argv[3])
            else:
                print('cryptkey not exists')
                quit()
            if os.path.exists(sys.argv[2]):
                if os.path.isfile(sys.argv[2]):
                    decrypt(sys.argv[2], key)
                    print('decrypted', sys.argv[2])

                elif os.path.isdir(sys.argv[2]):
                    folder = []
                    for i in os.walk('aesc'):
                        folder.append(i)

                    for address, dirs, files in folder:
                        for file in files:
                            file = address+'/'+file
                            decrypt(file, key)
                            print('decrypted', file)
            else:
                print('''file or dir not exists
type:
aesc --help''')

        elif sys.argv[1] == '-h' or sys.argv[1] == '--help':
                    print('''AES encryptor/decryptor.

    usage: 
    aesc [--option] [dir/file] [cryptkey]       encrypt/decrypt file or dir
    aesc --generate [keyname]                   generate cryptkey
    aesc --help                                 help

    options:
    --encrypt or -e
    --decrypt or -d
    --generate or -gen
    --help or -h''')

        else:
            print('''type:
    aesc --help''')
except:
    print('''type:
aesc --help''')