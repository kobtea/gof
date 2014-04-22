#!/usr/bin/env python
import abc


class AbstractDisplay(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def open(self):
        pass

    @abc.abstractmethod
    def print(self):
        pass

    @abc.abstractmethod
    def close(self):
        pass

    def display(self):
        self.open()
        for _ in range(5):
            self.print()
        self.close()


class CharDisplay(AbstractDisplay):
    def __init__(self, chars):
        self.chars = chars

    def open(self):
        print('<<', end='')

    def print(self):
        print(self.chars, end='')

    def close(self):
        print('>>')


class StringDisplay(AbstractDisplay):
    def __init__(self, string):
        self.string = string

    def open(self):
        print('+', '-' * len(self.string), '+')

    def print(self):
        print('|', self.string, '|')

    def close(self):
        print('+', '-' * len(self.string), '+')

if __name__ == '__main__':
    char_display = CharDisplay('H')
    char_display.display()
    string_display = StringDisplay('hogehoge')
    string_display.display()

    '''
    <<HHHHH>>
    + -------- +
    | hogehoge |
    | hogehoge |
    | hogehoge |
    | hogehoge |
    | hogehoge |
    + -------- +
    '''
