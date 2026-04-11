class Wallet:
    def __init__(self, dollars):
        self.dollars = dollars

    def __add__(self, other):
        if isinstance(other, Wallet):
            return Wallet(self.dollars + other.dollars)
        return NotImplemented
    
    @property
    def amount(self):
        return self.dollars
    
wallet1 = Wallet(50)
wallet2 = Wallet(30)
merged_wallet = wallet1 + wallet2
print(merged_wallet.amount == 80)       # True