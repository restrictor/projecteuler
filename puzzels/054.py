""" Poker hands

    Problem 54
    In the card game poker, a hand consists of five cards and are ranked, from lowest to highest, in the following way:

        High Card: Highest value card.
        One Pair: Two cards of the same value.
        Two Pairs: Two different pairs.
        Three of a Kind: Three cards of the same value.
        Straight: All cards are consecutive values.
        Flush: All cards of the same suit.
        Full House: Three of a kind and a pair.
        Four of a Kind: Four cards of the same value.
        Straight Flush: All cards are consecutive values of same suit.
        Royal Flush: Ten, Jack, Queen, King, Ace, in same suit.

    The cards are valued in the order:
    2, 3, 4, 5, 6, 7, 8, 9, 10, Jack, Queen, King, Ace.

    If two players have the same ranked hands then the rank made up of the highest value wins;
    for example, a pair of eights beats a pair of fives (see example 1 below).
    But if two ranks tie, for example, both players have a pair of queens, then highest cards in each
    hand are compared (see example 4 below); if the highest cards tie then the next highest cards
    are compared, and so on.

    Consider the following five hands dealt to two players:

    Hand	 	    Player 1	 	    Player 2	 	        Winner
    1	 	        5H 5C 6S 7S KD      2C 3S 8S 8D TD
                    Pair of Fives       Pair of Eights          Player 2

    2	 	        5D 8C 9S JS AC      2C 5C 7D 8S QH
                    Highest card Ace    Highest card Queen 	    Player 1

    3	 	        2D 9C AS AH AC      3D 6D 7D TD QD
                    Three Aces          Flush with Diamonds     Player 2

    4	 	        4D 6S 9H QH QC      3D 6D 7H QD QS
                    Pair of Queens      Pair of Queens
                    Highest card Nine   Highest card Seven      Player 1

    5	 	        2H 2D 4C 4D 4S      3C 3D 3S 9S 9D
                    Full House          Full House
                    With Three Fours    with Three Threes       Player 1

    The file, poker.txt, contains one-thousand random hands dealt to two players. Each line of the file
    contains ten cards (separated by a single space): the first five are Player 1's cards and the last
    five are Player 2's cards. You can assume that all hands are valid (no invalid characters or repeated cards),
    each player's hand is in no specific order, and in each hand there is a clear winner.

    How many hands does Player 1 win?
"""

from time import perf_counter
start = perf_counter()

from itertools import combinations


class PlayGames:

    def __init__(self, print_hands: bool = False):
        self.hands = []
        with open('../data/054.txt', 'r') as f:
            players_hands = f.read().splitlines()
            for two_hands in players_hands:
                self.hands.append(sorted(self.replace_hand(two_hands.split(" ")[0:5])))
                self.hands.append(sorted(self.replace_hand(two_hands.split(" ")[5:])))
        self.cards = ["2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E"]
        self.print_hands = print_hands
        self.score_cards = dict(zip(self.cards, range(1, len(self.cards) + 1)))

    @staticmethod
    def replace(card: str) -> str:
        if card[0] == "T":
            return "A" + card[1]
        if card[0] == "J":
            return "B" + card[1]
        if card[0] == "Q":
            return "C" + card[1]
        if card[0] == "K":
            return "D" + card[1]
        if card[0] == "A":
            return "E" + card[1]
        else:
            return card

    def replace_hand(self, hand: list[str]) -> list[str]:
        return [self.replace(card) for card in hand]

    def points(self, hand) -> (int, list[str], list[str]):

        #     High Card: Highest value card.                (1-13 point)
        highest_card, candidate, solution = 0, "", []
        for card in hand:
            if self.score_cards[card[0]] > highest_card:
                highest_card, candidate, solution = self.score_cards[card[0]], card, card
        score, remainder = highest_card, list(set(hand) - set(candidate))

        #     One Pair: Two cards of the same value.        (14-26 point)
        sol_temp, p_options, pair_score, two_pair_score = [], list(combinations(hand, 2)), 0, 0
        for pair in p_options:
            if pair[0][0] == pair[1][0]:
                score, solution, remainder = 13 + self.score_cards[pair[0][0]], [pair], list(set(hand))
                pair_score, candidate = score, pair

                #      Two Pairs: Two different pairs.              (27-40 point)
                s_p_options, two_pair_score = list(combinations(list(set(hand) - set(candidate)), 2)), 0
                for p2 in s_p_options:
                    if p2[0][0] == p2[1][0]:
                        two_pair_score, candidate, solution = 26 + self.score_cards[pair[0][0]], p2, solution + [p2]
                        score, remainder = two_pair_score, list(set(list(set(hand) - set(candidate))) - set(solution))
                break

        #     Three of a Kind: Three cards of the same value.   (41-54 points)
        three_of_a_kind_bool, three_of_a_kind = False, []
        for three in list(combinations(hand, 3)):
            if three[0][0] == three[1][0] and three[1][0] == three[2][0]:
                score, remainder, solution = 40 + self.score_cards[three[0][0]], list(set(hand) - set(three)), [three]
                three_of_a_kind, three_of_a_kind_bool = [three[0]] + [three[1]] + [three[2]], True
                break

        #     Straight: All cards are consecutive values.       (45-58 points)
        straight = sorted([self.score_cards[card[0]] for card in hand])
        s_bool = all([straight[i + 1] - straight[i] == 1 for i in [0, 1, 2, 3]])
        if s_bool:
            score, remainder, solution = 58 + self.score_cards[hand[4][0]], [], hand

        #     Flush: All cards of the same suit.    (59-72)
        suit = len(set([card[1] for card in hand])) == 1
        if suit:
            score, solution = 59 + self.score_cards[hand[0][0]], hand

        #     Full House: Three of a kind and a pair.   (points 73-86)
        if pair_score and two_pair_score:
            if three_of_a_kind_bool:
                score, solution = 72 + self.score_cards[three_of_a_kind[0][0]], hand

        #     Four of a Kind: Four cards of the same value. (points 87-100)
        four = [self.score_cards[card[0]] for card in hand]
        if len(set(four)) == 2:
            score, solution, remainder = 86 + self.score_cards[three_of_a_kind[0][0]], four, list(set(hand) - set(four))

        #     Straight Flush: All cards are consecutive values of same suit. (points 101-114)
        straight_flush = False
        if suit and s_bool:
            score, straight_flush, solution = 101 + self.score_cards[hand[0][0]], True, hand

        #     Royal Flush: Ten, Jack, Queen, King, Ace, in same suit. (points 127-140)
        if straight_flush and self.score_cards[hand[0][0]] == 13:
            score, solution = 127 + self.score_cards[hand[0][0]], hand

        return score, remainder, solution

    def game_on(self) -> None:
        wins_for_for_player_1 = 0
        for two_hands in range(0, len(self.hands), 2):
            if self.print_hands:
                print("hand ", int((two_hands + 2) / 2))
                print("player 1", self.hands[two_hands], self.points(self.hands[two_hands]))
                print("player 2", self.hands[two_hands + 1], self.points(self.hands[two_hands + 1]))
            score1, remainder1, sol1 = self.points(self.hands[two_hands])
            score2, remainder2, sol2 = self.points(self.hands[two_hands + 1])
            winner = 0
            if score1 > score2:
                winner = 1
            if score1 < score2:
                winner = 2
            if winner == 0:
                if len(sol1[0]) == 2:
                    r1, r2 = sorted(remainder1), sorted(remainder2)
                    for x, y in zip(r1[::-1], r2[::-1]):
                        if self.score_cards[x[0]] > self.score_cards[y[0]]:
                            winner = 1
                            break
                        if self.score_cards[x[0]] < self.score_cards[y[0]]:
                            winner = 2
                            break
            if self.print_hands:
                print("winner ", winner, '\n')
            if winner == 1:
                wins_for_for_player_1 += 1
        print(wins_for_for_player_1)


a = PlayGames(print_hands=False)
a.game_on()

end = perf_counter()
print(f"Runtime of the program is {end - start:.10f}")

# 376
# Runtime of the program is 0.0350799000
