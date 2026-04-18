class Game:
    def __init__(self, game):
        self.game = game

    def play(self):
        return 'Start the game!'

class Bingo(Game):
    def __init__(self, game, name):
        super().__init__(game)
        self.name = name

class Scrabble(Game):
    def __init__(self, game, *players):
        super().__init__(game)
        self.players = list(players)


bingo = Bingo('Bingo', 'Bill')
scrabble = Scrabble('Scrabble', 'Jill', 'Sill')
scrabble2 = Scrabble('Scrabble', 'Jill', 'Sill', 'Will')

print(vars(bingo))
print(vars(scrabble))
print(vars(scrabble2))

