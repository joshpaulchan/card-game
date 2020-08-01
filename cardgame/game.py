class Game:
    def __init__(self, players):
        self.players = players
        self._stopped = False

    def step(self):
        raise NotImplementedError

    def start(self):
        while True:
            if self._stopped:
                break

            self.step()

    def stop(self):
        self._stopped = True


class Poker(Game):

    def step(self):
        # 


class Player:
    def __init__(self, _id):
        self._id = _id


# can use decorator to attach functionality (is_flippable)
class Card:
    pass


class CardIterator:
    def __init__(self, cards=None):
        if not cards:
            cards = []

    def draw(self):
        for card in cards:
            yield card


class Deck:

    pass


def main():
    poker = Poker()
    poker.players = set([Player("PC"), Player("0")])


if __name__ == "__main__":
    main()
