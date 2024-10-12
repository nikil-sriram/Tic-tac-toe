print("Welcome to Tic Tac Toe")

turn = 1
letter = "x"
numbers_taken = []
playerx_turns = []
playery_turns = []
winner = False


board = [['','',''], ['','',''], ['','','']]
for i in board:
    print(i)

while not winner:
    for i in range(turn):
        if (turn % 2) == 0:
            player = "Player 2"
            letter = "y"
        else:
            player = "Player 1"
            letter = "x"
        turnplacementrow = int(input(f"{player} what row would you like to place your {letter}"))
        turnplacementcolumn = int(input(f"{player} what column would you like to place your {letter}"))

        while True:
            if board[turnplacementrow-1][turnplacementcolumn-1] != '':
                print("This has already been taken")
                turnplacementrow = int(input(f"{player} what row would you like to place your {letter}"))
                turnplacementcolumn = int(input(f"{player} what column would you like to place your {letter}"))
            else:
                break

        turn += 1

        if player == "Player 1":
            playerx_turns.append([turnplacementrow, turnplacementcolumn])
            print(playerx_turns)
        if player == "Player 2":
            playery_turns.append([turnplacementrow, turnplacementcolumn])

        board[turnplacementrow-1][turnplacementcolumn-1] = letter

        for i in board:
            print(i)

        for turnplacementrow in range(3): 
            if board[0] == board[1] == board[2] and board[0] != '':
                print(f"{player} has won the game!")
                winner = True
                break
        
        
        for col in range(3):
            if board[0][col] == board[1][col] == board[2][col] and board[0][col] != '':
                print(f"{player} has won the game!")
                winner = True
                break

        
        if (board[0][0] == board[1][1] == board[2][2] and board[0][0] != '') or \
           (board[0][2] == board[1][1] == board[2][0] and board[0][2] != ''):
            print(f"{player} has won the game!")
            winner = True
            break


    if winner:
        break