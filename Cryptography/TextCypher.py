#!/usr/bin/python
""" Command-line based function to encrypt text stored in a file. """
__author__ = 'Virgil Hoover'
__written__ = 'May 17, 2022'
__version__ = '1.0.0'
__name__ = 'TextCypher'
from random import shuffle, seed
from time import time
from argparse import ArgumentParser
import sys


class TextCypher:
    """ A class of Text and string manipulation to hide, encrypt, or otherwise
     make the text un readable without the proper key in some occasions. """
    def __init__(self):
        self.starting_text = []
        self.new_text_list = []
        self.final_list = []
        self.initial_text = ''

    def salt_text(self, options) -> None:
        """ Encrypt text found in a file.

        @param options: the shift value and the divisor are integers that aid in
        salting the test.
        """
        try:
            _parser = ArgumentParser(description='Encrypt some text')
            _parser.add_argument('input_file', type=str,
                                 help='The file in which to read the text')
            _parser.add_argument('-s', '--shift_value', nargs='?', const=10,
                                 metavar='#', type=int, default=5,
                                 help='Integer value of places to shift.')
            _parser.add_argument('-d', '--divisor', nargs='?', const=24,
                                 type=int, metavar='#', default=12,
                                 help='Integer to divide the initial seed by')
            _parser.add_argument('-o', '--output_file', type=str, default=False,
                                 help='The optional output file')
            _parser.add_argument('-v', '--verbose', default=False,
                                 action='store_true',
                                 help='The optional verbose output, enable this'
                                      ' to see the initial text read in.')
            _opts = _parser.parse_args()

            with open(_opts.input_file, 'r') as file_reader:
                self.starting_text.append(file_reader.read())

        except FileNotFoundError:
            print('File not found')
            sys.exit(2)

        except IOError:
            print('Error, reading from disk.')
            sys.exit(1)

        for item in self.starting_text[0].split('\n'):
            for _ in item:
                self.new_text_list.append(ord(_) + int(_opts.shift_value))

        seed(int(time() / int(_opts.divisor)))
        shuffle(self.new_text_list)
        for _ in self.new_text_list:
            self.final_list.append(chr(_))

        initial_text = ' '.join(self.starting_text[0].split('\n'))
        final_text = ' '.join(self.final_list).replace(' ', '')

        if _opts.verbose:
            print('Initial Text:\n', initial_text)
        print('Final Text:\n', final_text)

        if _opts.output_file:
            with open(_opts.output_file, 'w') as file_writer:
                file_writer.write(final_text)
    

if __name__ == 'TextCypher':
    app = TextCypher()
    app.salt_text(sys.argv)
