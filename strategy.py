#!/usr/bin/env python
import random


class WinningStrategy:
    def __init__(self):
        self.won = False
        self.prev_hand = 0

    def next_hand(self):
        if not self.won:
            self.prev_hand = random.randint(0, 2)
        return self.prev_hand

    def study(self, is_win):
        self.won = is_win


class ProbStrategy:
    def __init__(self):
        self.prev_hand = 0
        self.curr_hand = 0
        # history[previous_hand][current_hand] = won_size
        self.history = [
            [1, 1, 1],
            [1, 1, 1],
            [1, 1, 1]
        ]

    def next_hand(self):
        bet = random.randint(0, sum(self.history[self.prev_hand]))
        if bet < self.history[self.prev_hand][0]:
            return 0
        elif bet < self.history[self.prev_hand][0] \
                + self.history[self.prev_hand][1]:
            return 1
        else:
            return 2

    def study(self, is_win):
        if is_win:
            self.history[self.prev_hand][self.curr_hand] += 1
        else:
            self.history[self.prev_hand][self.curr_hand + 1] += 1
            self.history[self.prev_hand][self.curr_hand + 2] += 1


class Player:
    def __init__(self, name, strategy):
        self.name = name
        self.strategy = strategy
        self.count = {'win': 0, 'lose': 0, 'even': 0}

    def next_hand(self):
        return self.strategy.next_hand()

    def win(self):
        self.strategy.study(True)
        self.count['win'] += 1

    def lose(self):
        self.strategy.study(False)
        self.count['lose'] += 1

    def even(self):
        self.count['even'] += 1


class Game:
    @classmethod
    def fight(cls, hand1, hand2):
        if hand1 == hand2:
            return 0
        elif (hand1 + 1) % 3 == hand2:
            return 1
        else:
            return -1


if __name__ == '__main__':
    player1 = Player('hogemi', WinningStrategy())
    player2 = Player('foobar', ProbStrategy())
    for _ in range(10000):
        player1_hand = player1.next_hand()
        player2_hand = player2.next_hand()
        result = Game.fight(player1_hand, player2_hand)
        if result == 0:
            player1.even()
            player2.even()
        elif result == 1:
            player1.win()
            player2.lose()
        elif result == -1:
            player2.win()
            player1.lose()

    print('{} is score: {}'.format(player1.name, player1.count))
    print('{} is score: {}'.format(player2.name, player2.count))

    '''
    hogemi is score: {'lose': 3353, 'even': 3333, 'win': 3314}
    foobar is score: {'lose': 3314, 'even': 3333, 'win': 3353}
    '''
