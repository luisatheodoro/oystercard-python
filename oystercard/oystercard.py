class OysterCard:
    MAX_LIMIT = 90
    MIN_FARE = 2.50

    def __init__(self):
        self.balance = 0
        self.entry_station = None
        self.exit_station = None
        self.journeys = {}

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
            self.entry_station = entry_station
            return self.balance

    def touch_out(self, exit_station):
        self._deduct(self.MIN_FARE)
        self.exit_station = exit_station
        self._add_to_journeys_dict(self.entry_station, self.exit_station)
        self.entry_station = None
        return self.balance

    def _add_to_journeys_dict(self, entry_station, exit_station):
        self.journeys[len(self.journeys) + 1] = {"entry_station": entry_station, "exit_station": exit_station}

    def _deduct(self, value):
        self.balance -= value

    def _is_max_limit_exceeded(self, value):
        return self.balance + value > self.MAX_LIMIT

    def _is_not_enough_funds(self):
        return self.balance < self.MIN_FARE

    def _is_in_journey(self):
        if self.entry_station is None:
            return False
        else:
            return True
