class BankAccount:
    def __init__(self, starting_balance):
        self._balance = starting_balance

    def balance_is_positive(self):
        return self.balance > 0

    @property
    def balance(self):
        return self._balance

# Alyssa is correct because self.balance will
# simply be routed through the balance property
# and obtain self._balance anyway, which is
# a more idiosyncratic approach anyway.