
def draw_board(board):
    print(" " + board[0] + " | " + board[1] + " | " + board[2] + " ")
    print("---+---+---")
    print(" " + board[3] + " | " + board[4] + " | " + board[5] + " ")
    print("---+---+---")
    print(" " + board[6] + " | " + board[7] + " | " + board[8] + " ")

def get_player_move(board):
    # get a number from 1 to 9 for the board position
    move = input("Enter your move (position 1-9): ")
    imove = int(move)
    if can_make_move(board, imove - 1):
        return imove - 1
    else:
        print("Sorry, that's not a valid move. Please try again.")
        return get_player_move(board)

def get_board_copy(board):
    new_board = list(board)
    return new_board

def can_make_move(board, move):
    if move in range(0,9):
        if " " == board[move]:
            return True
    return False

def get_computer_move(board):
    # first priority, can I win?
    for m in range(0,9):
        copy_board = get_board_copy(board)
        if can_make_move(copy_board, m):
            make_move(copy_board, m, "O")
            if has_someone_won(copy_board):
                return m

    # second priority, block a win?    
    for m in range(0,9):
        copy_board = get_board_copy(board)
        if can_make_move(copy_board, m):
            make_move(copy_board, m, "X")
            if has_someone_won(copy_board):
                return m

    # third priority, take the middle
    if can_make_move(board, 4):
        return 4

    # fourth priority, take a corner
    for m in [0, 2, 6, 8]:
        if can_make_move(board, m):
            return m

    # fifth priority, take a side
    for m in [1, 3, 5, 7]:
        if can_make_move(board, m):
            return m

def make_move(board, move, piece):
    board[move] = piece

def has_someone_won(board):
    winner = False
    if (board[0] != " " and board[0] == board[1] == board[2]) or \
        (board[3] != " " and board[3] == board[4] == board[5]) or \
        (board[6] != " " and board[6] == board[7] == board[8]) or \
        (board[0] != " " and board[0] == board[3] == board[6]) or \
        (board[1] != " " and board[1] == board[4] == board[7]) or \
        (board[2] != " " and board[2] == board[5] == board[8]) or \
        (board[0] != " " and board[0] == board[4] == board[8]) or \
        (board[2] != " " and board[2] == board[4] == board[6]):
        winner = True
    return winner

def is_it_a_draw(board):
    if len("".join(board).replace(" ", "")) == 9:
        return True
    else:
        return False

print("Welcome to Noughts and Crosses")
board = [" "] * 9
while True:
    draw_board(board)
    move = get_player_move(board)
    make_move(board, move, "X")
    if has_someone_won(board):
        draw_board(board)
        print("We have a winner! Well done you!")
        break
    elif is_it_a_draw(board):
        print("Fought to a draw...")
        break

    move = get_computer_move(board)
    make_move(board, move, "O")
    if has_someone_won(board):
        draw_board(board)
        print("We have a winner! But it wasn't you!")
        break
    elif is_it_a_draw(board):
        print("Fought to a draw...")
        break
