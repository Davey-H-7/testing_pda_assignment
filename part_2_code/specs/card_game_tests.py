import unittest
from src.card import Card
from src.card_game import CardGame

class TestCardGame(unittest.TestCase):
    
    def setUp(self):
        self.card1 = Card("Heart", 8)
        self.card2 = Card("Diamond", 3)
        self.card3 = Card("Spade", 1)

    def testCanCheckForAce(self):
        test = CardGame.check_for_ace(self, self.card3)
        self.assertEqual(True, test)

    def testCanGetHighestCard(self):
        test = CardGame.highest_card(self, self.card1, self.card2)
        self.assertEqual(self.card1, test)

    def testCardsTotal(self):
        cards = [self.card1, self.card2, self.card3]
        test = CardGame.cards_total(self, cards)
        self.assertEqual('You have a total of 12', test)