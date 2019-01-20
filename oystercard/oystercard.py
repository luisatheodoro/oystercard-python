class OysterCard:
    MAX_LIMIT = 90
    MIN_FARE = 2.50

    def __init__(self):
        self.balance = 0
        self.is_in_journey = False
        self.entry_station = None

    def top_up(self, value):
        if self._is_max_limit_exceeded(value):
            raise Exception("Your balance is currently {} and your limit is {}".format(self.balance,
                                                                                       self.MAX_LIMIT))
        self.balance += value
        return self.balance

    def touch_in(self, entry_station):
        if self._is_not_enough_funds():
            raise Exception("Your don't have enough funds")
        else:
            self.is_in_journey = True
            self.entry_station = entry_station
            return self.balance

    def touch_out(self):
        self._deduct(self.MIN_FARE)
        self.is_in_journey = False
        self.entry_station = None
        return self.balance

    def _deduct(self, value):
        self.balance -= value
        return self.balance

    def _is_max_limit_exceeded(self, value):
        return self.balance + value > self.MAX_LIMIT

    def _is_not_enough_funds(self):
        return self.balance < self.MIN_FARE
