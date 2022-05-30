#!/usr/bin/env python3
#  Copyright (c) 2020
#  Author Virgil Hoover
#
#  MIT License
#  Permission is hereby granted, free of charge, to any person obtaining a copy
#  of this software and associated documentation files (the "Software"), to deal
#  in the Software without restriction, including without limitation the rights
#  to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#  copies of the Software, and to permit persons to whom the Software is
#  furnished to do so, subject to the following conditions:
#
#  The above copyright notice and this permission notice shall be included in all
#  copies or substantial portions of the Software.
#
#  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#  IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#  FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#  AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#  LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#  OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
#  SOFTWARE.

from array import array
from locale import setlocale, LC_ALL
from random import choice, shuffle, randint
from string import ascii_uppercase, ascii_lowercase, digits, punctuation
from time import sleep
from enchant import Dict
from pyperclip import copy
from os import system
from pyautogui import press
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import Chrome
from sys import platform

# TODO Make into Flask Application

RED = '\033[1;31;40m'
GREEN = '\033[1;32;40m'
RESET = '\033[1;38;40m'
CYAN = '\033[1;36;40m'
YELLOW = '\033[1;33;40m'


def check_if_password_found(password: str):
    """ Compares a given password to a list of hacked or easily hackable passwords.
    If the password is not found add it to the list to discourage re-use.

    :param password: the password to check for issues.
    """
    password_list = []
    file = '../src/pass.txt'
    with open(file, 'r') as file_reader:
        password_list.append(file_reader.read())

    if (password not in password_list) and (not compare_to_dictionary(password)):
        print(RESET + 'Local Check: ' + GREEN + 'PASS' + RESET)
        print('Remote Check:', check_password_again(password), '\n' + RESET)
        answer = input('Would you like a suggested password? (y/n) ')

        if answer.lower() == 'y':
            password_generator(length=len(password) + 2)

        with open(file, 'a') as file_writer:
            file_writer.write(password)
    else:
        print(RESET + 'Local Check: ' + RED + 'FAIL\n' + RESET)
        password_generator(length=len(password))


def dictionary_check(password: str) -> bool:
    dictionary_string = Dict('en_US')
    setlocale(LC_ALL, 'en_US.UTF-8')
    return dictionary_string.check(password)


def clear_screen():
    if platform == 'linux':
        system('clear')
    elif platform == 'nt':
        system('cls')


def compare_to_dictionary(password: str) -> bool:
    """ Compares given string against English dictionary for match of valid word.
    Called from check_password function.

    :param: password: The password is then checked against the english dictionary.
    """
    dictionary_string = Dict('en_US')
    setlocale(LC_ALL, 'en_US.UTF-8')
    return dictionary_string.check(password)


def password_generator(length: int):
    """ Generates a password of n length, comprised of letters (upper and lower), numbers, and symbols.

    :param length: how many characters the password should be."""
    generated_password = ''
    temporary_list = ''
    combined_list = digits + ascii_uppercase + ascii_lowercase + punctuation
    temporary_password = choice(digits) + choice(ascii_uppercase) + choice(ascii_lowercase) + choice(punctuation)

    # Add 5 to length of temporary_password to help ensure a strong generated one.
    for _ in range(length - len(temporary_password) + 5):
        temporary_password += choice(combined_list)
        temporary_list = array('u', temporary_password)
        shuffle(temporary_list)

    for item in temporary_list:
        generated_password += item

    print('Try this one instead\n' + CYAN + generated_password + RESET)


def copy_to_clipboard(password):
    copy(password)
    countdown(10)
    copy('')


def countdown(t):
    """ Create a countdown object for use in clearing the clipboard. """
    while t:
        _, seconds = divmod(t, 60)
        system('clear')
        print('Results: {:02d}:{:02d}'.format(_, seconds))
        sleep(1)
        t -= 1
        if t == 0:
            system('clear')


def check_password_again(pswd: str) -> str:
    """ Check against a website with known data breach credentials database. Using a Chrome Web Driver.

    :param pswd: the password checked a second time for problems.
    """
    driver = Chrome(executable_path='/home/v/Downloads/chromedriver')
    # Open the website
    driver.get('https://cybernews.com/password-leak-check/')

    # Send Password to check
    text_box = driver.find_element_by_name('p')
    text_box.send_keys(pswd)
    press('enter')
    try:
        if 'detected 1969085 times' in driver.page_source:
            return RED + 'FAIL'
        elif 'didn\'t find your password ' in driver.page_source:
            return GREEN + 'PASS'
        else:
            return YELLOW + 'UNKNOWN'
    except NoSuchElementException:
        return YELLOW + 'UNKNOWN'


if __name__ == '__main__':
    print('Password Check\n')
    print('1. Check a password'
          '2. Generate a password'
          )
    choice = int(input('Enter your choice: '))
    if choice == 1:
        passwd = input('Please enter the password to check: ')
        check_if_password_found(passwd)
    elif choice == 2:
        passwd_length = int(input('How long do you need it to be: '))
        password_generator(passwd_length)
    else:
        print('Invalid choice, please try later.')
