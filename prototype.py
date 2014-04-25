#!/usr/bin/env python
import copy


class Manager:
    def __init__(self):
        self.showcase = {}

    def register(self, name, obj):
        self.showcase[name] = obj

    def clone(self, name):
        return copy.deepcopy(self.showcase[name])


class MessageBox:
    def __init__(self, deco_char):
        self.deco_char = deco_char

    def display(self, message):
        print(self.deco_char * (len(message) + len(self.deco_char) * 2 + 2))
        print('{0} {1} {0}'.format(self.deco_char, message))
        print(self.deco_char * (len(message) + len(self.deco_char) * 2 + 2))


if __name__ == '__main__':
    manager = Manager()
    box1 = MessageBox('*')
    manager.register('ast', box1)
    box2 = manager.clone('ast')
    print(id(box1))
    print(id(box2))
    box1.display('hogehoge')
    box2.display('hogehoge')
