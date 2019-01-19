class OysterCard:
    MAX_LIMIT = 90

    def __init__(self):
        self.balance = 0
        self.is_in_journey = False

    def top_up(self, value):
        if self._is_max_limit_exceeded(value):
            raise Exception("Your balance is currently {} and your limit is {}".format(self.balance,
                                                                                       self.MAX_LIMIT))
        self.balance += value
        return self.balance

    def deduct(self, value):
        self.balance -= value
        return self.balance

    def touch_in(self):
        self.is_in_journey = True

    def touch_out(self):
        self.is_in_journey = False

    def _is_max_limit_exceeded(self, value):
        return self.balance + value > self.MAX_LIMIT
