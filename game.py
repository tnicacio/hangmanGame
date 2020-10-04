import random

from player import Player
from utils.drawings import draw_hangman


class Game:

    def __init__(self, player_name, words_list):
        self._player = Player(player_name, 6)
        self._words_list = words_list
        self._guessed_letters = []
        self._guessed_words = []
        self._word = self.choose_word()
        self._spaces = '-' * len(self._word)

    def run_game(self):
        self.new_round()
        while input("Do you want to play again? (Y/N) ").upper() == "Y":
            self.reset()
            self.new_round()

    def choose_word(self):
        return random.choice(self._words_list).upper()

    def new_round(self):
        print('''Let's Begin!''')
        if self._player.health == 0:
            self.reset()
        self.show_hangman_on_console()

        while not self._player.won and self._player.health > 0:
            guess = input("Please enter with a word or letter: ").upper()
            self.check_guess(guess)
            self.show_hangman_on_console()

        if self._player.won:
            print('Congratulations! You rock!')
        else:
            print(f'Oh, it happens. You cannot win everytime ;/ The word was {self._word}.\nTry again!')

    def check_guess(self, guess):
        if len(guess) == 1 and guess.isalpha():
            self.check_letters(guess)
        elif len(guess) == len(self._word) and guess.isalpha():
            self.check_word(guess)
        else:
            print('Wrong guess!')

    def check_letters(self, guess):
        if guess in self._guessed_letters:
            print('This letter has already been said')
        elif guess not in self._word:
            print(guess, ' does not belong to the word')
            self._player.health -= 1
            self._guessed_letters.append(guess)
        else:
            print("That' right!,", guess, " belongs to the word!")
            self._guessed_letters.append(guess)

            word_as_list = list(self._spaces)
            indexes = [i for i, letter in enumerate(self._word) if letter == guess]
            for index in indexes:
                word_as_list[index] = guess

            self._spaces = "".join(word_as_list)
            self._player.won = "-" not in self._spaces

    def check_word(self, guess):
        self._player.won = guess == self._word

        if self._player.won:
            self._spaces = self._word
        elif guess in self._guessed_words:
            print("You already made this guess")
        else:
            print(guess, " is not the right word!")
            self._player.health -= 1
            self._guessed_words.append(guess)

    def show_hangman_on_console(self):
        print(self._player)
        print(draw_hangman(self._player.health))
        print(self._spaces)
        print('\n')

    def reset(self):
        self._player.health = 6
        self._player.won = False
        self._guessed_letters = []
        self._guessed_words = []
        self._word = self.choose_word()
        self._spaces = '-' * len(self._word)
