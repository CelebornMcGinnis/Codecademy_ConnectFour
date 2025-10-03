#function called to print the board
def board_main(v3r1,v7r1,v12r1,v16r1,v20r1,v24r1,v28r1,v3r2,v7r2,v12r2,v16r2,v20r2,v24r2,v28r2,v3r3,v7r3,v12r3,v16r3,v20r3,v24r3,v28r3,v3r4,v7r4,v12r4,v16r4,v20r4,v24r4,v28r4,v3r5,v7r5,v12r5,v16r5,v20r5,v24r5,v28r5,v3r6,v7r6,v12r6,v16r6,v20r6,v24r6,v28r6):
  #Board Data Structures
  dividers = ["*---*---*---*---*---*---*---*"]
  unchanging_rows = ["|   |   |   |   |   |   |   |"]
  table_header = [" "," ","1"," "," "," ","2"," "," "," ","3"," "," "," ","4"," "," "," ","5"," "," "," ","6"," "," "," ","7"," "," "]

  """
  For change_row1-6, the indices that can be modified (and therefore checked) are:
    3, 7, 12, 16, 20, 24, 28
  """
  change_row1 = ["|"," ",v3r1," ","|"," ",v7r1," ","|"," ",v12r1," ","|"," ",v16r1," ","|"," ",v20r1," ","|"," ",v24r1," ","|"," ",v28r1," ","|"]
  change_row2 = ["|"," ",v3r2," ","|"," ",v7r2," ","|"," ",v12r2," ","|"," ",v16r2," ","|"," ",v20r2," ","|"," ",v24r2," ","|"," ",v28r2," ","|"]
  change_row3 = ["|"," ",v3r3," ","|"," ",v7r3," ","|"," ",v12r3," ","|"," ",v16r3," ","|"," ",v20r3," ","|"," ",v24r3," ","|"," ",v28r3," ","|"]
  change_row4 = ["|"," ",v3r4," ","|"," ",v7r4," ","|"," ",v12r4," ","|"," ",v16r4," ","|"," ",v20r4," ","|"," ",v24r4," ","|"," ",v28r4," ","|"]
  change_row5 = ["|"," ",v3r5," ","|"," ",v7r5," ","|"," ",v12r5," ","|"," ",v16r5," ","|"," ",v20r5," ","|"," ",v24r5," ","|"," ",v28r5," ","|"]
  change_row6 = ["|"," ",v3r6," ","|"," ",v7r6," ","|"," ",v12r6," ","|"," ",v16r6," ","|"," ",v20r6," ","|"," ",v24r6," ","|"," ",v28r6," ","|"]

  #Board Table for iteration
  board_table = [
    table_header,dividers,
    unchanging_rows,change_row1,unchanging_rows,dividers,
    unchanging_rows,change_row2,unchanging_rows,dividers,
    unchanging_rows,change_row3,unchanging_rows,dividers,
    unchanging_rows,change_row4,unchanging_rows,dividers,
    unchanging_rows,change_row5,unchanging_rows,dividers,
    unchanging_rows,change_row6,unchanging_rows,dividers
    ]

  #Loop for printing the board
  index = 0
  for i in board_table:
    for index in i:
      print(index, end="")
    print()

  return v3r1,v7r1,v12r1,v16r1,v20r1,v24r1,v28r1,v3r2,v7r2,v12r2,v16r2,v20r2,v24r2,v28r2,v3r3,v7r3,v12r3,v16r3,v20r3,v24r3,v28r3,v3r4,v7r4,v12r4,v16r4,v20r4,v24r4,v28r4,v3r5,v7r5,v12r5,v16r5,v20r5,v24r5,v28r5,v3r6,v7r6,v12r6,v16r6,v20r6,v24r6,v28r6

#------------------------------------------------------------------------------------------------------------

#function called to check if the player's input is valid
def check_player_input(int_player_input):
  if int_player_input.isdigit() and int_player_input in ["1","2","3","4","5","6","7"]:
    return True, int(int_player_input)
  else:
    print("Please enter a valid column number (1-7)")
    return False,0

#------------------------------------------------------------------------------------------------------------

#function called to check if player wants to play again
def player_decision_check(str_player_decision):
  bool_player_decision = False
  
  if str_player_decision == "y" or str_player_decision == "Y":
    bool_player_decision = True
    str_player_decision = "y"

  elif str_player_decision == "n" or str_player_decision == "N":
    bool_player_decision = True
    str_player_decision = "n"
  
  else: print("Please enter a valid input (y/n)")
  return bool_player_decision, str_player_decision


#------------------------------------------------------------------------------------------------------------

#function called to check if player move is valid (column is not full)
def valid_move_check(int_player_input,int_mod_value,v3r1,v7r1,v12r1,v16r1,v20r1,v24r1,v28r1,v3r2,v7r2,v12r2,v16r2,v20r2,v24r2,v28r2,v3r3,v7r3,v12r3,v16r3,v20r3,v24r3,v28r3,v3r4,v7r4,v12r4,v16r4,v20r4,v24r4,v28r4,v3r5,v7r5,v12r5,v16r5,v20r5,v24r5,v28r5,v3r6,v7r6,v12r6,v16r6,v20r6,v24r6,v28r6):
  printStr = "\n"
  if int_player_input == 1:
    if v3r6 == " ": 
      if int_mod_value == 1: v3r6 = "X"
      elif int_mod_value == 0: v3r6 = "O"
    elif v3r5 == " ":
      if int_mod_value == 1: v3r5 = "X"
      elif int_mod_value == 0: v3r5 = "O"
    elif v3r4 == " ":
      if int_mod_value == 1: v3r4 = "X"
      elif int_mod_value == 0: v3r4 = "O"
    elif v3r3 == " ":
      if int_mod_value == 1: v3r3 = "X"
      elif int_mod_value == 0: v3r3 = "O"
    elif v3r2 == " ":
      if int_mod_value == 1: v3r2 = "X"
      elif int_mod_value == 0: v3r2 = "O"
    elif v3r1 == " ":
      if int_mod_value == 1: v3r1 = "X"
      elif int_mod_value == 0: v3r1 = "O"
    else:
      printStr = "Column " + str(int_player_input) + " is full\n"
      
  elif int_player_input == 2:
    if v7r6 == " ": 
      if int_mod_value == 1: v7r6 = "X"
      elif int_mod_value == 0: v7r6 = "O"
    elif v7r5 == " ":
      if int_mod_value == 1: v7r5 = "X"
      elif int_mod_value == 0: v7r5 = "O"
    elif v7r4 == " ":
      if int_mod_value == 1: v7r4 = "X"
      elif int_mod_value == 0: v7r4 = "O"
    elif v7r3 == " ":
      if int_mod_value == 1: v7r3 = "X"
      elif int_mod_value == 0: v7r3 = "O"
    elif v7r2 == " ":
      if int_mod_value == 1: v7r2 = "X"
      elif int_mod_value == 0: v7r2 = "O"
    elif v7r1 == " ":
      if int_mod_value == 1: v7r1 = "X"
      elif int_mod_value == 0: v7r1 = "O"
    else:
      printStr = "Column " + str(int_player_input) + " is full\n"
      
  elif int_player_input == 3: 
    if v12r6 == " ": 
      if int_mod_value == 1: v12r6 = "X"
      elif int_mod_value == 0: v12r6 = "O"
    elif v12r5 == " ":
      if int_mod_value == 1: v12r5 = "X"
      elif int_mod_value == 0: v12r5 = "O"
    elif v12r4 == " ":
      if int_mod_value == 1: v12r4 = "X"
      elif int_mod_value == 0: v12r4 = "O"
    elif v12r3 == " ":
      if int_mod_value == 1: v12r3 = "X"
      elif int_mod_value == 0: v12r3 = "O"
    elif v12r2 == " ":
      if int_mod_value == 1: v12r2 = "X"
      elif int_mod_value == 0: v12r2 = "O"
    elif v12r1 == " ":
      if int_mod_value == 1: v12r1 = "X"
      elif int_mod_value == 0: v12r1 = "O"
    else:
      printStr = "Column " + str(int_player_input) + " is full\n"
    
  elif int_player_input == 4:
    if v16r6 == " ": 
      if int_mod_value == 1: v16r6 = "X"
      elif int_mod_value == 0: v16r6 = "O"
    elif v16r5 == " ":
      if int_mod_value == 1: v16r5 = "X"
      elif int_mod_value == 0: v16r5 = "O"
    elif v16r4 == " ":
      if int_mod_value == 1: v16r4 = "X"
      elif int_mod_value == 0: v16r4 = "O"
    elif v16r3 == " ":
      if int_mod_value == 1: v16r3 = "X"
      elif int_mod_value == 0: v16r3 = "O"
    elif v16r2 == " ":
      if int_mod_value == 1: v16r2 = "X"
      elif int_mod_value == 0: v16r2 = "O"
    elif v16r1 == " ":
      if int_mod_value == 1: v16r1 = "X"
      elif int_mod_value == 0: v16r1 = "O"
    else:
      printStr = "Column " + str(int_player_input) + " is full\n"

  elif int_player_input == 5:
    if v20r6 == " ": 
      if int_mod_value == 1: v20r6 = "X"
      elif int_mod_value == 0: v20r6 = "O"
    elif v20r5 == " ":
      if int_mod_value == 1: v20r5 = "X"
      elif int_mod_value == 0: v20r5 = "O"
    elif v20r4 == " ":
      if int_mod_value == 1: v20r4 = "X"
      elif int_mod_value == 0: v20r4 = "O"
    elif v20r3 == " ":
      if int_mod_value == 1: v20r3 = "X"
      elif int_mod_value == 0: v20r3 = "O"
    elif v20r2 == " ":
      if int_mod_value == 1: v20r2 = "X"
      elif int_mod_value == 0: v20r2 = "O"
    elif v20r1 == " ":
      if int_mod_value == 1: v20r1 = "X"
      elif int_mod_value == 0: v20r1 = "O"
    else:
      printStr = "Column " + str(int_player_input) + " is full\n"
    
  elif int_player_input == 6:
    if v24r6 == " ": 
      if int_mod_value == 1: v24r6 = "X"
      elif int_mod_value == 0: v24r6 = "O"
    elif v24r5 == " ":
      if int_mod_value == 1: v24r5 = "X"
      elif int_mod_value == 0: v24r5 = "O"
    elif v24r4 == " ":
      if int_mod_value == 1: v24r4 = "X"
      elif int_mod_value == 0: v24r4 = "O"
    elif v24r3 == " ":
      if int_mod_value == 1: v24r3 = "X"
      elif int_mod_value == 0: v24r3 = "O"
    elif v24r2 == " ":
      if int_mod_value == 1: v24r2 = "X"
      elif int_mod_value == 0: v24r2 = "O"
    elif v24r1 == " ":
      if int_mod_value == 1: v24r1 = "X"
      elif int_mod_value == 0: v24r1 = "O"
    else:
      printStr = "Column " + str(int_player_input) + " is full\n"
    
  elif int_player_input == 7:
    if v28r6 == " ": 
      if int_mod_value == 1: v28r6 = "X"
      elif int_mod_value == 0: v28r6 = "O"
    elif v28r5 == " ":
      if int_mod_value == 1: v28r5 = "X"
      elif int_mod_value == 0: v28r5 = "O"
    elif v28r4 == " ":
      if int_mod_value == 1: v28r4 = "X"
      elif int_mod_value == 0: v28r4 = "O"
    elif v28r3 == " ":
      if int_mod_value == 1: v28r3 = "X"
      elif int_mod_value == 0: v28r3 = "O"
    elif v28r2 == " ":
      if int_mod_value == 1: v28r2 = "X"
      elif int_mod_value == 0: v28r2 = "O"
    elif v28r1 == " ":
      if int_mod_value == 1: v28r1 = "X"
      elif int_mod_value == 0: v28r1 = "O"
    else:
      printStr = "Column " + str(int_player_input) + " is full\n"

  return True,printStr,v3r1,v7r1,v12r1,v16r1,v20r1,v24r1,v28r1,v3r2,v7r2,v12r2,v16r2,v20r2,v24r2,v28r2,v3r3,v7r3,v12r3,v16r3,v20r3,v24r3,v28r3,v3r4,v7r4,v12r4,v16r4,v20r4,v24r4,v28r4,v3r5,v7r5,v12r5,v16r5,v20r5,v24r5,v28r5,v3r6,v7r6,v12r6,v16r6,v20r6,v24r6,v28r6

#------------------------------------------------------------------------------------------------------------

#function called to check if there is a winner
def winner_check(v3r1,v7r1,v12r1,v16r1,v20r1,v24r1,v28r1,v3r2,v7r2,v12r2,v16r2,v20r2,v24r2,v28r2,v3r3,v7r3,v12r3,v16r3,v20r3,v24r3,v28r3,v3r4,v7r4,v12r4,v16r4,v20r4,v24r4,v28r4,v3r5,v7r5,v12r5,v16r5,v20r5,v24r5,v28r5,v3r6,v7r6,v12r6,v16r6,v20r6,v24r6,v28r6):
  str_winning_player = ""
  
  #check for horizontal winner
  if v3r1 == v7r1 == v12r1 == v16r1 == "X" or v7r1 == v12r1 == v16r1 == v20r1 == "X" or v12r1 == v16r1 == v20r1 == v24r1 == "X" or v16r1 == v20r1 == v24r1 == v28r1 == "X" or v3r2 == v7r2 == v12r2 == v16r2 == "X" or v7r2 == v12r2 == v16r2 == v20r2 == "X" or v12r2 == v16r2 == v20r2 == v24r2 == "X" or v16r2 == v20r2 == v24r2 == v28r2 == "X" or v3r3 == v7r3 == v12r3 == v16r3 == "X" or v7r3 == v12r3 == v16r3 == v20r3 == "X" or v12r3 == v16r3 == v20r3 == v24r3 == "X" or v16r3 == v20r3 == v24r3 == v28r3 == "X" or v3r4 == v7r4 == v12r4 == v16r4 == "X" or v7r4 == v12r4 == v16r4 == v20r4 == "X" or v12r4 == v16r4 == v20r4 == v24r4 == "X" or v16r4 == v20r4 == v24r4 == v28r4 == "X" or v3r5 == v7r5 == v12r5 == v16r5 == "X" or v7r5 == v12r5 == v16r5 == v20r5 == "X" or v12r5 == v16r5 == v20r5 == v24r5 == "X" or v16r5 == v20r5 == v24r5 == v28r5 == "X" or v3r6 == v7r6 == v12r6 == v16r6 == "X" or v7r6 == v12r6 == v16r6 == v20r6 == "X" or v12r6 == v16r6 == v20r6 == v24r6 == "X" or v16r6 == v20r6 == v24r6 == v28r6 == "X":
    str_winning_player = "Player 1"
    return True, str_winning_player
  elif v3r1 == v7r1 == v12r1 == v16r1 == "O" or v7r1 == v12r1 == v16r1 == v20r1 == "O" or v12r1 == v16r1 == v20r1 == v24r1 == "O" or v16r1 == v20r1 == v24r1 == v28r1 == "O" or v3r2 == v7r2 == v12r2 == v16r2 == "O" or v7r2 == v12r2 == v16r2 == v20r2 == "O" or v12r2 == v16r2 == v20r2 == v24r2 == "O" or v16r2 == v20r2 == v24r2 == v28r2 == "O" or v3r3 == v7r3 == v12r3 == v16r3 == "O" or v7r3 == v12r3 == v16r3 == v20r3 == "O" or v12r3 == v16r3 == v20r3 == v24r3 == "O" or v16r3 == v20r3 == v24r3 == v28r3 == "O" or v3r4 == v7r4 == v12r4 == v16r4 == "O" or v7r4 == v12r4 == v16r4 == v20r4 == "O" or v12r4 == v16r4 == v20r4 == v24r4 == "O" or v16r4 == v20r4 == v24r4 == v28r4 == "O" or v3r5 == v7r5 == v12r5 == v16r5 == "O" or v7r5 == v12r5 == v16r5 == v20r5 == "O" or v12r5 == v16r5 == v20r5 == v24r5 == "O" or v16r5 == v20r5 == v24r5 == v28r5 == "O" or v3r6 == v7r6 == v12r6 == v16r6 == "O" or v7r6 == v12r6 == v16r6 == v20r6 == "O" or v12r6 == v16r6 == v20r6 == v24r6 == "O" or v16r6 == v20r6 == v24r6 == v28r6 == "O":
    str_winning_player = "Player 2"
    return True, str_winning_player

  #check for vertical winner
  if v3r1 == v3r2 == v3r3 == v3r4 == "X" or v3r2 == v3r3 == v3r4 == v3r5 == "X" or v3r3 == v3r4 == v3r5 == v3r6 == "X" or v7r1 == v7r2 == v7r3 == v7r4 == "X" or v7r2 == v7r3 == v7r4 == v7r5 == "X" or v7r3 == v7r4 == v7r5 == v7r6 == "X" or v12r1 == v12r2 == v12r3 == v12r4 == "X" or v12r2 == v12r3 == v12r4 == v12r5 == "X" or v12r3 == v12r4 == v12r5 == v12r6 == "X" or v16r1 == v16r2 == v16r3 == v16r4 == "X" or v16r2 == v16r3 == v16r4 == v16r5 == "X" or v16r3 == v16r4 == v16r5 == v16r6 == "X" or v20r1 == v20r2 == v20r3 == v20r4 == "X" or v20r2 == v20r3 == v20r4 == v20r5 == "X" or v20r3 == v20r4 == v20r5 == v20r6 == "X" or v24r1 == v24r2 == v24r3 == v24r4 == "X" or v24r2 == v24r3 == v24r4 == v24r5 == "X" or v24r3 == v24r4 == v24r5 == v24r6 == "X" or v28r1 == v28r2 == v28r3 == v28r4 == "X" or v28r2 == v28r3 == v28r4 == v28r5 == "X" or v28r3 == v28r4 == v28r5 == v28r6 == "X":
    str_winning_player = "Player 1"
    return True, str_winning_player
  elif v3r1 == v3r2 == v3r3 == v3r4 == "O" or v3r2 == v3r3 == v3r4 == v3r5 == "O" or v3r3 == v3r4 == v3r5 == v3r6 == "O" or v7r1 == v7r2 == v7r3 == v7r4 == "O" or v7r2 == v7r3 == v7r4 == v7r5 == "O" or v7r3 == v7r4 == v7r5 == v7r6 == "O" or v12r1 == v12r2 == v12r3 == v12r4 == "O" or v12r2 == v12r3 == v12r4 == v12r5 == "O" or v12r3 == v12r4 == v12r5 == v12r6 == "O" or v16r1 == v16r2 == v16r3 == v16r4 == "O" or v16r2 == v16r3 == v16r4 == v16r5 == "O" or v16r3 == v16r4 == v16r5 == v16r6 == "O" or v20r1 == v20r2 == v20r3 == v20r4 == "O" or v20r2 == v20r3 == v20r4 == v20r5 == "O" or v20r3 == v20r4 == v20r5 == v20r6 == "O" or v24r1 == v24r2 == v24r3 == v24r4 == "O" or v24r2 == v24r3 == v24r4 == v24r5 == "O" or v24r3 == v24r4 == v24r5 == v24r6 == "O" or v28r1 == v28r2 == v28r3 == v28r4 == "O" or v28r2 == v28r3 == v28r4 == v28r5 == "O" or v28r3 == v28r4 == v28r5 == v28r6 == "O":
    str_winning_player = "Player 2"
    return True, str_winning_player

  
  #check for diagonal winner
  if v3r1 == v7r2 == v12r3 == v16r4 == "X" or v7r1 == v12r2 == v16r3 == v20r4 == "X" or v12r1 == v16r2 == v20r3 == v24r4 == "X" or v16r1 == v20r2 == v24r3 == v28r4 == "X" or v20r1 == v16r2 == v12r3 == v7r4 == "X" or v24r1 == v20r2 == v16r3 == v12r4 == "X" or v28r1 == v24r2 == v20r3 == v16r4 == "X" or v3r2 == v7r3 == v12r4 == v16r5 == "X" or v7r2 == v12r3 == v16r4 == v20r5 == "X" or v12r2 == v16r3 == v20r4 == v24r5 == "X" or v16r2 == v20r3 == v24r4 == v28r5 == "X" or v20r2 == v16r3 == v12r4 == v7r5 == "X" or v24r2 == v20r3 == v16r4 == v12r5 == "X" or v28r2 == v24r3 == v20r4 == v16r5 == "X" or v3r3 == v7r4 == v12r5 == v16r6 == "X" or v7r3 == v12r4 == v16r5 == v20r6 == "X" or v12r3 == v16r4 == v20r5 == v24r6 == "X" or v16r3 == v20r4 == v24r5 == v28r6 == "X" or v20r3 == v16r4 == v12r5 == v7r6 == "X" or v24r3 == v20r4 == v16r5 == v12r6 == "X" or v28r3 == v24r4 == v20r5 == v16r6 == "X" or v3r6 == v7r5 == v12r4 == v16r3 == "X" or v7r6 == v12r5 == v16r4 == v20r3 == "X" or v12r6 == v16r5 == v20r4 == v24r3 == "X" or v16r6 == v20r5 == v24r4 == v28r3 == "X" or v20r6 == v16r5 == v12r4 == v7r3 == "X" or v24r6 == v20r5 == v16r4 == v12r3 == "X" or v28r6 == v24r5 == v20r4 == v16r3 == "X" or v3r5 == v7r4 == v12r3 == v16r2 == "X" or v7r5 == v12r4 == v16r3 == v20r2 == "X" or v12r5 == v16r4 == v20r3 == v24r2 == "X" or v16r5 == v20r4 == v24r3 == v28r2 == "X" or v20r5 == v16r4 == v12r3 == v7r2 == "X" or v24r5 == v20r4 == v16r3 == v12r2 == "X" or v28r5 == v24r4 == v20r3 == v16r2 == "X" or v3r4 == v7r3 == v12r2 == v16r1 == "X" or v7r4 == v12r3 == v16r2 == v20r1 == "X" or v12r4 == v16r3 == v20r2 == v24r1 == "X" or v16r4 == v20r3 == v24r2 == v28r1 == "X" or v20r4 == v16r3 == v12r2 == v7r1 == "X" or v24r4 == v20r3 == v16r2 == v12r1 == "X" or v28r4 == v24r3 == v20r2 == v16r1 == "X": 
    str_winning_player = "Player 1"
    return True, str_winning_player
  elif v3r1 == v7r2 == v12r3 == v16r4 == "O" or v7r1 == v12r2 == v16r3 == v20r4 == "O" or v12r1 == v16r2 == v20r3 == v24r4 == "O" or v16r1 == v20r2 == v24r3 == v28r4 == "O" or v20r1 == v16r2 == v12r3 == v7r4 == "O" or v24r1 == v20r2 == v16r3 == v12r4 == "O" or v28r1 == v24r2 == v20r3 == v16r4 == "O" or v3r2 == v7r3 == v12r4 == v16r5 == "O" or v7r2 == v12r3 == v16r4 == v20r5 == "O" or v12r2 == v16r3 == v20r4 == v24r5 == "O" or v16r2 == v20r3 == v24r4 == v28r5 == "O" or v20r2 == v16r3 == v12r4 == v7r5 == "O" or v24r2 == v20r3 == v16r4 == v12r5 == "O" or v28r2 == v24r3 == v20r4 == v16r5 == "O" or v3r3 == v7r4 == v12r5 == v16r6 == "O" or v7r3 == v12r4 == v16r5 == v20r6 == "O" or v12r3 == v16r4 == v20r5 == v24r6 == "O" or v16r3 == v20r4 == v24r5 == v28r6 == "O" or v20r3 == v16r4 == v12r5 == v7r6 == "O" or v24r3 == v20r4 == v16r5 == v12r6 == "O" or v28r3 == v24r4 == v20r5 == v16r6 == "O" or v3r6 == v7r5 == v12r4 == v16r3 == "O" or v7r6 == v12r5 == v16r4 == v20r3 == "O" or v12r6 == v16r5 == v20r4 == v24r3 == "O" or v16r6 == v20r5 == v24r4 == v28r3 == "O" or v20r6 == v16r5 == v12r4 == v7r3 == "O" or v24r6 == v20r5 == v16r4 == v12r3 == "O" or v28r6 == v24r5 == v20r4 == v16r3 == "O" or v3r5 == v7r4 == v12r3 == v16r2 == "O" or v7r5 == v12r4 == v16r3 == v20r2 == "O" or v12r5 == v16r4 == v20r3 == v24r2 == "O" or v16r5 == v20r4 == v24r3 == v28r2 == "O" or v20r5 == v16r4 == v12r3 == v7r2 == "O" or v24r5 == v20r4 == v16r3 == v12r2 == "O" or v28r5 == v24r4 == v20r3 == v16r2 == "O" or v3r4 == v7r3 == v12r2 == v16r1 == "O" or v7r4 == v12r3 == v16r2 == v20r1 == "O" or v12r4 == v16r3 == v20r2 == v24r1 == "O" or v16r4 == v20r3 == v24r2 == v28r1 == "O" or v20r4 == v16r3 == v12r2 == v7r1 == "O" or v24r4 == v20r3 == v16r2 == v12r1 == "O" or v28r4 == v24r3 == v20r2 == v16r1 == "O":
    str_winning_player = "Player 2"
    return True, str_winning_player
  
  return False, str_winning_player
