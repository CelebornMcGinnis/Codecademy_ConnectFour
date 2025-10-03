#Imports
import script
import os
import time

#Variables
bool_winner_found = False
bool_valid_move = False
bool_player_decision = False
int_round = 1
int_player1_input = 0
int_player2_input = 0
int_player_input = 0
str_player_input = ""
str_winning_player = ""
printStr = ""

#modifiable indices for the board (v = variable, x = column in board print structure, r = row, y = row number)
v3r1 = " "; v7r1 = " "; v12r1 = " "; v16r1 = " "; v20r1 = " "; v24r1 = " "; v28r1 = " "
v3r2 = " "; v7r2 = " "; v12r2 = " "; v16r2 = " "; v20r2 = " "; v24r2 = " "; v28r2 = " "
v3r3 = " "; v7r3 = " "; v12r3 = " "; v16r3 = " "; v20r3 = " "; v24r3 = " "; v28r3 = " "
v3r4 = " "; v7r4 = " "; v12r4 = " "; v16r4 = " "; v20r4 = " "; v24r4 = " "; v28r4 = " "
v3r5 = " "; v7r5 = " "; v12r5 = " "; v16r5 = " "; v20r5 = " "; v24r5 = " "; v28r5 = " "
v3r6 = " "; v7r6 = " "; v12r6 = " "; v16r6 = " "; v20r6 = " "; v24r6 = " "; v28r6 = " "

print("Let's play some Connect Four!\n")
v3r1,v7r1,v12r1,v16r1,v20r1,v24r1,v28r1,v3r2,v7r2,v12r2,v16r2,v20r2,v24r2,v28r2,v3r3,v7r3,v12r3,v16r3,v20r3,v24r3,v28r3,v3r4,v7r4,v12r4,v16r4,v20r4,v24r4,v28r4,v3r5,v7r5,v12r5,v16r5,v20r5,v24r5,v28r5,v3r6,v7r6,v12r6,v16r6,v20r6,v24r6,v28r6 = script.board_main(v3r1,v7r1,v12r1,v16r1,v20r1,v24r1,v28r1,v3r2,v7r2,v12r2,v16r2,v20r2,v24r2,v28r2,v3r3,v7r3,v12r3,v16r3,v20r3,v24r3,v28r3,v3r4,v7r4,v12r4,v16r4,v20r4,v24r4,v28r4,v3r5,v7r5,v12r5,v16r5,v20r5,v24r5,v28r5,v3r6,v7r6,v12r6,v16r6,v20r6,v24r6,v28r6)

#The while loop will run 42 times since 42 is the maximum number of turns in a game of Connect Four
while int_round <= 42 and bool_winner_found == False:
  #check for winner
  bool_winner_found, str_winning_player = script.winner_check(v3r1,v7r1,v12r1,v16r1,v20r1,v24r1,v28r1,v3r2,v7r2,v12r2,v16r2,v20r2,v24r2,v28r2,v3r3,v7r3,v12r3,v16r3,v20r3,v24r3,v28r3,v3r4,v7r4,v12r4,v16r4,v20r4,v24r4,v28r4,v3r5,v7r5,v12r5,v16r5,v20r5,v24r5,v28r5,v3r6,v7r6,v12r6,v16r6,v20r6,v24r6,v28r6)
  if bool_winner_found == True:
    print(str_winning_player + " is the winner!")
    time.sleep(1.5)
    while bool_player_decision == False and str_winning_player != "":
      str_player_decision = input("Would you like to play again? (y/n): ")
      bool_player_decision, str_player_decision = script.player_decision_check(str_player_decision)

    if str_player_decision == "y":
      os.system('clear')
      #modifiable indices for the board (v = variable, x = column in board print structure, r = row, y = row number)
      v3r1 = " "; v7r1 = " "; v12r1 = " "; v16r1 = " "; v20r1 = " "; v24r1 = " "; v28r1 = " "
      v3r2 = " "; v7r2 = " "; v12r2 = " "; v16r2 = " "; v20r2 = " "; v24r2 = " "; v28r2 = " "
      v3r3 = " "; v7r3 = " "; v12r3 = " "; v16r3 = " "; v20r3 = " "; v24r3 = " "; v28r3 = " "
      v3r4 = " "; v7r4 = " "; v12r4 = " "; v16r4 = " "; v20r4 = " "; v24r4 = " "; v28r4 = " "
      v3r5 = " "; v7r5 = " "; v12r5 = " "; v16r5 = " "; v20r5 = " "; v24r5 = " "; v28r5 = " "
      v3r6 = " "; v7r6 = " "; v12r6 = " "; v16r6 = " "; v20r6 = " "; v24r6 = " "; v28r6 = " "
      print("Let's play some Connect Four!\n")
      script.board_main(v3r1,v7r1,v12r1,v16r1,v20r1,v24r1,v28r1,v3r2,v7r2,v12r2,v16r2,v20r2,v24r2,v28r2,v3r3,v7r3,v12r3,v16r3,v20r3,v24r3,v28r3,v3r4,v7r4,v12r4,v16r4,v20r4,v24r4,v28r4,v3r5,v7r5,v12r5,v16r5,v20r5,v24r5,v28r5,v3r6,v7r6,v12r6,v16r6,v20r6,v24r6,v28r6)
      str_winning_player = ""
      str_player_decision = ""
      bool_winner_found = False
      bool_player_decision = False
      int_round = 1
      
    else:
      os.system('clear')
      print("Thank you for playing!")
      exit()
      
  bool_player_value_check = False #This boolean will update to True if the player's input is valid
  #While loop for checking if the player's input is valid
  while bool_player_value_check == False:
    int_player1_input = 0 #Reset the player's input to 0
    int_player2_input = 0 #Reset the player's input to 0
    int_player_input = 0 #Reset variable to 0
    str_player_input = "" #reset variable to empty string
    printStr = "" #reset variable to empty string
    
    #Player 1's turn
    if int_round % 2 != 0: int_player1_input = input("Player 1, please enter the column number you would like to place your piece (X) in: ")
    #Player 2's turn
    else: int_player2_input = input("Player 2, please enter the column number you would like to place your piece (O) in: ")

    if int_player1_input != 0: str_player_input = int_player1_input
    else: str_player_input = int_player2_input
    #Calling the function to check if the player's input is valid
    bool_player_value_check, int_player_input = script.check_player_input(str_player_input)
  
    #validate move is allowed (column is not full)
    bool_valid_move,printStr,v3r1,v7r1,v12r1,v16r1,v20r1,v24r1,v28r1,v3r2,v7r2,v12r2,v16r2,v20r2,v24r2,v28r2,v3r3,v7r3,v12r3,v16r3,v20r3,v24r3,v28r3,v3r4,v7r4,v12r4,v16r4,v20r4,v24r4,v28r4,v3r5,v7r5,v12r5,v16r5,v20r5,v24r5,v28r5,v3r6,v7r6,v12r6,v16r6,v20r6,v24r6,v28r6 = script.valid_move_check(int_player_input,int_round % 2,v3r1,v7r1,v12r1,v16r1,v20r1,v24r1,v28r1,v3r2,v7r2,v12r2,v16r2,v20r2,v24r2,v28r2,v3r3,v7r3,v12r3,v16r3,v20r3,v24r3,v28r3,v3r4,v7r4,v12r4,v16r4,v20r4,v24r4,v28r4,v3r5,v7r5,v12r5,v16r5,v20r5,v24r5,v28r5,v3r6,v7r6,v12r6,v16r6,v20r6,v24r6,v28r6)
    
  #clear the screen and print the board
  os.system('clear')
  print(printStr)
  script.board_main(v3r1,v7r1,v12r1,v16r1,v20r1,v24r1,v28r1,v3r2,v7r2,v12r2,v16r2,v20r2,v24r2,v28r2,v3r3,v7r3,v12r3,v16r3,v20r3,v24r3,v28r3,v3r4,v7r4,v12r4,v16r4,v20r4,v24r4,v28r4,v3r5,v7r5,v12r5,v16r5,v20r5,v24r5,v28r5,v3r6,v7r6,v12r6,v16r6,v20r6,v24r6,v28r6)
  int_round += 1
