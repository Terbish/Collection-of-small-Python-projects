from os import O_APPEND, P_DETACH
import random


def play():
    user = input("\nPick 'r' for rock, 'p' for paper, 's' for scissors: ")
    computer = random.choice(['r', 's', 'p'])

    if user == computer:
        return '\ntie'

    if p_win(user, computer):
        return '\nYou won!'

    return '\nYou lost'


def p_win(player, opponent):
    if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p')\
            or (player == 'p' and opponent == 'r'):
        return True


print(play())
