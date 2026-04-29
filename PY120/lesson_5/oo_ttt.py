import random
import os

def clear_screen():
    os.system('clear')

def join_or(num_list, separator=', ', final_connector='or'):
    if len(num_list) == 0:
        return ""
    if len(num_list) == 1:
        return str(num_list[0])
    if len(num_list) == 2:
        return f"{num_list[0]} {final_connector} {num_list[1]}"
    full_string = ''
    for num in num_list[0:-1]:
        full_string += str(num)
        full_string += separator
    full_string += f'{final_connector} '
    full_string += str(num_list[-1])
    return full_string

class Square:
    INITIAL_MARKER = " "
    HUMAN_MARKER = "X"
    COMPUTER_MARKER = "O"

    def __init__(self, marker=INITIAL_MARKER):
        self.marker = marker

    def __str__(self):
        return self.marker

    @property
    def marker(self):
        return self._marker

    @marker.setter
    def marker(self, marker):
        self._marker = marker

    def is_unused(self):
        return self.marker == Square.INITIAL_MARKER

class Board:
    def __init__(self):
        self.squares = {key: Square() for key in range(1, 10)}

    def display(self):
        print()
        print("     |     |")
        print(f"  {self.squares[1]}  |"
              f"  {self.squares[2]}  |"
              f"  {self.squares[3]}")
        print("     |     |")
        print("-----+-----+-----")
        print("     |     |")
        print(f"  {self.squares[4]}  |"
              f"  {self.squares[5]}  |"
              f"  {self.squares[6]}")
        print("     |     |")
        print("-----+-----+-----")
        print("     |     |")
        print(f"  {self.squares[7]}  |"
              f"  {self.squares[8]}  |"
              f"  {self.squares[9]}")
        print("     |     |")
        print()

    def mark_square_at(self, key, marker):
        self.squares[key].marker = marker

    def unused_squares(self):
        return [key
                for key, square in self.squares.items()
                if square.is_unused()]

    def is_full(self):
        return len(self.unused_squares()) == 0

    def count_markers_for(self, player, keys):
        markers = [self.squares[key].marker for key in keys]
        return markers.count(player.marker)

    def reset(self):
        self.squares = {key: Square() for key in range(1, 10)}

    def display_with_clear(self):
        clear_screen()
        print("\n")
        self.display()

class Player:
    def __init__(self, marker):
        self.marker = marker

class Human(Player):
    def __init__(self):
        super().__init__(Square.HUMAN_MARKER)

class Computer(Player):
    def __init__(self):
        super().__init__(Square.COMPUTER_MARKER)

class TTTGame:
    WINS_FOR_VICTORY = 3
    TOTAL_GAMES = WINS_FOR_VICTORY * 2 - 1
    POSSIBLE_WINNING_ROWS = (
        (1, 2, 3),  # top row of board
        (4, 5, 6),  # center row of board
        (7, 8, 9),  # bottom row of board
        (1, 4, 7),  # left column of board
        (2, 5, 8),  # middle column of board
        (3, 6, 9),  # right column of board
        (1, 5, 9),  # diagonal: top-left to bottom-right
        (3, 5, 7),  # diagonal: top-right to bottom-left
    )

    def __init__(self):
        self.board = Board()
        self.human = Human()
        self.computer = Computer()
        self._computer_victories = 0
        self._human_victories = 0
        self._first_player = self.human

    def _play_again(self):  
        while True:
            answer = input("Would you like to play another match? (y/n): ")
            if answer.lower() in ('y', 'yes', 'yea'):
                return True
            return False

    def play(self):
        self.display_welcome_message()
        while True:
            self._play_match()
            if not self._play_again():
                break

        self.display_goodbye_message()

    def _play_game(self):
        current_player = self._first_player
        while True:
            self.board.display_with_clear()
            self._player_moves(current_player)
            if self.is_game_over():
                break

            current_player = self._alternate_player(current_player)

    def _play_match(self):
        self.reset_series()
        while (self._computer_victories < self.WINS_FOR_VICTORY and
                    self._human_victories < self.WINS_FOR_VICTORY):
            self.board.reset()
            self._play_game()

            self.board.display_with_clear()
            self._update_score()
            self.display_results()
            self.display_match_status()

            if (self._computer_victories < self.WINS_FOR_VICTORY and
                    self._human_victories < self.WINS_FOR_VICTORY):
                input("\nPress any button to play the next game...")
            self._first_player = self._alternate_player(self._first_player)

        self._display_match_winner()

    def _alternate_player(self, player):
        return self.computer if player == self.human else self.human

    def display_match_status(self):
        print(f'The match score is Computer: {self._computer_victories} - User: {self._human_victories}')

    def _display_match_winner(self):
        if self._computer_victories == self.WINS_FOR_VICTORY:
            print('Computer wins! Better luck next time!')
        else:
            print('You win! Well done, mate!')

    def display_welcome_message(self):
        clear_screen()
        print("Welcome to Tic Tac Toe!")
        print(f"This will be a best of {self.TOTAL_GAMES} series.")
        print(f"First to {self.WINS_FOR_VICTORY} wins!")
        print()

    def display_goodbye_message(self):
        print("Thanks for playing Tic Tac Toe! Goodbye!")

    def _update_score(self):
        if self.is_winner(self.human):
            self._human_victories += 1
        elif self.is_winner(self.computer):
            self._computer_victories += 1

    def reset_series(self):
        self._computer_victories = 0
        self._human_victories = 0

    def display_results(self):
        if self.is_winner(self.human):
            print("\nYou won! Congratulations!")
        elif self.is_winner(self.computer):
            print("\nI won! I won! Take that, human!")
        else:
            print("\nA tie game. How boring.")

    def _player_moves(self, current_player):
        if current_player == self.human:
            self.human_moves()
        else:
            self.computer_moves()

    def human_moves(self):
        choice = None
        while True:
            valid_choices = self.board.unused_squares()
            choices_str = join_or(valid_choices)
            prompt = f"Choose a square ({choices_str}): "
            choice = input(prompt)

            try:
                choice = int(choice)
                if choice in valid_choices:
                    break
            except ValueError:
                pass

            print("Sorry, that's not a valid choice.")
            print()

        self.board.mark_square_at(choice, self.human.marker)

    def _find_critical_square(self, target_marker, opponent_marker):
        for row in self.POSSIBLE_WINNING_ROWS:
            row_total = 0
            critical_location = None
            for num in row:
                if self.board.squares[num].marker == opponent_marker:
                    break
                elif self.board.squares[num].marker == target_marker:
                    row_total += 1
                elif self.board.squares[num].marker == Square.INITIAL_MARKER:
                    critical_location = num
            if row_total == 2 and critical_location:
                return critical_location
        return None

    def computer_moves(self):
        valid_choices = self.board.unused_squares()
        choice = self._find_critical_square(Square.COMPUTER_MARKER,
                                       Square.HUMAN_MARKER)
        if not choice:
            choice = self._find_critical_square(Square.HUMAN_MARKER,
                                           Square.COMPUTER_MARKER)
        if not choice and self.board.squares[5].is_unused():
            choice = 5
        if not choice:
            choice = random.choice(valid_choices)
        self.board.mark_square_at(choice, self.computer.marker)

    def is_game_over(self):
        return self.board.is_full() or self.someone_won()

    def three_in_a_row(self, player, row):
        return self.board.count_markers_for(player, row) == 3

    def someone_won(self):
        return (self.is_winner(self.human) or
                self.is_winner(self.computer))

    def is_winner(self, player):
        for row in TTTGame.POSSIBLE_WINNING_ROWS:
            if self.three_in_a_row(player, row):
                return True

        return False

game = TTTGame()
game.play()