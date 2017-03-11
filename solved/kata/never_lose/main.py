"""
How much do you win if you never lose a bet?

How to detect if someone is winning all the
bets so you can throw them out of the casino?
"""
import random


# Level 1
def run():
    start = 100
    bet = 10
    odds = 4  # to 1

    total = start
    for i in range(1, 10):
        total += bet * odds
        print(total)


run()


def fair_player(bet, odds):
    dice = random.random(0, odds)
    if dice == 0:
        return bet * odds
    else:
        return 0

def cheater(bet, odds):
    dice = random.random(0, odds)
    if dice == 0:
        return bet * odds
    else:
        return 0

# level 3- game
def generate_players():
    yield fair
    yield cheater

def casino():
    players = [x for x in generate_players()]

    while True:
        print("Player 1 ")
        print("Throw out player 1, 2 or to throw out now one, type 0.")
        x = input()

