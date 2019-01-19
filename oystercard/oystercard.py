class OysterCard:
    def __init__(self, balance=0):
        self.balance = balance

    def top_up(self, value):
        self.balance += value
        return self.balance

