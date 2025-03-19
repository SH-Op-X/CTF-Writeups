# Decompiled with PyLingual (https://pylingual.io)
# Internal filename: stone_game.py
# Bytecode version: 3.13.0rc3 (3571)
# Source timestamp: 1970-01-01 00:00:00 UTC (0)

import os
import time
import random
import sys
from game_logic import DigitalDisplayGame, MonteCarloAI
FLAG = open('FLAG').read()

class GameUI:
    def __init__(self, max_stones=10):
        self.max_stones = max_stones
        self.reset_game()

    def reset_game(self):
        """Reset the game for a new round"""  # inserted
        self.game = DigitalDisplayGame(self.max_stones)
        self.ai = MonteCarloAI(self.game, iterations=2000)
        self.game.current_player = 0

    def display_game(self):
        """Display the current game state"""  # inserted
        os.system('clear' if os.name == 'posix' else 'cls')
        print('\nDigital Display Game\n')
        print('\nCurrent stone count:')
        for i in range(7):
            print(f'Segment {i + 1}: {self.game.stones[i]} stones')
        print('\nCurrent player:', 'You' if self.game.current_player == 0 else None, 'AI')

    def get_player_move(self):
        """Get the player\'s move"""  # inserted
        pass
        try:
            print('\nEnter the number of stones to remove from each segment (space-separated, e.g.: 0 1 0 2 0 0 0):')
            move = list(map(int, input().split()))
            if len(move)!= 7:
                print('Input must be 7 numbers!')
                continue
            if self.game.is_valid_move(move):
                return move
            except ValueError:
                print('Please enter valid numbers!')

    def play_single_game(self):
        """Play a single round of the game"""  # inserted
        if not self.game.is_game_over():
            self.display_game()
            if self.game.current_player == 0:
                move = self.get_player_move()
                self.game.make_move(move)
        self.display_game()
        winner = self.game.get_winner()
        if winner == 0:
            print('\nYou won this round!')
        return True

def main():
    max_stones = 100
    total_rounds = 100
    win_threshold = 90
    print('Welcome to the Digital Display Game Challenge!')
    print('The player who cannot make a move loses.')
    print('You will always go first in each round.')
    print(f'You need to win at least {win_threshold} out of {total_rounds} rounds to get the flag.')
    print('Press Enter to start...')
    input()
    game = GameUI(max_stones)
    player_wins = 0
    for round_num in range(1, total_rounds + 1):
        print(f'\n=== Round {round_num}/{total_rounds} ===')
        print(f'Current score: {player_wins}/{round_num - 1}')
        game.reset_game()
        if game.play_single_game():
            player_wins += 1
        print(f'Score after round {round_num}: {player_wins}/{round_num}')
        if round_num < total_rounds:
            pass  # postinserted
        else:  # inserted
            print('Next round starting in 2 seconds...')
            time.sleep(2)
    print('\n=== Challenge Complete ===')
    print(f'Final score: {player_wins}/{total_rounds}')
    if player_wins >= win_threshold:
        print('\nCongratulations! You\'ve beaten the AI enough times to earn the flag:')
        print(FLAG)
    return None
if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('\nGame terminated by user.')
        sys.exit(0)