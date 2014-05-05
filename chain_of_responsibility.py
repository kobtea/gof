#!/usr/bin/env python


class Trouble:
    def __init__(self, number):
        self.number = number

    def __str__(self):
        return '<Trouble: {}>'.format(self.number)


class Support:
    def __init__(self, name):
        self.name = name
        self.next = None

    def set_next(self, next):
        self.next = next
        return self.next

    def support(self, trouble):
        if self.resolve(trouble):
            self.done(trouble)
        elif self.next:
            self.next.support(trouble)
        else:
            self.fail(trouble)

    def resolve(self):
        pass

    def done(self, trouble):
        print('{} is resolved by {}.'.format(trouble, self))

    def fail(self, trouble):
        print('{} cannot be resolved.'.format(trouble))

    def __str__(self):
        return '[ {} ]'.format(self.name)


class NoSupport(Support):
    def __init__(self, name):
        super().__init__(name)

    def resolve(self, trouble):
        return False


class LimitSupport(Support):
    def __init__(self, name, limit):
        super().__init__(name)
        self.limit = limit

    def resolve(self, trouble):
        if (trouble.number < self.limit):
            return True
        else:
            return False


class OddSupport(Support):
    def __init__(self, name):
        super().__init__(name)

    def resolve(self, trouble):
        if (trouble.number % 2 == 1):
            return True
        else:
            return False


class SpecialSupport(Support):
    def __init__(self, name, number):
        super().__init__(name)
        self.number = number

    def resolve(self, trouble):
        if (trouble.number == self.number):
            return True
        else:
            return False


if __name__ == '__main__':
    alice = NoSupport('Alice')
    bob = LimitSupport('Bob', 100)
    charlie = SpecialSupport('Charlie', 429)
    diana = LimitSupport('Diana', 200)
    elmo = OddSupport('Elmo')
    fred = LimitSupport('Fred', 300)

    alice.set_next(bob).set_next(charlie).set_next(diana). \
        set_next(elmo).set_next(fred)

    i = 0
    while(i < 500):
        alice.support(Trouble(i))
        i += 33

    '''
    <Trouble: 0> is resolved by [ Bob ].
    <Trouble: 33> is resolved by [ Bob ].
    <Trouble: 66> is resolved by [ Bob ].
    <Trouble: 99> is resolved by [ Bob ].
    <Trouble: 132> is resolved by [ Diana ].
    <Trouble: 165> is resolved by [ Diana ].
    <Trouble: 198> is resolved by [ Diana ].
    <Trouble: 231> is resolved by [ Elmo ].
    <Trouble: 264> is resolved by [ Fred ].
    <Trouble: 297> is resolved by [ Elmo ].
    <Trouble: 330> cannot be resolved.
    <Trouble: 363> is resolved by [ Elmo ].
    <Trouble: 396> cannot be resolved.
    <Trouble: 429> is resolved by [ Charlie ].
    <Trouble: 462> cannot be resolved.
    <Trouble: 495> is resolved by [ Elmo ].
    '''
