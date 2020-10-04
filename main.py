from game import Game
from utils.words_list import hangman_words_list

if __name__ == '__main__':
    player_name = input('''What's your name, hang-player? ''').title()
    Game(player_name, hangman_words_list).run_game()
