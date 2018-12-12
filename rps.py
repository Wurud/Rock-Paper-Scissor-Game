#!/usr/bin/env python3

import random
import sys

"""This program plays a game of Rock, Paper, Scissors between two Players,
and reports both Player's scores each round."""

moves = ['rock', 'paper', 'scissors']
hScore = 0
cScore = 0

"""The Player class is the parent class for all of the Players
in this game"""


class Player:
    def move(self):
        pass

    def learn(self, humanMove, computerMove):
        pass


class RepeatPlayer (Player):
    # The computer return rock always.
    def move(self):
        return 'rock'


class RandomPlayer (Player):
    # The computer return random move for each round.
    def move(self):
        result = random.choice(moves)
        return result


class RefelectPlayer (Player):
    # The computer plays randomly the first round,
    # and will imitate the human move for each round after
    def __init__(self):
        self.flag = 0

    def move(self):
        if self.flag == 0:
            result = random.choice(moves)
            self.flag += 1
            return result
        else:
            return self.computerMove

    def learn(self, humanMove, computerMove):
            if self.flag >= 1:
                self.humanMove = humanMove
                self.computerMove = computerMove
                self.flag += 1


class CyclePlayer (Player):
    # The computer will cycle through the moves list.
    def __init__(self):
        self.flag = 0

    def move(self):
        if self.flag == 0:
            result = moves[0]
            self.flag += 1

        elif self.flag == 1:
            result = moves[1]
            self.flag += 1

        elif self.flag == 2:
            result = moves[2]
            self.flag -= 2
        return result


class HumanPlayer (Player):
    def move(self):
        result = input("Rock, paper, scissors or quit the game?\n")
        return result


class Game:
    chosenStrategy = 0

    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
        chosenStrategy = 0

    def compare_inputs(self, humanMove, computerMove):

        global hScore
        global cScore

        if ((humanMove == 'rock' and computerMove == 'scissors') or
           (humanMove == 'scissors' and computerMove == 'paper') or
           (humanMove == 'paper' and computerMove == 'rock')):
                hScore += 1
                print(f"You played {humanMove}.")
                print(f"Opponent played {computerMove}.")
                print("** PLAYER ONE WINS **")
                print(f"Score: Player One {hScore},Player Two {cScore}")

        elif((computerMove == 'rock' and humanMove == 'scissors') or
             (computerMove == 'scissors' and humanMove == 'paper') or
             (computerMove == 'paper' and humanMove == 'rock')):
                cScore += 1
                print(f"You played {humanMove}.")
                print(f"Opponent played {computerMove}.")
                print("** PLAYER TWO WINS **")
                print(f"Score: Player One {hScore},Player Two {cScore}")

        elif (computerMove == humanMove):
                print(f"You played {humanMove}.")
                print(f"Opponent played {computerMove}.")
                print("** TIE **")
                print(f"Score: Player One {hScore},Player Two {cScore}")

        elif (humanMove == 'quit'):
                exit()

        else:
            print("Invalid input, try again ..")
            self.play_round()

    def play_round(self):
        move1 = self.p1.move()
        move2 = self.p2.move()
        print(f"Player 1: {move1}  Player 2: {move2}")
        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)
        self.compare_inputs(move1, move2)

    def play_game(self):
        try:
            numOfRounds = int(input("Number of rounds to play?"))
        except ValueError:
            print("Invalid input, try again ..")
            numOfRounds = int(input("The rounds number is:"))
        for round in range(int(numOfRounds)):
            print(f"Round {round} --")
            self.play_round()
        if hScore > cScore:
            print("Congratulations you won the game ^_^")
        elif hScore < cScore:
            print("Congratulations to me I won the game Hhahaha!!")
        else:
            print("No one won this game :(")
        print("__Game over!__")

    def start_game():
        if __name__ == '__main__':
            print("__GAME START__")
            try:
                Game.chosenStrategy = int(input("Opponent Strategy:\n" +
                                                " Random = 0\n Repeat = 1\n " +
                                                "Refelect = 2\n Cycle = 3\n " +
                                                "Your choice is: "))
            except ValueError:
                    print("Invalid input, try again ..")
                    chosenStrategy = int(input("The strategy number is:"))
            if Game.chosenStrategy == 0:
                game = Game(HumanPlayer(), RandomPlayer())
            elif Game.chosenStrategy == 1:
                game = Game(HumanPlayer(), RepeatPlayer())
            elif Game.chosenStrategy == 2:
                game = Game(HumanPlayer(), RefelectPlayer())
            elif Game.chosenStrategy == 3:
                game = Game(HumanPlayer(), CyclePlayer())
            game.play_game()


Game.start_game()
