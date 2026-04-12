import random
import math

class GuessingGame:
    def __init__(self, low, high):
        self.low_num = low
        self.high_num = high
        self.number = None
        self.guesses_remaining = None
        
    def reset(self):
        self.number = random.randint(self.low_num, self.high_num)
        number_of_guesses = int(math.log2(self.high_num - self.low_num+ 1)) + 1
        self.guesses_remaining = number_of_guesses

    def play(self):
        self.reset()
        while self.guesses_remaining > 0:
            print(f'You have {self.guesses_remaining} guesses remaining.')
            guess = self.get_guess()
            if guess > self.number:
                print('Your guess is too high.')
            elif guess < self.number:
                print('Your guess is too low.')
            else:
                print("That's the number!")
                print("\nYou won!")
                return
            
            self.guesses_remaining -= 1
        print('You have no more guesses. You lost!')

    def get_guess(self):
        while True:
            try:
                guess = int(input(f"Enter a number between {self.low_num} and {self.high_num}: "))
            except ValueError:
                print("Invalid guess. Must be a number.")
                continue
            if guess < self.low_num or guess > self.high_num:
                print('Invalid guess.')
                continue
            else:
                return guess     

game = GuessingGame(501, 1500)
game.play()
'''
# Winning Result Example:

You have 10 guesses remaining.
Enter a number between 501 and 1500: 104
Invalid guess. Enter a number between 501 and 1500: 1000
Your guess is too low.

You have 9 guesses remaining.
Enter a number between 501 and 1500: 1250
Your guess is too low.

You have 8 guesses remaining.
Enter a number between 501 and 1500: 1375
Your guess is too high.

You have 7 guesses remaining.
Enter a number between 501 and 1500: 80
Invalid guess. Enter a number between 501 and 1500: 1312
Your guess is too low.

You have 6 guesses remaining.
Enter a number between 501 and 1500: 1343
Your guess is too low.

You have 5 guesses remaining.
Enter a number between 501 and 1500: 1359
Your guess is too high.

You have 4 guesses remaining.
Enter a number between 501 and 1500: 1351
Your guess is too low.

You have 3 guesses remaining.
Enter a number between 501 and 1500: 1355
That's the number!

You won!

# Losing Result Example:
You have 10 guesses remaining.
Enter a number between 501 and 1500: 1000
Your guess is too high.

You have 9 guesses remaining.
Enter a number between 501 and 1500: 750
Your guess is too low.

You have 8 guesses remaining.
Enter a number between 501 and 1500: 875
Your guess is too high.

You have 7 guesses remaining.
Enter a number between 501 and 1500: 812
Your guess is too low.

You have 6 guesses remaining.
Enter a number between 501 and 1500: 843
Your guess is too high.

You have 5 guesses remaining.
Enter a number between 501 and 1500: 820
Your guess is too low.

You have 4 guesses remaining.
Enter a number between 501 and 1500: 830
Your guess is too low.

You have 3 guesses remaining.
Enter a number between 501 and 1500: 835
Your guess is too low.

You have 2 guesses remaining.
Enter a number between 501 and 1500: 836
Your guess is too low.

You have 1 guess remaining.
Enter a number between 501 and 1500: 837
Your guess is too low.

You have no more guesses. You lost!
'''