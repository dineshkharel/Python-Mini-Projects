import random,msvcrt
import board
import winlogic
print("Welcome to the tic_tac_toe:")
combo =[["","",""],
        ["","",""],
        ["","",""]]
player_symbol= {
    1:"X",
    2:"O"
}
print("""The symbols are:
1 for 'X' 
2 for 'O' """)
human_symbol= int (input("Enter the player symbol:"))
if human_symbol ==1:
    computer_symbol =2
else:
    computer_symbol=1
marked=[]
print("""Positions: 
| 1  2  3 |
| 4  5  6 | 
| 7  8  9 | """)

while len(marked) !=9:
  
    mark = int(input("Where do you want to place your mark?" \
    ""))
    
    if 1<= mark <=9 and mark not in marked:
        row = (mark -1)//3
        col = (mark-1)%3
        combo[row][col]=player_symbol[human_symbol]
        marked.append(mark)
    else:
        print("Invalid move")
        continue
    winner= winlogic.check_logic(combo)
    if winner:
        board.print_board(combo)
        print(f"{winner} won the game")
        break
    if len(marked)==9:
        board.print_board(combo)
        print("Game draw!")
        break

    computer_move=random.randint(1,9)
    while computer_move in marked:
        computer_move=random.randint(1,9)
    marked.append(computer_move)
    row=(computer_move-1)//3
    col=(computer_move-1)%3
    combo[row][col]=player_symbol[computer_symbol]

    board.print_board(combo)
    winner= winlogic.check_logic(combo)
    if winner:
        print(f"{winner} won the game")
        break

msvcrt.getch()