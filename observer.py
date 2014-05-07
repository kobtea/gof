#!/usr/bin/env python
import random


class NumberGenerator:
    def __init__(self):
        self.observers = []

    def add_observer(self, observer):
        self.observers.append(observer)

    def delete_observer(self, observer):
        self.observers.remove(observer)

    def notify_observers(self):
        for observer in self.observers:
            observer.update(self)

    def get_number(self):
        pass

    def execute(self):
        pass


class RandomNumberGenerator(NumberGenerator):
    def __init__(self):
        super().__init__()
        self.random = 0
        self.number = None

    def get_number(self):
        return self.number

    def execute(self):
        for i in range(10):
            self.number = random.randint(0, 50)
            self.notify_observers()


class DigitObserver:
    def update(self, generator):
        print('DigitObserver : {}'.format(generator.get_number()))


class GraphObserver:
    def update(self, generator):
        print('GraphObserver : ', end='')
        print('*' * generator.get_number())


if __name__ == '__main__':
    generator = RandomNumberGenerator()
    observer1 = DigitObserver()
    observer2 = GraphObserver()
    generator.add_observer(observer1)
    generator.add_observer(observer2)
    generator.execute()

    '''
    DigitObserver : 6
    GraphObserver : ******
    DigitObserver : 39
    GraphObserver : ***************************************
    DigitObserver : 21
    GraphObserver : *********************
    DigitObserver : 27
    GraphObserver : ***************************
    DigitObserver : 37
    GraphObserver : *************************************
    DigitObserver : 20
    GraphObserver : ********************
    DigitObserver : 31
    GraphObserver : *******************************
    DigitObserver : 35
    GraphObserver : ***********************************
    DigitObserver : 25
    GraphObserver : *************************
    DigitObserver : 40
    GraphObserver : ****************************************
    '''
