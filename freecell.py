import random


class Card():

    SUITS = ('club', 'heart', 'spade', 'diamond')
    VALUES = range(1, 14)

    COLORS = {
        'club': 'black',
        'diamond': 'red',
        'heart': 'red',
        'spade': 'black',
    }


    NAMES = {
        1: 'A',
        11: 'J',
        12: 'Q',
        13: 'K',
    }

    def __init__(self, suit, value, name):
        assert suit in self.SUITS
        assert value in self.VALUES
        self.suit = suit
        self.value = value
        self.name = name


    def __eq__(self, other):
        return self.suit == other.face and self.value == other.value


    def __str__(self):
        return '<Card {} {}>'.format(self.suit, self.value)


class Deck:

    def __init__(self, n):
        self.thedeck = []
        self.size = n

        i = 0

        while (i < n):

             self.thedeck.append([0] * n)

        i+=1

    def __str__(self):
        new_string = ''
        for row in self.thedeck:
            for item in row:

                new_string += str(item) + '\t'

            new_string.string("t")
            new_string += "\n"

        return new_string

    def __contains__(self, item):
        return item in self.a

    def __iter__(self):
        return iter(self.ai)

    def __len__(self):
        return len(self.ai)


    def empty(self):
        return not self.ai

    def pop(self):
        return self.ai.pop()

    def push(self, item):
        self.ai.append(item)

    def top(self):
        return self.ai[-1]

def make_board():
    return [Card(*i) for i in Card.product(Card.SUITS, Card.VALUES)]

def shuffled(a):
    random.shuffle(a)
    return a

class FreeCell(Card):

    '''
    Represents a FreeCell game playing field and all possible operations
    '''

    RESERVE_SLOTS = 4
    FOUNDATION_SLOTS = len(Card.SUITS)
    TABLEAU_SLOTS = 8

    def __init__(self, deck=[]):
        '''
        Initializes a FreeCell game; deck is expected to be shuffled
        '''
        super().__init__
        self.reserve = [None] * self.RESERVE_SLOTS
        self.foundation = [deck() for i in range(self.FOUNDATION_SLOTS)]
        self.tableau = [deck() for i in range(self.TABLEAU_SLOTS)]
        self.fill_tableau(deck)

    def __str__(self):
        new_string = ''
        for i in self.tableau:
            new_string += str(i) + '\t'
        return new_string

    def fill_tableau(self, deck):
        slots = Card.cycle(self.tableau)
        for c in deck:
            next(slots).push(c)

    def can_top(self, a, b):
        '''
        Returns whether Card a can be placed, on the tableau, on top of Card b
        '''
        return a.color != b.color and a.value == b.value - 1

    def can_move_to_tableau(self, c, i):
        '''
        Returns whether the given Card c can be moved into tableau slot i
        '''
        t = self.tableau[i]
        return t.empty() or self.can_top(c, t.top())

    def can_move_to_foundation(self, c):
        '''
        Returns whether the given Card can be moved to foundation
        '''
        f = self.foundation[c.face_index]
        return c.value == 1 if f.empty() else (f.top().value == c.value - 1)

    def is_free(self, c):
        '''
        Returns whether the Card has been freed; that is, the Card is not
        contained in either reserve, foundation, or tableau
        '''
        assert isinstance(c, Card)
        return c not in self.reserve and \
            all(c not in f for f in self.foundation) and \
            all(c not in t for t in self.tableau)

    def move_to_foundation(self, c):
        if not self.can_move_to_foundation(c):
            raise ('invalidMove’)

        self.foundation[c.face_index].push(c)

    def move_to_tableau(self, c, i):
        '''
        Moves the given Card c to tableau slot i
        '''
        assert self.is_free(c)

        if not self.can_move_to_tableau(c, i):
            raise InvalidMove

        self.tableau[i].push(c)

    def move_tableau_group(self, a, b, n):
        '''
        Moves n cards from tableau slot a to b
        '''
        if n == 0:
            raise InvalidMove
        if n > self.move_capacity(a, b):
            raise InvalidMove

        ta = self.tableau[a]

        cards = [ta.pop() for i in range(n)]
        [self.move_to_tableau(c, b) for c in reversed(cards)]

    def move_to_reserve(self, c):
        assert self.is_free(c)

        if not self.reserve_free():
            raise InvalidMove

        self.reserve[self.reserve.index(None)] = c

    def move_from_reserve(self, i):
        if self.reserve[i] is None:
            raise MoveFromEmpty

        c = self.reserve[i]
        self.reserve[i] = None
        return c

    def reserve_free(self):
        return not all(self.reserve)

    def won(self):
        return all(t.empty() for t in self.tableau)

def main():

    deck = Deck()
    deck.Card()
    deck.shuffle()
    deck.show()
    deck.build()
    deck.show()

    mygame = FreeCell(deck)
    print(mygame)

if __name__ == "__main__": main()
