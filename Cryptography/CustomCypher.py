""" A custom cypher to use for encryption.  This is a utility module. """
__author__ = 'Virgil Hoover'
__version__= '1.0.0'
__written__= 'January 1, 2022'


def encrypt_string(words: str) -> str:
    """ Takes a string, shifts each letter by two and breaks into two letter chunks. """
    encrypted_word = []
    final_string = ''
    for word in words:
        for letter in word:
            temp_value = ord(letter)
            temp_value += 2
            hidden_letter = chr(temp_value)
            encrypted_word.append(hidden_letter)
            encrypted_string = ''.join(encrypted_word)
            n = 2
            chunks = [encrypted_string[i:i + n] for i in range(0, len(encrypted_string), n)]
            final_string = ' '.join(chunks)
    return final_string


def decrypt_string(encrypted: str) -> str:
    """ Takes an encrypted string (encrypted by above function) and decrypts it. """
    pass


if __name__ == '__main__':
    WORDS = 'Hello World'
    print(encrypt_string(WORDS))
