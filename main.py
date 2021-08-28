from arrow import Arrows

arrow = Arrows
print("=====2048 game=====")
print("play the game with 'w,a,s,d'")
print("press 'Enter' to start the game!")
input()
arrow.create()

bor=arrow.board.copy()

while True:
  arrow.clear()
  arrow.screen()
  arrow.key=input()

  arrow.board_temp = arrow.board[:]
  if arrow.key == 'w':
    arrow.Merge_up()
  elif arrow.key =='s':
    arrow.Merge_down()
  elif arrow.key =='a':
    arrow.Merge_left()
  elif arrow.key =='d':
    arrow.Merge_right()
  else:
    continue
  
  #if (arrow.board_temp == arrow.board)==True:
  #  continue
  arrow.create()
  arrow.clear() # window    
  arrow.screen()
  print(arrow.board_temp == arrow.board)
  if arrow.quit_key == 1:
    break