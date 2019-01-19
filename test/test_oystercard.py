import unittest
from oystercard.oystercard import OysterCard


class OysterCardTest(unittest.TestCase):

    def test_oyster_card_starts_with_zero_balance(self):
        self.assertEqual(OysterCard().balance, 0)

    def test_customer_can_top_up(self):
        self.assertEqual(OysterCard().top_up(10), 10)

    def test_raises_error_if_top_up_above_card_limit(self):
        with self.assertRaises(Exception) as cm:
            OysterCard().top_up(91)
        self.assertEqual(
            "Your balance is currently {} and your limit is {}".format(OysterCard().balance,
                                                                       OysterCard().MAX_LIMIT),
            str(cm.exception)
        )

    def test_money_is_deducted_from_balance(self):
        oyster_card = OysterCard()
        print oyster_card.top_up(10)
        self.assertEqual(oyster_card.deduct(4), 6)


if __name__ == "__main__":
    unittest.main()
