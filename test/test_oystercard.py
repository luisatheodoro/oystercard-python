import unittest
from oystercard.oystercard import OysterCard


class OysterCardTest(unittest.TestCase):

    def test_oyster_card_starts_with_zero_balance(self):
        self.assertEqual(OysterCard().balance, 0)

    def test_customer_can_top_up(self):
        self.assertEqual(OysterCard().top_up(10), 10)


if __name__ == "__main__":
    unittest.main()
