#!/usr/bin/env python
import abc


class Display(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def get_columns(self):
        pass

    @abc.abstractmethod
    def get_rows(self):
        pass

    @abc.abstractmethod
    def get_row_text(self):
        pass

    def show(self):
        for i in range(self.get_rows()):
            print(self.get_row_text(i))


class StringDisplay(Display):
    def __init__(self, string):
        self.string = string

    def get_columns(self):
        return len(self.string)

    def get_rows(self):
        return 1

    def get_row_text(self, row_num):
        if (row_num == 0):
            return self.string
        else:
            return None


class Border(Display):
    def __init__(self, display):
        self.display = display


class SideBorder(Border):
    def __init__(self, display, deco_char):
        super().__init__(display)
        self.deco_char = deco_char

    def get_columns(self):
        return self.display.get_columns() + 2

    def get_rows(self):
        return self.display.get_rows()

    def get_row_text(self, row_num):
        return self.deco_char \
            + self.display.get_row_text(row_num) \
            + self.deco_char


class FullBorder(Border):
    def __init__(self, display):
        super().__init__(display)

    def get_columns(self):
        return self.display.get_columns() + 2

    def get_rows(self):
        return self.display.get_rows() + 2

    def get_row_text(self, row_num):
        if (row_num == 0) or \
           (row_num == self.display.get_rows() + 1):
            return '+' + '-' * self.display.get_columns() + '+'
        else:
            return '|{}|'.format(self.display.get_row_text(row_num - 1))


if __name__ == '__main__':
    b1 = StringDisplay('Deco Deco')
    b2 = SideBorder(b1, '#')
    b3 = FullBorder(b2)
    b1.show()
    b2.show()
    b3.show()

    '''
    Deco Deco
    #Deco Deco#
    +-----------+
    |#Deco Deco#|
    +-----------+
    '''
