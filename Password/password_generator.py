from random import choice, shuffle, randint
from string import ascii_lowercase, ascii_uppercase, digits, punctuation


def password(length, num=False, strength='weak'):
    """length of password, num if you want a number,
    and strength(weak, strong, very)"""
    lower = ascii_lowercase
    upper = ascii_uppercase
    letter = lower + upper
    digi = digits
    punc = punctuation
    passwd = ''
    if strength == 'weak':
        if num:
            length -= 2
            for i in range(2):
                passwd += choice(digi)
        for i in range(length):
            passwd += choice(lower)
    elif strength == 'strong':
        if num:
            length -= 2
            for i in range(2):
                passwd += choice(digi)
        for i in range(length):
            passwd += choice(letter)
    elif strength == 'very':
        rand_num = randint(2, 4)
        if num:
            length -= rand_num
            for i in range(rand_num):
                passwd += choice(digi)
            for i in range(rand_num):
                passwd += choice(punc)
            for i in range(length):
                passwd += choice(letter)

    passwd = list(passwd)
    shuffle(passwd)
    return ''.join(passwd)


if __name__ == '__main__':
    print(password(5, num=True))
    print(password(10, num=True, strength='strong'))
    print(password(15, num=True, strength='very'))
