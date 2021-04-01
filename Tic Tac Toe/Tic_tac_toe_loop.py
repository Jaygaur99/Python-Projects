board = {
    'T1': ' ', 'T2': ' ', 'T3': ' ',
    'M1': ' ', 'M2': ' ', 'M3': ' ',
    'B1': ' ', 'B2': ' ', 'B3': ' ',
}
player = 1
total_moves = 0
end_check = 0
print("T1 | T2 | T3".center(50))
print("---+----+---".center(50))
print("M1 | M2 | M3".center(50))
print("---+----+---".center(50))
print("B1 | B2 | B3".center(50))
print()
print("*************".center(50))
print()

while True:
    print((board['T1'] + ' | ' + board['T2'] + ' | ' + board['T3']).center(50))
    print(('--+---+--').center(50))
    print((board['M1'] + ' | ' + board['M2'] + ' | ' + board['M3']).center(50))
    print(('--+---+--').center(50))
    print((board['B1'] + ' | ' + board['B2'] + ' | ' + board['B3']).center(50))
    # condition_check
    if ((board['T1'] == 'X' and board['T2'] == 'X' and board['T3'] == 'X') or
    (board['B1'] == 'X' and board['B2'] == 'X' and board['B3'] == 'X') or 
    (board['M1'] == 'X' and board['M2'] == 'X' and board['M3'] == 'X') or
    (board['T1'] == 'X' and board['M2'] == 'X' and board['B3'] == 'X') or
    (board['T3'] == 'X' and board['M2'] == 'X' and board['B1'] == 'X') or
    (board['T1'] == 'X' and board['M1'] == 'X' and board['B1'] == 'X') or 
    (board['T2'] == 'X' and board['M2'] == 'X' and board['B2'] == 'X') or 
    (board['T3'] == 'X' and board['M3'] == 'X' and board['B3'] == 'X')):
        print("Player One Won")
        break
    elif ((board['T1'] == 'O' and board['T2'] == 'O' and board['T3'] == 'O') or
    (board['B1'] == 'O' and board['B2'] == 'O' and board['B3'] == 'O') or
    (board['M1'] == 'O' and board['M2'] == 'O' and board['M3'] == 'O') or
    (board['T1'] == 'O' and board['M2'] == 'O' and board['B3'] == 'O') or
    (board['T3'] == 'O' and board['M2'] == 'O' and board['B1'] == 'O') or
    (board['T1'] == 'O' and board['M1'] == 'O' and board['B1'] == 'O') or
    (board['T2'] == 'O' and board['M2'] == 'O' and board['B2'] == 'O') or
    (board['T3'] == 'O' and board['M3'] == 'O' and board['B3'] == 'O')):
        print("Player 2 Won")
        break
    if total_moves == 9:
        break
    while True:
        if player == 1:
            p1_input = input("Player One: ")
            if p1_input.upper() in board and board[p1_input.upper()] == ' ':
                board[p1_input.upper()] = 'X'
                player = 2
                break
            else:
                print("Please Enter Again, Wrong Input!")
        else:
            p2_input = input("Player Two: ")
            if p2_input.upper() in board and board[p2_input.upper()] == ' ':
                board[p2_input.upper()] = 'O'
                player = 1
                break
            else:
                print("Please Enter Again, Wrong Input!")
    total_moves += 1
    print()
    print("*************".center(50))
    print()
