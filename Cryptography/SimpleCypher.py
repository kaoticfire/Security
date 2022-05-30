"""
This program provides a variation on a standard shift cypher. It was originally used to pass messages
back in high school.

Written May 2, 2022
"""
from datetime import datetime
__author__ = 'Virgil Hoover'
__version__ = '1.0'


def cypher_math() -> int:
    """ Returns and integer calculated for today's date."""

    currently = datetime.today()
    year = currently.year
    month = currently.month
    day = currently.day
    added = []
    divided = int(year / day / month)
    x = [int(a) for a in str(divided)]
    for i in x:
        added.append(int(i))
    return sum(added)


def encrypt_text(text: str, algorythm: int) -> str:
    """ Returns an encrypted sting derived from the provided text

        :param text: provided text to encrypt
        :param algorythm: the number of digits to shift left or right, calculated from today's date
        :returns encrypted_text: the resulting string of characters
        """

    chunk_length = 2
    step_one = [text[i:i+chunk_length] for i in range(0, len(text), chunk_length)]
    step_two = []
    step_three = []
    step_four = []
    encrypt = ''

    # Convert the list containing the elements of the string to ascii
    for item in step_one:
        for bit in item:
            step_two.append(ord(bit))

    for ordinal in step_two:
        ordinal = str(ordinal + algorythm)
        step_three.append(ordinal)

    # Convert the list of ascii values back into a string
    for i in step_three:
        if int(i) > 128:
            i = (128 - int(i))
        step_four.append(chr(int(i)))
        encrypt = ''.join(step_four)

    step_five = [encrypt[i:i+chunk_length] for i in range(0, len(encrypt), chunk_length)]
    encrypted_text = ' '.join(step_five)

    return encrypted_text


def decrypt_text(text: str, algorythm: int) -> str:
    """ Returns a decrypted sting derived from the provided text

        :param text: provided text to decrypt
        :param algorythm: the number of digits to shift left or right, calculated from today's date
        :returns decrypted_text: the resulting string of characters
        """

    chunk_size = 2
    text = text.replace(' ', '')
    step_five = [text[i:i+chunk_size] for i in range(0, len(text), chunk_size)]
    step_four = []
    step_three = []
    step_two = []
    decrypted_text = ''
    for item in step_five:
        for bit in item:
            step_four.append(ord(bit))

    for ordinal in step_four:
        ordinal = str(ordinal - algorythm)
        step_three.append(ordinal)

    for i in step_three:
        if int(i) < algorythm:
            i = (int(i) + 128)
        step_two.append(chr(int(i)))
        decrypted_text = ''.join(step_two)

    return decrypted_text


if __name__ == '__main__':
    msg = 'Hello, this is a sample text'
    shift = cypher_math()
    new_msg = encrypt_text(msg, shift)
    original_msg = decrypt_text(new_msg, shift)

    print(msg, ' | encrypts into | ', new_msg)
    print(new_msg, ' | decrypts into | ', original_msg)
