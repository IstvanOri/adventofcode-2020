from collections import deque

from ac2020.days import AbstractDay


def game(deck1, deck2):
    hand1 = list(deck1)
    hand2 = list(deck2)

    log = set()

    while len(hand1) != 0 and len(hand2) != 0:
        hashed = ''.join(map(str, hand1)) + '|' + ''.join(map(str, hand2))
        if hashed in log:
            return hand1, []
        log.add(hashed)
        card1 = hand1.pop(0)
        card2 = hand2.pop(0)
        if len(hand1) >= card1 and len(hand2) >= card2:
            sub = game(list(hand1)[:card1], list(hand2)[:card2])
            if len(sub[0]) > 0:
                hand1.append(card1)
                hand1.append(card2)
            else:
                hand2.append(card2)
                hand2.append(card1)
        else:
            if card1 >= card2:
                hand1.append(card1)
                hand1.append(card2)
            else:
                hand2.append(card2)
                hand2.append(card1)
    return hand1, hand2


class Day22(AbstractDay.AbstractDay):

    def _set_input(self, input_: str):
        self.entries = {}
        self.player1 = []
        self.player2 = []
        if len(input_) != 0:
            split = input_.split('\n\n')
            self.player1 = list(map(int, (split[0].split('\n')[1:])))
            self.player2 = list(map(int, (split[1].split('\n')[1:])))

    def part1(self) -> str:
        hand1 = deque(self.player1)
        hand2 = deque(self.player2)
        while len(hand1) != 0 and len(hand2) != 0:
            card1 = hand1.popleft()
            card2 = hand2.popleft()
            if card1 > card2:
                hand1.append(card1)
                hand1.append(card2)
            else:
                hand2.append(card2)
                hand2.append(card1)

        winner_hand = list(hand2)
        if len(hand1) > 0:
            winner_hand = list(hand1)

        return str(sum([(i+1) * x for i, x in enumerate(winner_hand[::-1])]))

    def part2(self) -> str:
        hands = game(list(self.player1), list(self.player2))

        winner_hand = list(hands[1])
        if len(hands[0]) > 0:
            winner_hand = list(hands[0])

        return str(sum([(i + 1) * x for i, x in enumerate(winner_hand[::-1])]))
