# Created By: EH

def check_corners(board):

    if board[0][0] == board[1][1] and board[1][1] == board[2][2] and board[0][0] != " ":
        return True
    elif board[0][2] == board[1][1] and board[1][1] == board[2][0] and board[0][2] != " ":
        return True
    else:
        return False


def check_vertical(board):

    if board[0][0] == board[1][0] and board[1][0] == board[2][0] and board[0][0] != " ":
        return True
    elif board[0][1] == board[1][1] and board[1][1] == board[2][1] and board[0][1] != " ":
        return True
    elif board[0][2] == board[1][2] and board[1][2] == board[2][2] and board[0][2] != " ":
        return True
    else:
        return False


def check_horizontal(board):

    if board[0][0] == board[0][1] and board[0][1] == board[0][2] and board[0][0] != " ":
        return True
    
    elif board[1][0] == board[1][1] and board[1][1] == board[1][2] and board[1][0] != " ":
        return True

    elif board[2][0] == board[2][1] and board[2][1] == board[2][2] and board[2][0]!= " ":
        return True
    else:
        return False

def check_full(board):
    for x in range(3):
        for i in range(3):
            if board[x][i] == " ":
                return False
    
    return True


def display(board):

    display_board = """ 
      {0}  | {1}  | {2}  
    ------------------
      {3}  | {4}  | {5} 
    ------------------
      {6}  | {7}  | {8}
    """.format(board[0][0], board[0][1], board[0][2], board[1][0],
    board[1][1], board[1][2], board[2][0], board[2][1], board[2][2])

    return display_board

if __name__ == "__main__":
    inputs = {
        "a1":[0,0], "a2":[0,1], "a3":[0,2],
        "b1":[1,0], "b2":[1,1], "b3":[1,2],
        "c1":[2,0], "c2":[2,1], "c3":[2,2]
    }

    board = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
    turn = 0

    print("moves: a1,a2,a3, b1,b2,b3, c1,c2,c3")

    while True:
        if turn == 0:
            user_input = input("Player 1: ")
            turn += 1
        else:
            user_input = input("Player 2: ")
            turn = 0
        
        try:
            if turn == 1:
                if board[inputs[user_input][0]][inputs[user_input][1]] not in "XO":
                    board[inputs[user_input][0]][inputs[user_input][1]] = "X"
                else:
                    print("That Place is Already Taken")
            else:
                if board[inputs[user_input][0]][inputs[user_input][1]] not in "XO":
                    board[inputs[user_input][0]][inputs[user_input][1]] = "O"
                else:
                    print("That Place Is Already Taken")
        except KeyError:
            print("That's not a valid option")

        print(display(board))
        
        if check_horizontal(board):
            if turn == 1:
                print("Winner: Player 1")
                break
            else:
                print("Winner: Player 2")
                break
        elif check_vertical(board):
            if turn == 1:
                print("Winner: Player 1")
                break
            else:
                print("Winner: Player 2")
                break
        
        elif check_corners(board):
            if turn == 1:
                print("Winner: Player 1")
                break
            else:
                print("Winner: Player 2")
                break
        

        if check_full(board):
            print("Game ended in a draw.")
            break
