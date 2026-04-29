import random

class Card:
    suits = ('Hearts', 'Spades', 'Diamonds', 'Clubs')
    ranks = (2, 3, 4, 5, 6, 7, 8, 9, 10, 'Jack', 'Queen', 'King', 'Ace')

    def __init__(self, suit, rank):
        self._suit = suit
        self._rank = rank
        self._value = rank if isinstance(rank, int) else 11 if rank == 'Ace' else 10
        self._hidden = False

    @property
    def value(self):
        return self._value

    @property
    def hidden(self):
        return self._hidden

    def hide(self):
        self._hidden = True

    def reveal(self):
        self._hidden = False

    @property
    def rank(self):
        return self._rank

    def __str__(self):
        if self._hidden:
            return 'Hidden'
        return f"{self._rank} of {self._suit}"

class Deck:
    def __init__(self):
        self._cards = [Card(suit, rank) for suit in Card.suits for rank in Card.ranks]
        self.shuffle()

    def deal_one(self):
        card = random.choice(self._cards)
        self._cards.remove(card)
        return card

    def shuffle(self):
        random.shuffle(self._cards)

class Participant:
    def __init__(self):
        self._score = 0
        self._balance = 0
        self._hand = []

    @property
    def hand(self):
        return self._hand

    def update_hand(self, card):
        self.hand.append(card)

    def score_hand(self):
        score = 0
        aces_in_hand = 0
        for card in self.hand:
            if card.hidden:
                continue
            if card.value == 11:
                aces_in_hand += 1
            score += card.value
        if aces_in_hand:
            for _ in range(aces_in_hand):
                if score > self.TARGET_SCORE:
                    score -= 10
        return score

    def is_busted(self):
        return self.score_hand() > 21

    def show_hand(self):
        card_strings = [str(card) for card in self.hand]
        hand_display = Participant.join_and(card_strings)
        return hand_display

    def hit(self, deck: Deck):
        self.update_hand((deck.deal_one()))

    @staticmethod
    def join_and(num_list, separator=', ', final_connector='and'):
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
        full_string += 'and '
        full_string += str(num_list[-1])
        return full_string

class Dealer(Participant):
    def __init__(self):
        super().__init__()

    def deal_opening_cards(self, person: Participant, deck: Deck):
        person.update_hand((deck.deal_one()))
        self.update_hand((deck.deal_one()))
        person.update_hand((deck.deal_one()))
        hidden_card = deck.deal_one()
        hidden_card.hide()
        self.update_hand(hidden_card)

    def reveal_all_cards(self):
        for card in self.hand:
            card.reveal()

class Player(Participant):
    def __init__(self):
        super().__init__()

class TwentyOneGame:
    TARGET_SCORE = 21
    DEALER_HIT_ON = 17

    def __init__(self):
        self.deck = Deck()
        self.player = Player()
        self.dealer = Dealer()

    def play(self):
        self.display_welcome_message()
        while True:
            self.play_round()
            if not self.player_wants_to_continue():
                break
        self.display_goodbye_message()

    def play_round(self):
        self.deck = Deck()
        self.player.hand.clear()
        self.dealer.hand.clear()

        self.deal_opening_cards()
        self.show_cards()
        self.player_turn()

        if not self.player.is_busted():
            self.dealer_turn()

        self.display_result()

    def deal_opening_cards(self):
        self.dealer.deal_opening_cards(self.player, self.deck)

    def dealer_turn(self):
        self.dealer.reveal_all_cards()
        while self.dealer.score_hand() < self.DEALER_HIT_ON:
            self.dealer.hit(self.deck)
            print(f'Dealer hits ==> {self.dealer.hand[-1]}')
        print(f'Dealer has {self.dealer.score_hand()}')

    def display_goodbye_message(self):
        print("Thanks for playing Twenty One. Come back soon.")

    def display_result(self):
        player_total = self.player.score_hand()
        dealer_total = self.dealer.score_hand()

        print("\n" + "="*20)
        print(f"Player has: {self.player.show_hand()} ({player_total} points)")
        print(f"Dealer has: {self.dealer.show_hand()} ({dealer_total} points)")
        print("="*20)

        result = self._who_won()

        if result == 'player_busted':
            print("You busted! Dealer wins.")
        elif result == 'dealer_busted':
            print("Dealer busted! You win.")
        elif result == 'player':
            print("You win!")
        elif result == 'dealer':
            print("Dealer wins!")
        else:
            print("It's a tie!")
        print()

    def display_welcome_message(self):
        print("Hello. Welcome to Twenty One. Let's play.")

    def _who_won(self):
        player_score = self.player.score_hand()
        dealer_score = self.dealer.score_hand()

        if player_score > self.TARGET_SCORE:
            return 'player_busted'
        elif dealer_score > self.TARGET_SCORE:
            return 'dealer_busted'
        elif player_score > dealer_score:
            return 'player'
        elif dealer_score > player_score:
            return 'dealer'
        else:
            return 'tie'

    def player_turn(self):
        while True:
            print(f'Your total is: {self.player.score_hand()}')
            choice = input("Would you like to (h)it or (s)tay? ")
            if choice.lower() == 'h':
                self.player.hit(self.deck)
                print(f'==> {self.player.hand[-1]}')
                if self.player.score_hand() > self.TARGET_SCORE:
                    break
            elif choice.lower() == 's':
                break
            else:
                print("Sorry, that's not a valid choice.")

    def player_wants_to_continue(self):
        while True:
            choice = input('Want to play again? Yes or no?')
            if choice.lower() in ('y', 'yes', 'yeah', 'ye', 'yea'):
                return True
            elif choice.lower() in ('n', 'no', 'nope'):
                return False
            else:
                print("Sorry, that's not a valid choice.")

    def show_cards(self):
        print(f"Dealer's hand: {self.dealer.show_hand()}")
        print(f"Your cards: {self.player.show_hand()}")

game = TwentyOneGame()
game.play()
