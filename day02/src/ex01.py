from collections import Counter
from typing import List, Tuple
from itertools import combinations


class Player:

    def __init__(self):
        # False - cheating, True - communicate
        self.action_history: List[bool] = []

    def action(self, history: List[bool]):
        pass

    def add_action_history(self, action: bool):
        self.action_history.append(action)


class Cheater(Player):

    def __str__(self):
        return "cheater"

    def action(self, history: List[bool]):
        return False


class Cooperator(Player):

    def __str__(self):
        return "cooperator"

    def action(self, history: List[bool]):
        return True


class Copycat(Player):

    def __str__(self):
        return "copycat"

    def action(self, history: List[bool]):
        if len(history) == 0:
            return True
        else:
            return history[-1]


class Grudger(Player):

    def __str__(self):
        return "grudger"

    def action(self, history: List[bool]):
        if history.count(False) == 0:
            return True
        else:
            return False


class Detective(Player):

    def __init__(self):
        super().__init__()
        self.detective_mode: bool = True
        self.copycat_mode: bool = False
        self.cheater_mode: bool = False
        self.detective_history: List[bool] = []

    def __str__(self) -> str:
        return "detective"

    def action(self, history: List[bool]) -> bool:
        if self.detective_mode:
            count = len(self.detective_history)
            if count in [0, 2, 3]:
                if count == 3:
                    self.detective_mode = False
                    if history.count(False):
                        self.copycat_mode = True
                    else:
                        self.cheater_mode = True
                self.detective_history.append(True)
                return True
            else:
                self.detective_history.append(False)
                return False
        elif self.cheater_mode:
            return Cheater.action(Cheater(), history)
        else:
            return Copycat.action(Copycat(), history)


class Game(object):

    def __init__(self, matches=10):
        self.matches = matches
        self.registry = Counter()

    def play(self, player1, player2):
        for _ in range(self.matches):
            player1_action = player1.action(player2.action_history)
            player2_action = player2.action(player1.action_history)

            if player1_action and player2_action:
                self.registry[str(player1)] += 2
                self.registry[str(player2)] += 2
            elif player1_action ^ player2_action:
                if player1_action:
                    self.registry[str(player1)] -= 1
                    self.registry[str(player2)] += 3
                else:
                    self.registry[str(player1)] += 3
                    self.registry[str(player2)] -= 1

            player1.action_history.append(player1_action)
            player2.action_history.append(player2_action)

    def top3(self):
        top = self.registry.most_common(3)
        for name, score in top:
            print(name, score)


def generate_players_pair() -> Tuple[Player, Player]:
    players = [Cheater, Cooperator, Copycat, Grudger, Detective]
    pairs: list[(Player, Player)] = combinations(players, 2)
    for pl1, pl2 in pairs:
        yield pl1(), pl2()


def test():
    game = Game()
    for player_1, player_2 in generate_players_pair():
        game.play(player_1, player_2)
    game.top3()


if __name__ == '__main__':
    test()
