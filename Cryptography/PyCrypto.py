""" A program to test out cryptography. """
from cryptography.fernet import Fernet

__prog__ = 'Cryptography'
__author__ = 'Virgil Hoover'
__created__ = 'June 1, 2021'


class Crypto:
    """ A class that can encrypt and decrypt a string of text
    using the cryptography class but with a twist.
    """
    def __init__(self) -> None:
        self.key = Fernet.generate_key()

    def encrypt(self, message: str) -> bytes:
        """Args:
              message: the string to be encrypted.
        """
        f_net = Fernet(self.key)
        encrypted_message = f_net.encrypt(message.encode())
        return encrypted_message

    def decrypt(self, message: bytes) -> str:
        """Args:
               message: the bytes string to be decrypted.
        """
        f_net = Fernet(self.key)
        decrypted_message = f_net.decrypt(message).decode('utf-8')
        return decrypted_message

    @staticmethod
    def break_string(starting_string: str, n=2) -> list:
        """Args:
               starting_string: this is the string to be broken into a list
               n: the number of chunks, default is two.
        """
        end_list = []
        tmp_part = ''
        a_list = [starting_string[i:i+n] for i in range(0, len(starting_string), n)]
        for item in a_list:
            for partial in item:
                new_char = chr(ord(partial) + 7)
                tmp_part += new_char
            end_list.append(tmp_part)
            tmp_part = ''
        return end_list

    @staticmethod
    def combine_string(start_point: list) -> str:
        """Args:
               start_point: the list to be converted back into a string for decoding.
        """
        end_point = ''
        for i in start_point:
            end_point += i
        return end_point

    @staticmethod
    def menu():
        """ A menu for the application. """
        print('1. Encrypt', '\n2. Decrypt')
        answer = int(input('Make a selection: '))
        c = Crypto()
        if answer == 1:
            msg = input('What string do you want to encrypt? ')
            enc_msg = Crypto.encrypt(c, msg)
            print(Crypto.break_string(enc_msg.decode('utf-8')))
        elif answer == 2:
            dec_msg = list(input('What string do you want to decrypt? '))
            dec_str = Crypto.combine_string([dec_msg[i:i + 2] for i in range(0, len(dec_msg), 2)])
            dec_bytes = dec_str.encode('utf-8')
            print(Crypto.decrypt(c, dec_bytes))


if __name__ == __prog__:
    app = Crypto()
    app.menu()
