import random

# Winning Combinations
win1 = [0, 1, 2]
win2 = [3, 4, 5]
win3 = [6, 7, 8]
win4 = [0, 3, 6]
win5 = [1, 4, 7]
win6 = [2, 5, 8]
win7 = [0, 4, 8]
win8 = [2, 4, 6]


def comp_choice(symbol, table_list):
    # TODO should be reset in the flip coin,
    # TODO +1 in main
    COMP_TURN = 2

    # TODO Can be gotten from flip coin
    comp_started = False

    current_state = table_list

    # 1. First play is always random
    if COMP_TURN == 1:
        print(' first turn')
        table_list = [ele for ele in table_list if ele != opp_symbol(symbol)]
        table_list = [ele for ele in table_list if ele != symbol]
        return table_list.pop(random.randint(0, len(table_list) - 1))
    # 2. if comp started
    elif comp_started and COMP_TURN == 2:
        # a. play next_best_move()
        return second_move(symbol, table_list)
    elif comp_started and COMP_TURN > 2:
        # b. if player has streak of 2 then block else next_best_move()
        return next_best_move(symbol(symbol), table_list)

    # 3. else if player started
    elif not comp_started:
        if COMP_TURN >= 2:
            # a. check if player has made streak of 2 then block else next_best_move()
            if next_best_move(opp_symbol(symbol), table_list) is not None:
                return next_best_move(opp_symbol(symbol), table_list)
            else:
                return second_move(symbol, table_list)


def opp_symbol(symbol):
    if symbol == 'X':
        return 'O'
    else:
        return 'X'


# Return a remaining slot of any streak of 2 by a player
def next_best_move(symbol, table_list):
    group_moves = []

    moves_list = []
    symbol_count = 0
    for a in win1:
        if str(table_list[a]) == symbol:
            symbol_count += 1
        if table_list[a] != symbol and table_list[a] != opp_symbol(symbol):
            moves_list.append(a)
        if symbol_count == 2:
            group_moves.append(moves_list)

    moves_list = []
    symbol_count = 0
    for a in win2:
        if str(table_list[a]) == symbol:
            symbol_count += 1
        if table_list[a] != symbol and table_list[a] != opp_symbol(symbol):
            moves_list.append(a)
        if symbol_count == 2:
            group_moves.append(moves_list)

    moves_list = []
    symbol_count = 0
    for a in win3:
        if str(table_list[a]) == symbol:
            symbol_count += 1
        if table_list[a] != symbol and table_list[a] != opp_symbol(symbol):
            moves_list.append(a)
        if symbol_count == 2:
            group_moves.append(moves_list)

    moves_list = []
    symbol_count = 0
    for a in win4:
        if str(table_list[a]) == symbol:
            symbol_count += 1
        if table_list[a] != symbol and table_list[a] != opp_symbol(symbol):
            moves_list.append(a)
        if symbol_count == 2:
            group_moves.append(moves_list)

    moves_list = []
    symbol_count = 0
    for a in win5:
        if str(table_list[a]) == symbol:
            symbol_count += 1
        if table_list[a] != symbol and table_list[a] != opp_symbol(symbol):
            moves_list.append(a)
        if symbol_count == 2:
            group_moves.append(moves_list)

    moves_list = []
    symbol_count = 0
    for a in win6:
        if str(table_list[a]) == symbol:
            symbol_count += 1
        if table_list[a] != symbol and table_list[a] != opp_symbol(symbol):
            moves_list.append(a)
        if symbol_count == 2:
            group_moves.append(moves_list)

    moves_list = []
    symbol_count = 0
    for a in win7:
        if str(table_list[a]) == symbol:
            symbol_count += 1
        if table_list[a] != symbol and table_list[a] != opp_symbol(symbol):
            moves_list.append(a)
        if symbol_count == 2:
            group_moves.append(moves_list)

    moves_list = []
    symbol_count = 0
    for a in win8:
        if str(table_list[a]) == symbol:
            symbol_count += 1
        if table_list[a] != symbol and table_list[a] != opp_symbol(symbol):
            moves_list.append(a)
        if symbol_count == 2:
            group_moves.append(moves_list)

    print(group_moves)
    if len(group_moves) > 0:
        random_moves = group_moves.pop(random.randint(0, len(group_moves) - 1))
        random_moves = [ele for ele in random_moves if ele != []]
        print(random_moves)
        print('returning to main function')
        if len(random_moves) is not None:
            return random_moves.pop()
        else:
            return None
    else:
        return None


# Second move check any wining line with 2 empty slots
def second_move(symbol, table_list):
    group_moves = []

    moves_list = []
    symbol_count = 0
    valid_line = False
    for a in win1:
        if table_list[a] == symbol:
            valid_line = True
        if table_list[a] != symbol and table_list[a] != opp_symbol(symbol):
            symbol_count += 1
            moves_list.append(a)
        if symbol_count == 2 and valid_line:
            group_moves.append(moves_list)

    moves_list = []
    symbol_count = 0
    valid_line = False
    for a in win2:
        if table_list[a] == symbol:
            valid_line = True
        if table_list[a] != symbol and table_list[a] != opp_symbol(symbol):
            symbol_count += 1
            moves_list.append(a)
        if symbol_count == 2 and valid_line:
            group_moves.append(moves_list)

    moves_list = []
    symbol_count = 0
    valid_line = False
    for a in win3:
        if table_list[a] == symbol:
            valid_line = True
        if table_list[a] != symbol and table_list[a] != opp_symbol(symbol):
            symbol_count += 1
            moves_list.append(a)
        if symbol_count == 2 and valid_line:
            group_moves.append(moves_list)

    moves_list = []
    symbol_count = 0
    valid_line = False
    for a in win4:
        if table_list[a] == symbol:
            valid_line = True
        if table_list[a] != symbol and table_list[a] != opp_symbol(symbol):
            symbol_count += 1
            moves_list.append(a)
        if symbol_count == 2 and valid_line:
            group_moves.append(moves_list)

    moves_list = []
    symbol_count = 0
    valid_line = False
    for a in win5:
        if table_list[a] == symbol:
            valid_line = True
        if table_list[a] != symbol and table_list[a] != opp_symbol(symbol):
            symbol_count += 1
            moves_list.append(a)
        if symbol_count == 2 and valid_line:
            group_moves.append(moves_list)

    moves_list = []
    symbol_count = 0
    valid_line = False
    for a in win6:
        if table_list[a] == symbol:
            valid_line = True
        if table_list[a] != symbol and table_list[a] != opp_symbol(symbol):
            symbol_count += 1
            moves_list.append(a)
        if symbol_count == 2 and valid_line:
            group_moves.append(moves_list)

    moves_list = []
    symbol_count = 0
    valid_line = False
    for a in win7:
        if table_list[a] == symbol:
            valid_line = True
        if table_list[a] != symbol and table_list[a] != opp_symbol(symbol):
            symbol_count += 1
            moves_list.append(a)
        if symbol_count == 2 and valid_line:
            group_moves.append(moves_list)

    moves_list = []
    symbol_count = 0
    valid_line = False
    for a in win8:
        if table_list[a] == symbol:
            valid_line = True
        if table_list[a] != symbol and table_list[a] != opp_symbol(symbol):
            symbol_count += 1
            moves_list.append(a)
        if symbol_count == 2 and valid_line:
            group_moves.append(moves_list)

    if len(group_moves) > 0:
        random_moves = group_moves.pop(random.randint(0, len(group_moves) - 1))
        return random_moves.pop(random.randint(0, len(random_moves) - 1))
    else:
        return None


array = ['O','X','X',
          4 ,'O', 6 ,
          7 , 8, 'X']

comp_symbol = 'O'

# if next_best_move(comp_symbol, array) is not None:
#     print(next_best_move('O', array))
# else:
#     print("play random number")
#
# if second_move(comp_symbol, array) is not None:
#     print(second_move('O', array))
# else:
#     print("no 2 free slots available")

print(comp_choice(comp_symbol, array))
