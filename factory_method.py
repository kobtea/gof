#!/usr/bin/env python
import abc


class Product(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def use(self):
        pass


class Factory(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def create_product(self):
        pass

    @abc.abstractmethod
    def register_product(self):
        pass

    def create(self, owner):
        product = self.create_product(owner)
        self.register_product(product)
        return product


class IDCard(Product):
    def __init__(self, owner):
        print("Create {0}'s ID Card ...".format(owner))
        self.__owner = owner

    def use(self):
        print("Use {0}'s ID Card !".format(self.__owner))

    @property
    def owner(self):
        return self.__owner


class IDCardFactory(Factory):
    def __init__(self):
        self.__owners = []

    def create_product(self, owner):
        return IDCard(owner)

    def register_product(self, product):
        self.__owners.append(product)

    @property
    def owners(self):
        return self.__owners


if __name__ == '__main__':
    id_factory = IDCardFactory()
    card1 = id_factory.create('hogeta')
    card2 = id_factory.create('fooman')
    card3 = id_factory.create('barko')
    card1.use()
    card2.use()
    card3.use()

    '''
    Create hogeta's ID Card ...
    Create fooman's ID Card ...
    Create barko's ID Card ...
    Use hogeta's ID Card !
    Use fooman's ID Card !
    Use barko's ID Card !
    '''
