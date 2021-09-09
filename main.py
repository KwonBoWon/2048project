import copy
from arrow import Arrows

board_temp=[]
arrow = Arrows()
print("=====2048 game=====")
print("play the game with 'w,a,s,d'")
print("press 'Enter' to start the game!")
input()
arrow.create()




while True:
  arrow.clear()
  arrow.screen()
  arrow.key=input()

  arrow.board_temp = copy.deepcopy(arrow.board)#깊은 복사((새롭게 복사))

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
  

  if (arrow.board_temp == arrow.board)==True:
    continue
  arrow.create()
  arrow.clear() # window    
  arrow.screen()

  if arrow.quit_key == 1:
    break