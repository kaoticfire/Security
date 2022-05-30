# ./venv/bin/python3

from os import listdir
from os.path import isfile
from cryptography.fernet import Fernet


def file_decryption():
    """ Decrpyt files with given key. """
    files = []
    ignored_files = ['file_encryption.py', 'key.key', 'file_decryption.py']
    for file in listdir():
        if file in ignored_files:
            continue
        if isfile(file):
            files.append(file)

    with open('key.key', 'rb') as file_reader:
        key = file_reader.read()

    for victim in files:
        with open(victim, 'rb') as file_read:
            doomed_contents = file_read.read()
        decrypted_contents = Fernet(key).decrypt(doomed_contents)
        with open(victim, 'wb') as file_writer:
            file_writer.write(decrypted_contents)


if __name__ == '__main__':
    file_decryption()
