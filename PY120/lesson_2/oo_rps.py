import random

class Player:
    CHOICES =  ('rock', 'paper', 'scissors')

    def __init__(self):
        self.move = None

class Computer(Player):
    def choose(self, last_human_move=None):
        self.move = random.choice(Player.CHOICES)

class R2D2(Computer):
    def choose(self, last_human_move=None):
        self.move = 'rock'

class HAL(Computer):
    def choose(self, last_human_move=None):
        base = list(Player.CHOICES)
        biased = base + ['scissors', 'scissors']
        self.move = random.choice(biased)

class Daneel(Computer):
    def choose(self, last_human_move=None):
        self.move = last_human_move if last_human_move else random.choice(Player.CHOICES)

class Human(Player):
    def choose(self):
        prompt = 'Please choose rock, paper, or scissors: '

        while True:
            choice = input(prompt).lower()
            if choice in Player.CHOICES:
                break
            print(f'Sorry, {choice} is not valid')

        self.move = choice

class RPSGame:
    WINS_FOR_VICTORY = 3
    WINNING_COMBOS = {
        ('rock', 'scissors'),
        ('paper', 'rock'),
        ('scissors', 'paper'),
        }

    def __init__(self):
        self._human = Human()
        self._computer = self._choose_computer()
        self._computer_victories = 0
        self._human_victories = 0
        self.user_moves = []

    def display_welcome_message(self):
        print("Welcome to Rock Paper Scissors!")
        total_games = self.WINS_FOR_VICTORY * 2 - 1
        print(f"This will be a best of {total_games} series.")
        print(f"First to {self.WINS_FOR_VICTORY} wins!")

    def display_goodbye_message(self):
        print('Thanks for playing Rock Paper Scissors. Goodbye!')

    def _choose_computer(self):
        prompt = "Who do you want to play against? (r2d2, hal, daneel, or normal): "
        while True:
            choice = input(prompt).strip().lower()
            if choice == 'r2d2':
                return R2D2()
            elif choice == 'hal':
                return HAL()
            elif choice == 'daneel':
                return Daneel()
            elif choice == 'normal':
                return Computer()
            else:
                print("Sorry, that's not a valid choice.")

    def _round_result(self):
        human_move = self._human.move
        computer_move = self._computer.move

        if human_move == computer_move:
            return 'tie'
        if (human_move, computer_move) in self.WINNING_COMBOS:
            return 'human'
        return 'computer'

    def _update_score(self, result):
        if result == 'human':
            self._human_victories += 1
        elif result == 'computer':
            self._computer_victories += 1

    def reset_series(self):
        self._computer_victories = 0
        self._human_victories = 0
        self.user_moves = []

    def _display_winner(self, result):
        human_move = self._human.move
        computer_move = self._computer.move

        print(f'You chose: {human_move}')
        print(f'The computer chose: {computer_move}')

        if result == 'human':
            print('You win!')
        elif result == 'computer':
            print('Computer wins!')
        else:
            print("It's a tie!")

    def play(self):
        self.display_welcome_message()

        while True:
            while True:
                last_human_move = self.user_moves[-1] if self.user_moves else None
                self._human.choose()
                self._computer.choose(last_human_move)
                self.user_moves.append(self._human.move)
                result = self._round_result()
                self._update_score(result)
                self._display_winner(result)
                self._display_score()
                if self._computer_victories == self.WINS_FOR_VICTORY:
                    print('Computer wins the best of 5 series!')
                    self.reset_series()
                    break
                if self._human_victories == self.WINS_FOR_VICTORY:
                    print('You win the best of 5 series!')
                    self.reset_series()
                    break
                print("Begin next round...")

            if not self._play_again():
                break
        self.display_goodbye_message()

    def _play_again(self):
        answer = input("Would you like to play again? (y/n) ")
        return answer.lower().startswith('y')

    def _display_score(self):
        print(f"Score: You {self._human_victories} - Computer {self._computer_victories}")

    def display_move_history(self):
        if not self.user_moves:
            print("No moves yet.")
        else:
            print(self.user_moves)
            print(", ".join(self.user_moves))

RPSGame().play()
