import numpy as np
from settings import *

class Deck:
    def __init__(self, size) -> None:
        self.abilities = {"3 coin treasure":1, "block foreign aid":2, "assassinate":3,
                          "exchange":4, "block steal":5, "steal":6, "block assassinate":7}
        
        self.card_types = {"Duke":[self.abilities["3 coin treasure"], self.abilities["block foreign aid"]],
                           "Assassin":[self.abilities["assassinate"]],
                           "Ambassador":[self.abilities["exchange"], self.abilities["block steal"]],
                           "Captain":[self.abilities["steal"], self.abilities["block steal"]],
                           "Contessa":[self.abilities["block assasinate"]]}
        
        self.deck = []

    def create_deck(self) -> None:
        num_to_deal = len(DECK_SIZE)/5
        to_deal = {"Duke":num_to_deal,
                   "Assassin":num_to_deal,
                   "Ambassador":num_to_deal,
                   "Captain":num_to_deal,
                   "Contessa":num_to_deal}
        for i in range(DECK_SIZE):
            card = np.random.choice(list(to_deal.keys()))

    def shuffle(self) -> None:
        pass

    def get_card(self) -> int:
        return self.deck.pop()
    
    def return_card(self) -> None:
        pass
