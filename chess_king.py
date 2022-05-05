def check_for_attacking_queens(queens_pos, king_pos, affection: list, current_direction_of_king):
    # Initializing x as king_pos[0], and y as king_pos[1]
    # -> [2, 1] -> x = 2, y = 1
    x, y = king_pos[0], king_pos[1]
    # Using while loop to iterate inside the chessboard (i.e. moving the king to it's 8 moves)
    # from it's position to the up, down and diagonally:
    while 0 <= x < 9 and 0 <= y < 9:
        # if the coordinate is equal to a queen's coordinate, adding it to the list, then return
        if [x, y] in queens_pos:
            affection.append([x, y])
            return
        # after that increasing the x, y with the coordinates given in
        # directions and checking again...
        x += current_direction_of_king[0]
        y += current_direction_of_king[1]


chess_board_size = 8
chess_board = []
king_row, king_col = 0, 0
queens = []
king_position = []
queen_positions = []
king_affection_count = 0
attacking_queens = []
directions = [[1, 0], [0, 1], [-1, 0], [0, -1], [-1, -1], [1, 1], [1, -1], [-1, 1]]  # direction mapping...
# These directions above are the eight moves of the king on a chessboard...


# The first, we're obtaining the positions of the king and the queens
# and storing them on variables:
for row in range(chess_board_size):
    elements = input().split()
    chess_board.append(elements)

    for col in range(chess_board_size):
        element = elements[col]
        if element == "K":
            king_row, king_col = row, col  # (2, 1)
            king_position.append([king_row, king_col])

        if element == "Q":
            queen_row, queen_col = row, col
            queen_positions.append([queen_row, queen_col])

# Then preparing the coordinates of the king for mapping use...
king_position = sum(king_position, [])  # [2, 1]

# Iterating over the directions:
for direction in directions:
    # Checking for each direction, move of the king, is it equal to a queen's coordinates
    # Defining a function for this purpose, which takes queens positions, king_position,
    # current direction and an empty list for collecting the attacking queens:
    check_for_attacking_queens(queen_positions, king_position, attacking_queens, direction)

if not attacking_queens:  # If we don't have attacking queens:
    print('The king is safe!')
else:  # If we have, printing their coordinates each on a new line:
    print(*attacking_queens, sep="\n")

# last_vertical_q_row = 0
# last_vertical_q_col = 0
# for q in queen_positions:
#     queen_row = q[0]
#     queen_col = q[1]
#     for k in king_position:
#         king_row = k[0]
#         king_col = k[1]
#         if queen_row == king_row:  # horizontal affection
#             king_affection_count += 1
#             print(f"King affected horizontally by queen in position: {queen_row, queen_col}")
#
#         elif queen_col == king_col:  # vertical affection
#             pass
#
#
#         elif abs(queen_row - king_row) == abs(queen_col - king_col):  # diagonal affection
#             king_affection_count += 1
#             print(f"King affected diagonally by queen in position: {queen_row, queen_col}")

# (x+1, y): one step horizontal move to the right.
# (x-1, y): one step horizontal move to the left.
# (x+1, y+1): one step diagonal move up-right.
# (x-1, y-1): one step diagonal move down-left.
# (x-1, y+1): one step diagonal move left-up.
# (x+1, y-1): one step diagonal move right-down.
# (x, y+1): one step downward.
# (x, y-1): one step upward.


test = '''. . . . . . . .
Q . . . . . . .
. K . . . Q . .
. . . Q . . . .
Q . . . Q . . .
. Q . . . . . .
. . . . . . Q .
. Q . Q . . . .
'''

test2 = '''. . . . . . . .
. . . Q . . . .
. . . . . . . .
. . . . . . . .
Q . . . Q . . .
. . K . . . . .
. . . . . . Q .
. . . Q . . . .
'''