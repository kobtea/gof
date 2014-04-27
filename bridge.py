#!/usr/bin/env python
import abc


class Display:
    def __init__(self, impl_obj):
        self.impl = impl_obj

    def open(self):
        self.impl.raw_open()

    def print(self):
        self.impl.raw_print()

    def close(self):
        self.impl.raw_close()

    def display(self):
        self.open()
        self.print()
        self.close()


class CountDisplay(Display):
    def __init__(self, impl_obj):
        super().__init__(impl_obj)

    def multi_display(self, times):
        self.open()
        for _ in range(times):
            self.print()
        self.close()


class DisplayImpl(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def raw_open(self):
        pass

    @abc.abstractmethod
    def raw_print(self):
        pass

    @abc.abstractmethod
    def raw_close(self):
        pass


class StringDisplayImpl(DisplayImpl):
    def __init__(self, string):
        self.string = string
        self.width = len(self.string)

    def raw_open(self):
        print('+', '-' * self.width, '+')

    def raw_print(self):
        print('|', self.string, '|')

    def raw_close(self):
        print('+', '-' * self.width, '+')


if __name__ == '__main__':
    d1 = Display(StringDisplayImpl('Hello Bridge Pattern'))
    d2 = CountDisplay(StringDisplayImpl('This is Multi-Display'))
    d1.display()
    d2.display()
    d2.multi_display(5)

    '''
+ -------------------- +
| Hello Bridge Pattern |
+ -------------------- +
+ --------------------- +
| This is Multi-Display |
+ --------------------- +
+ --------------------- +
| This is Multi-Display |
| This is Multi-Display |
| This is Multi-Display |
| This is Multi-Display |
| This is Multi-Display |
+ --------------------- +
    '''
