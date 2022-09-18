#Variables
board = ["-", "-", "-",
         "-","-", "-",
         "-","-", "-"]
game_running = True
winner = None
current_player = "X"

#Print the board
def display_board(board):
    print(board[0], "|", board[1], "|", board[2])
    print("===========")
    print(board[3], "|", board[4], "|", board[5])
    print("===========")
    print(board[6], "|", board[7], "|", board[8])
    print()
    print()

#Take the input from the player(1-9)
def player_input(board):
    global game_running
    choice = int(input("Enter any number between 1-9: "))
    if (choice>=1 and choice<=9 and board[choice-1] == "-"):
        board[choice-1] = current_player
    else:
        print("Invaild Input. Program Terminated !")
        game_running = False
    
#Check win or tie
def check_hori(board):
    global winner
    if board[0]==board[1]==board[2] and board[0] != "-":
        winner = board[0]
        return True
    
    elif board[3]==board[4]==board[5] and board[3] != "-":
        winner = board[3]
        return True
    
    elif board[6]==board[7]==board[8] and board[6] != "-":
        winner = board[6]
        return True

def check_row(board):
    global winner
    if board[0]==board[3]==board[6] and board[0] != "-":
        winner = board[0]
        return True

    elif board[1]==board[4]==board[7] and board[1] != "-":
        winner = board[1]
        return True

    elif board[2]==board[5]==board[8] and board[2] != "-":
        winner = board[2]
        return True

def check_diag(board):
    global winner
    if board[0]==board[4]==board[8] and board[0] != "-":
        winner = board[0]
        return True

    elif board[2]==board[4]==board[6] and board[2] != "-":
        winner = board[2]
        return True

def check_tie(board):
    global game_running
    if "-" not in board:
        print("It's a Tie !")
        print("Program Terminated !")
        game_running = False

def check_win_master():
    global game_running
    if check_hori(board) or check_row(board) or check_diag(board):
        display_board(board)
        print(f"The winner is {winner}")
        game_running = False

        
#switch  player
def switch_player():
    global current_player
    if current_player == "X":
        current_player = "O"
    else:
        current_player = "X"
#Check win or tie again

#This is the main loop
print("First one to start is the 'X' Player.")
print("Second one is the 'O' Player.")

while game_running:
    display_board(board)
    player_input(board)
    check_win_master()
    check_tie(board)
    switch_player()

