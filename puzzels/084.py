""" Monopoly odds

    Problem 84
    In the game, Monopoly, the standard board is set up in the following way:

        GO 	A1 	CC1 A2 	T1 	R1 	B1 	CH1 B2 	B3 	JAIL
        H2 	  	                                C1
        T2 	  	                                U1
        H1 	  	                                C2
        CH3 	  	                            C3
        R4 	  	                                R2
        G3 	  	                                D1
        CC3 	  	                            CC2
        G2 	  	                                D2
        G1 	  	                                D3
        G2J F3 	U2 	F2 	F1 	R3 	E3 	E2 	CH2 E1 	FP

    A player starts on the GO square and adds the scores on two 6-sided dice to determine the number of squares
    they advance in a clockwise direction. Without any further rules we would expect to visit each square with equal
    probability: 2.5%. However, landing on G2J (Go To Jail), CC (community chest), and CH (chance) changes this
    distribution.

    In addition to G2J, and one card from each of CC and CH, that orders the player to go directly to jail,
    if a player rolls three consecutive doubles, they do not advance the result of their 3rd roll. Instead they
    proceed directly to jail.

    At the beginning of the game, the CC and CH cards are shuffled. When a player lands on CC or CH they take a
    card from the top of the respective pile and, after following the instructions, it is returned to the bottom
    of the pile. There are sixteen cards in each pile, but for the purpose of this problem we are only concerned
    with cards that order a movement; any instruction not concerned with movement will be ignored and the player
    will remain on the CC/CH square.

        - Community Chest (2/16 cards):
            1. Advance to GO
            2. Go to JAIL
        - Chance (10/16 cards):
            1. Advance to GO
            2. Go to JAIL
            3. Go to C1
            4. Go to E3
            5. Go to H2
            6. Go to R1
            7. Go to next R (railway company)
            8. Go to next R
            9. Go to next U (utility company)
            10. Go back 3 squares.

    The heart of this problem concerns the likelihood of visiting a particular square. That is, the probability of
    finishing at that square after a roll. For this reason it should be clear that, with the exception of G2J for which
    the probability of finishing on it is zero, the CH squares will have the lowest probabilities, as 5/8 request a
    movement to another square, and it is the final square that the player finishes at on each roll that we are
    interested in. We shall make no distinction between "Just Visiting" and being sent to JAIL, and we shall also
    ignore the rule about requiring a double to "get out of jail", assuming that they pay to get out on their next turn.

    By starting at GO and numbering the squares sequentially from 00 to 39 we can concatenate these two-digit
    numbers to produce strings that correspond with sets of squares.

    Statistically it can be shown that the three most popular squares, in order, are JAIL (6.24%) = Square 10,
    E3 (3.18%) = Square 24, and GO (3.09%) = Square 00. So these three most popular squares can be listed with the
    six-digit modal string: 102400.

    If, instead of using two 6-sided dice, two 4-sided dice are used, find the six-digit modal string.
"""

from time import perf_counter
start = perf_counter()


global CC, CH, visit_places
import random


def get_new_position(position: int, dice1: int, dice2: int) -> int:
    global CC, CH
    n_bord_positions = 40
    new_position = (position + dice1 + dice2) % n_bord_positions

    # go to jail
    if new_position == 30:
        return 10

    # CH
    if new_position in [7, 22, 36]:

        # get card
        card = CH[0]
        CH = CH[1:] + [CH[0]]

        # stay put
        if card == -1:
            return new_position

        # go to next railroad
        if card == -2:
            if new_position < 5:
                return 5
            if new_position < 15:
                return 15
            if new_position < 25:
                return 25
            else:
                return 35

        # go to next utility
        if card == -3:
            if new_position < 12:
                return 12
            else:
                return 28

        # go three spots back
        if card == -4 and new_position != 36:
            return new_position - 3

        # if you are at 36 and get card to jump to CC (33)
        if card == -4 and new_position == 36:
            position -= 3
        else:
            return card

    # CC
    if new_position in [2, 17, 33]:

        # get card
        card = CC[0]
        CC = CC[1:] + [CC[0]]

        # stay put
        if card == -1:
            return new_position
        else:
            return card
    return new_position


def roll_n_dice(number_of_rolls: int, dice_sides: int) -> None:
    consecutive_doubles, position = 0, 0
    for m in range(number_of_rolls):

        # Roll dices
        dice1, dice2 = random.randint(1, dice_sides), random.randint(1, dice_sides)

        # keep track of times consecutive doubles
        if dice1 == dice2:
            consecutive_doubles += 1

            # go to jail OR visit new place
            if consecutive_doubles == 3:
                position = 10
                consecutive_doubles = 0
                visit_places[10] += 1
            else:
                position = get_new_position(position, dice1, dice2)

        # get new position and reset consecutive_doubles
        else:
            consecutive_doubles = 0
            position = get_new_position(position, dice1, dice2)
            visit_places[position] += 1

    answer = []
    for i in range(number_of_rolls):
        answer.append([visit_places[i] / number_of_rolls, i])
    answer.sort(key=lambda x: x[0], reverse=True)
    print(''.join([str(x[1]) for x in answer[:3]]))


def main():

    global visit_places, CC, CH

    n_rolls = 100000
    states, visit_places = list(range(n_rolls)), [0] * n_rolls

    CC = [0, 10] + [-1] * 14
    CH = [0, 10, 11, 24, 39, 5, -2, -2, -3, -4] + [-1] * 6

    roll_n_dice(n_rolls, 4)

    end = perf_counter()
    print(f"Runtime of the program is {end - start:.10f}")


if __name__ == "__main__":
    main()


# 101524
# Runtime of the program is 0.1513782000
