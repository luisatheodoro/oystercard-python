class OysterCard:

    def __init__(self, balance=0):
        self.balance = balance
        self.MAX_LIMIT = 90

    def top_up(self, value):
        if self.balance + value > self.MAX_LIMIT:
            raise Exception("Your balance is currently {} and your limit is {}".format(self.balance,
                                                                                       self.MAX_LIMIT))
        self.balance += value
        return self.balance
