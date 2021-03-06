import unittest
import test_helper
from oystercard.oystercard import OysterCard


class OysterCardTest(unittest.TestCase):

    def test_oyster_card_starts_with_zero_balance(self):
        self.assertEqual(OysterCard().balance, 0)

    def test_customer_can_top_up(self):
        oyster_card = OysterCard()
        self.assertEqual(oyster_card.top_up(10), oyster_card.balance)

    def test_raises_error_if_top_up_above_card_limit(self):
        with self.assertRaises(Exception) as cm:
            OysterCard().top_up(91)
        self.assertEqual(
            "Your balance is currently {} and your limit is {}".format(OysterCard().balance,
                                                                       OysterCard().MAX_LIMIT),
            str(cm.exception)
        )

    def test_money_is_deducted_from_balance_at_touch_out(self):
        oyster_card = OysterCard()
        oyster_card.top_up(10)
        self.assertEqual(oyster_card.touch_out(test_helper.aldgate_station()), oyster_card.balance)

    def test_is_not_in_journey_by_default(self):
        self.assertIs(OysterCard()._is_in_journey(), False)

    def test_is_in_journey_after_touch_in(self):
        oyster_card = OysterCard()
        oyster_card.top_up(10)
        oyster_card.touch_in(test_helper.victoria_station())
        self.assertIs(oyster_card._is_in_journey(), True)

    def test_is_not_in_journey_after_touch_out(self):
        oyster_card = OysterCard()
        oyster_card.top_up(10)
        oyster_card.touch_in(test_helper.victoria_station())
        oyster_card.touch_out(test_helper.aldgate_station())
        self.assertIs(oyster_card._is_in_journey(), False)

    def test_raises_error_if_touch_in_without_credit(self):
        with self.assertRaises(Exception) as cm:
            OysterCard().touch_in(test_helper.victoria_station())
        self.assertEqual(
            "Your don't have enough funds",
            str(cm.exception)
        )

    def test_raises_error_if_touch_in_without_min_fare(self):
        with self.assertRaises(Exception) as cm:
            oyster_card = OysterCard()
            oyster_card.top_up(2)
            oyster_card.touch_in(test_helper.victoria_station())
        self.assertEqual(
            "Your don't have enough funds",
            str(cm.exception)
        )

    def test_card_store_entry_station(self):
        oyster_card = OysterCard()
        oyster_card.top_up(10)
        oyster_card.touch_in(test_helper.victoria_station())
        self.assertEqual(oyster_card.entry_station, test_helper.victoria_station())

    def test_card_store_exit_station(self):
        oyster_card = OysterCard()
        oyster_card.top_up(10)
        oyster_card.touch_in(test_helper.victoria_station())
        oyster_card.touch_out(test_helper.aldgate_station())
        self.assertEqual(oyster_card.exit_station, test_helper.aldgate_station())

    def test_card_starts_with_empty_journey_by_default(self):
        self.assertEqual(OysterCard().journeys, {})

    def test_touch_in_touch_out_creates_a_journey(self):
        oyster_card = OysterCard()
        oyster_card.top_up(10)
        oyster_card.touch_in(test_helper.victoria_station())
        oyster_card.touch_out(test_helper.aldgate_station())
        self.assertEqual(oyster_card.journeys, test_helper.journey())


if __name__ == "__main__":
    unittest.main()
