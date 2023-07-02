import random
'''function for displaying the borad'''
def board_display(board):
    print('   |   |')
    print(' '+board[1]+' | '+board[2]+' |'+board[3])
    print('   |   |')
    print('------------')
    print('   |   |')
    print(' '+board[4]+' | '+board[5]+' |'+board[6])
    print('   |   |')
    print('------------')
    print('   |   |')
    print(' '+board[7]+' | '+board[8]+' |'+board[9])
    print('   |   |')


''' board = ['#', 'X', 'O', 'X', 'X', 'X', 'X', 'O', 'X', 'O']

board_display(board) '''

'''function for getting mark of the player'''
def player_mark():
    mark = ' '
    while not(mark=='X' or mark =='O'):
        mark = input('Choose a Mark : X OR O ?').upper()
    if mark == 'X':
        return('X','O')
    else:
        return('O','X')


'''function to place the marker on the board'''
def place_marker(board,mark,position):
    board[position]=mark

'''function to check whether someone has won'''
def check_win(board,mark):
    return( (board[1] == board[2] == board[3] == mark) or
            (board[4] == board[5] == board[6] == mark) or
            (board[7] == board[8] == board[9] == mark) or
            (board[7] == board[4] == board[1] == mark) or
            (board[8] == board[5] == board[2] == mark) or
            (board[9] == board[6] == board[3] == mark) or
            (board[1] == board[5] == board[9] == mark) or
            (board[3] == board[5] == board[7] == mark) )

'''function to choose player to play first'''
def choose_player():
    if random.randint(0,1) == 0:
        return 'PLAYER 1'
    else:
        return 'PLAYER 2'

'''fucntion to check space in the board, return True when there's space in the board, else returns False'''
def check_space(board,position):
    return board[position]== ' '

'''function to check whether the board is full, returns True when the board is full, else returns False
if check_space(board,i) indicates the function output True so if True return False i.e the there's space else return True i.e the board is full'''
def check_board_full(board):
    for i in range(1,10):
        if check_space(board,i):
            return False
    return True

'''function to get position from players'''
def get_position(board):
    position = 0
    while position not in [1,2,3,4,5,6,7,8,9] or not check_space(board,position):
        position = int(input('Enter a position - [1-9]: '))
    return position

'''function for replay '''
def replay():
    return input('Do you want to play again? Enter Yes or No: ').lower().startswith('y')

'''final Main function'''
print('TIC-TAC-TOE')

while True:
    #reset the board
    new_board = [' ']*10
    player_1_mark,player_2_mark = player_mark()
    turn = choose_player()
    print(turn+' WILL GO FIRST')
    game_play = input('Are you ready to start the game? Yes or No: ')
    if game_play.lower().startswith('y'):
        game = True
    else:
        game = False
    
    while game:
        if turn == 'PLAYER 1':
            board_display(new_board)
            position = get_position(new_board)
            place_marker(new_board,player_1_mark,position)
            if check_win(new_board,player_1_mark):
                board_display(new_board)
                print("CONGRATULATIONS! Player 1 has won the game!")
                game=False
            else:
                if check_board_full(new_board):
                    board_display(new_board)
                    print('The match is a DRAW!')
                    break
                else:
                    turn = 'PLAYER 2'
        else:
            #PLAYER 2'S TURN
            board_display(new_board)
            position = get_position(new_board)
            place_marker(new_board,player_2_mark,position)
            if check_win(new_board,player_2_mark):
                board_display(new_board)
                print("CONGRATULATIONS! Player 2 has won the game!")
                game = False
            else:
                if check_board_full(new_board):
                    board_display(new_board)
                    print('The match is a DRAW!')
                    break
                else:
                    turn = 'PLAYER 1'
    
    if not replay():
        break

