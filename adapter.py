#!/usr/bin/env python


class Banner:
    def __init__(self, string):
        self.__string = string

    def show_with_paren(self):
        print('({0})'.format(self.__string))

    def show_with_aster(self):
        print('*{0}*'.format(self.__string))


class PrintBanner(Banner):
    def __init__(self, string):
        super().__init__('hogehoge')

    def print_weak(self):
        self.show_with_paren()

    def print_strong(self):
        self.show_with_aster()


if __name__ == '__main__':
    adapter = PrintBanner('hogehoge')
    adapter.print_weak()    # (hogehoge)
    adapter.print_strong()  # *hogehoge*
