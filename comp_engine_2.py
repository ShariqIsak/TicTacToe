import random


def print_screen():
    print('\n')
    print(f"   {array[0]} | {array[1]} | {array[2]}")
    print("   ---------")
    print(f"   {array[3]} | {array[4]} | {array[5]}")
    print("   ---------")
    print(f"   {array[6]} | {array[7]} | {array[8]}")
    print('\n')


def opp_symbol(symbol):
    if symbol == 'X':
        return 'O'
    else:
        return 'X'


# Winning Combinations
win1 = [0, 1, 2]
win2 = [3, 4, 5]
win3 = [6, 7, 8]
win4 = [0, 3, 6]
win5 = [1, 4, 7]
win6 = [2, 5, 8]
win7 = [0, 4, 8]
win8 = [2, 4, 6]


def two_streak(symbol, array):
    # Returns an index position after iterating through win combinations else none
    # Win 1
    plays = []

    empty_slots = []
    count = 0
    for x in win1:
        if array[x] == symbol:
            count += 1
        if array[x] != symbol and array[x] != opp_symbol(symbol):
            empty_slots.append(x)
    if count == 2:
        plays.append(empty_slots)

    # Win 2
    empty_slots = []
    count = 0
    for x in win2:
        if array[x] == symbol:
            count += 1
        if array[x] != symbol and array[x] != opp_symbol(symbol):
            empty_slots.append(x)
    if count == 2:
        plays.append(empty_slots)

    # Win 3
    empty_slots = []
    count = 0
    for x in win3:
        if array[x] == symbol:
            count += 1
        if array[x] != symbol and array[x] != opp_symbol(symbol):
            empty_slots.append(x)
    if count == 2:
        plays.append(empty_slots)



    # Win 4
    empty_slots = []
    count = 0
    for x in win4:
        if array[x] == symbol:
            count += 1
        elif array[x] != symbol and array[x] != opp_symbol(symbol):
            empty_slots.append(x)
    if count == 2:
        plays.append(empty_slots)


    # Win 5
    empty_slots = []
    count = 0
    for x in win5:

        if array[x] == symbol:
            count += 1

        if array[x] != symbol and array[x] != opp_symbol(symbol):
            empty_slots.append(x)
    if count == 2:
        plays.append(empty_slots)


    # Win 6
    empty_slots = []
    count = 0
    for x in win6:
        if array[x] == symbol:
            count += 1
        if array[x] != symbol and array[x] != opp_symbol(symbol):
            empty_slots.append(x)
    if count == 2:
        plays.append(empty_slots)

    # Win 7
    empty_slots = []
    count = 0
    for x in win7:
        if array[x] == symbol:
            count += 1
        if array[x] != symbol and array[x] != opp_symbol(symbol):
            empty_slots.append(x)
    if count == 2:
        plays.append(empty_slots)

    # Win 8
    empty_slots = []
    count = 0
    for x in win8:
        if array[x] == symbol:
            count += 1
        if array[x] != symbol and array[x] != opp_symbol(symbol):
            empty_slots.append(x)
    if count == 2:
        plays.append(empty_slots)

    # BUG FIX: Checks special case when an empty list is added to plays
    if len(plays)==1 and plays[0]==[]:
        return None

    elif len(plays) != 0:
        plays = [ele for ele in plays if ele != []]
        try:
            move = random.choice(plays)
            return move.pop()
        except IndexError:
            return random_play(array)

    else:
        return None


# Returns a random playable index
def random_play(array):

    available = []
    for c in range(0, 9):
        print(c)
        if array[c] != 'X' and array[c] != 'O':
            available.append(c)

    print(available)
    if len(available) != 0:
        return random.choice(available)
    else:
        return None


def check_corners(array):
    #checks the corners of the table and return a random playable corner
    corners = [0,2,6,8]
    available = []
    for c in corners:
        if array[c] != 'X' and array[c] != 'O':
            available.append(c)

    if len(available) != 0:
        return random.choice(available)
    else:
        return None


def generate_play(comp_symbol, comp_started, array, comp_turn_number):
    print(f"Computer is: {comp_symbol} \nComputer started: {comp_started} \nComp Turn Number: {comp_turn_number}.")

    player_symbol = opp_symbol(comp_symbol)

    if comp_started:
        # first move = pos 0 always
        if comp_turn_number == 1:
            return 0
        # second move = check for either 3,7 or 9 whichever is empty
        if comp_turn_number == 2:
            if array[2] != player_symbol:
                return 2
            elif array[6] != player_symbol:
                return 6
            elif array[8] != player_symbol:
                return 9
        # third move  = check for wi
        if comp_turn_number == 3:
            if two_streak(comp_symbol, array) is not None:
                return two_streak(comp_symbol, array)
            else:
                return check_corners(array)
        if comp_turn_number > 3:
            return two_streak(comp_symbol, array)

    else:
        #if player started...
        if comp_turn_number == 1:
            return check_corners(array)
        if comp_turn_number == 2:
            if two_streak(player_symbol, array) is not None:
                return two_streak(player_symbol, array)
            else:
                return check_corners(array)
        if comp_turn_number >= 3:
            if two_streak(comp_symbol, array) is not None:
                return two_streak(comp_symbol, array)
            else:
                return two_streak(player_symbol, array)



# Testing Parameters
print('Comp Engine V2 - Dev')

array = ['O', 'X', 'O',
          4, 'O',  6,
         'X', 'O', 'X']

# DONE add these to main function
comp_symbol = 'X'
comp_started = False
comp_turn_number = 4

plays = 1

if all(type(x) is str for x in array):
    print('Draw')




for a in range(0, plays):
    print_screen()
    # DONE call in main
    next_move = generate_play(comp_symbol, comp_started, array, comp_turn_number)
    print(f'Next move is: {next_move}')
    comp_turn_number += 1
