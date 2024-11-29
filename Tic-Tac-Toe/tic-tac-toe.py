def print_board(n, board):
  # premake +---+ style boundary using string mutiplication and concatination
  boundary_line = ("+---" * n) + "+"
  # range over every row in board (an n by n board)
  for i in range(n):
    # print a leading boundary line
    print(boundary_line)
    # start string for row i with leading bar
    row_i = "|"
    # range over every column in board (an n by n board)
    for j in range(n):
      # update row_i string with space, characher from board, space, and trailing bar
      # this completes "cell j" for row i
      row_i += " " + board[i][j] + " " + "|"
    # print the completed row i
    print(row_i)
  # print final boundary line
  print(boundary_line)

def make_empty_board(n):
  board_list = []
  for i in list(range(n)):
    board_list.append([" "])
  for j in list(range(n-1)):
    for k in board_list:
      k.append(" ")
  return board_list


def get_location(n,game_board):
  r = input(f"Please enter a row index between 0 and {n-1}: ")
  c = input(f"Please enter a column index between 0 and {n-1}: ")
  while r.isdigit() == False or c.isdigit()==False or int(r)>n-1 or int(c)>n-1 or game_board[int(r)][int(c)] != ' ':
    if r.isdigit() == False or c.isdigit() == False:
      print(f"({r}, {c}) is not a legal input!")  
      r = input(f"Please enter a row index between 0 and {n-1}: ")
      c = input(f"Please enter a column index between 0 and {n-1}: ")
    elif int(r) > n-1 or int(c) > n-1:
      print(f"({r}, {c}) is not a legal space!")
      r = input(f"Please enter a row index between 0 and {n-1}: ")
      c = input(f"Please enter a column index between 0 and {n-1}: ")
    elif game_board[int(r)][int(c)] != ' ':
      print(f"({r}, {c}) is not an available space!")
      r = input(f"Please enter a row index between 0 and {n-1}: ")
      c = input(f"Please enter a column index between 0 and {n-1}: ")
  return int(r),int(c)

#print(get_location(3,make_empty_board(3))[0])
  

def row_win(n,game_board,player):
  for i in range(0, n):
    counter = 0
    for j in range(0, n - 1):
      
      if (game_board[i][j] == player and game_board[i][j] == game_board[i][j + 1]):
        counter += 1

    if counter == n - 1:
      return True

  return False

def col_win(n,game_board,player):
  for i in range(0, n):
    counter = 0
    for j in range(0, n - 1):
      
      if (game_board[j][i] == player and game_board[j][i] == game_board[j + 1][i]):
        counter += 1

    if counter == n - 1:
      return True

  return False

def diag_win(n,game_board,player):
  for i in range(0, n - 1):
    if (game_board[i][i] != player or game_board[i][i] != game_board[i + 1][i + 1]):
      return False
  
  return True

def anti_diag_win(n,game_board,player):
  for i in range(0, n - 1):
    if (game_board[i][n - 1 - i] != player or game_board[i][n - 1 - i] != game_board[i + 1][n - 2 - i]):
      return False
  
  return True

def has_won(n,game_board,player):
  return row_win(n, game_board, player) or col_win(n, game_board, player) or diag_win(n, game_board, player) or anti_diag_win(n, game_board, player)

def play_game(n):
  game_board = make_empty_board(n)
  print(f"*** Welcome to {n} by {n} Tic-Tac-Toe ***")
  print_board(n,game_board)

  moves = 0

  while has_won(n,game_board,'X') == False or has_won(n,game_board,'O') == False:
    print("* X's turn *")
    location = get_location(n,game_board)
    game_board[location[0]][location[1]] = 'X'

    print_board(n,game_board)
    moves += 1
    
    if has_won(n,game_board,'X') == True:
      print("X wins!")
      return None

    if moves >= n * n:
      print("Tie!")
      return None

    print("* O's turn *")
    
    location = get_location(n,game_board)
    game_board[location[0]][location[1]] = 'O'

    print_board(n,game_board)
    moves += 1

    if has_won(n,game_board,'O') == True:
      print("O wins!")
      return None

    if moves >= n * n:
      print("Tie!")
      return None



