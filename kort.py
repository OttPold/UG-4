import os


class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value


    def show(self):
        return f"{self.suit} {self.value}"
    

    def __str__(self):
        return f"{self.suit} {self.value}"

    def __repr__(self):
        return f"{self.suit} {self.value}"


def create_deck():
    cards = []

    suits = ["♠", "♥", "♣", "♦"]
    values = ["A", 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K"]


    for suit in suits:
        for value in values:
            cards.append(Card(suit, value))


    for card in cards:
        print(card)

    return cards



os.system("cls")


create_deck()


