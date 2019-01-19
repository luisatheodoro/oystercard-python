class OysterCard:

    def __init__(self, balance=0):
        self.balance = balance
        self.MAX_LIMIT = 90

    def top_up(self, value):
        if self._is_max_limit_exceeded:
            raise Exception("Your balance is currently {} and your limit is {}".format(self.balance,
                                                                                       self.MAX_LIMIT))
        self.balance += value
        return self.balance

    def _is_max_limit_exceeded(self, value):
        return self.balance + value > self.MAX_LIMIT
