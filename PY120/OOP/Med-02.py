import random

class GuessingGame:
    def play(self):
        self.number = random.randint(1, 100)
        self.guesses_remaining = 7

        while self.guesses_remaining > 0:
            print(f'You have {self.guesses_remaining} guesses remaining.')
            guess = self.get_guess()
            if guess > self.number:
                print('Your guess is too high.')
            elif guess < self.number:
                print('Your guess is too low.')
            else:
                print("That's the number!\n\nYou won!")
                return
            
            self.guesses_remaining -= 1
        print('You have no more guesses. You lost!')

    def get_guess(self):
        while True:
            try:
                guess = int(input("Enter a number between 1 and 100: "))
            except ValueError:
                print("Invalid guess. Please enter a number.")
                continue
            if guess < 1 or guess > 100:
                print('Invalid guess.')
                continue
            else:
                return guess        

game = GuessingGame()
game.play()

'''
You have 7 guesses remaining.
Enter a number between 1 and 100: 104
Invalid guess. Enter a number between 1 and 100: 50
Your guess is too low.

You have 6 guesses remaining.
Enter a number between 1 and 100: 75
Your guess is too low.

You have 5 guesses remaining.
Enter a number between 1 and 100: 85
Your guess is too high.

You have 4 guesses remaining.
Enter a number between 1 and 100: 0
Invalid guess. Enter a number between 1 and 100: 80
Your guess is too low.

You have 3 guesses remaining.
Enter a number between 1 and 100: 81
That's the number!

You won!

game.play()

You have 7 guesses remaining.
Enter a number between 1 and 100: 50
Your guess is too high.

You have 6 guesses remaining.
Enter a number between 1 and 100: 25
Your guess is too low.

You have 5 guesses remaining.
Enter a number between 1 and 100: 37
Your guess is too high.

You have 4 guesses remaining.
Enter a number between 1 and 100: 31
Your guess is too low.

You have 3 guesses remaining.
Enter a number between 1 and 100: 34
Your guess is too high.

You have 2 guesses remaining.
Enter a number between 1 and 100: 32
Your guess is too low.

You have 1 guess remaining.
Enter a number between 1 and 100: 32
Your guess is too low.

You have no more guesses. You lost!
'''

# Original Attempt
'''
import random

class GuessingGame:
    def play(self):
        self.number = random.randint(1, 100)
        self.guesses_remaining = 7
        print(f'You have {self.guesses_remaining} guesses remaining.')
        self.receive_guess()

    def update_status(self):
        self.guesses_remaining -= 1
        if self.guesses_remaining == 0:
            print('You have no more gueses. You lost!')
        else:
            print(f'You have {self.guesses_remaining} guesses remaining.')

    def receive_guess(self):
        self.guess = int(input("Enter a number between 1 and 100: "))
        if self.guess < 1 or self.guess > 100:
            print('Invalid guess.')
            self.receive_guess()
        else:
            if self.guess > self.number:
                print('Your guess is too high.')
                self.update_status()
                if self.guesses_remaining:
                    self.receive_guess()
            elif self.guess < self.number:
                print('Your guess is too low.')
                self.update_status()
                if self.guesses_remaining:
                    self.receive_guess()
            else:
                print("That's the number!\n\nYou won!")
'''