import random
import os
class Arrows:
  def __init__(self):
    self.result = 0
  board = [[0 for _ in range(5)] for _ in range(5)]
  board_temp = [[0 for _ in range(5)] for _ in range(5)]
  key = 0
  quit_key = 0
  
#print('\033[31m \033[43m' + '글자와 배경 변경' + '\033[0m') 
  def screen():
    for n in range(4,-1,-1):
      for k in range(5):
        if Arrows.board[n][k]==0:
          print("|" + str(Arrows.board[n][k]).rjust(4),end="| ")
        else:
          print("|" + '\033[96m' + str(Arrows.board[n][k]).rjust(4) + '\033[0m',end="| ")
      print("")
    print("\n")

  def clear():
    os.system('clear')


  def create():#빈칸에서 숫자 스폰
    zerosum = []
    num, zero_choice, number = 0, -1, -1
    for col in range(5):
      for row in range(5):
        if Arrows.board[col][row] == 0:
          zerosum.append([])
          zerosum[num].append(col)
          zerosum[num].append(row)
          num += 1
    if zerosum == False:
      Arrows.quit()
    zero_choice = random.choice(zerosum)

    number = random.randrange(1,9)#248중에 뽑기
    if number <= 4:
      number=2
    elif 4 < number <=7:
      number=4 
    Arrows.board[zero_choice[0]][zero_choice[1]] = number

      
  def quit():#게임오버
    print(" GAME OVER ")
    global quit_key
    quit_key=1

    
  #row행(가로), col열(세로)
  def Merge_left():#왼쪽으로 당기기
    merge_flag=-1
    for col in range(5):
      for row in range(3, -1, -1):#0당겨서 처리
        if Arrows.board[col][row] == 0 and Arrows.board[col][row+1] != 0:#0이있으면 한칸씩 당김
            for shift_row in range(row, 4, 1):
              Arrows.board[col][shift_row], Arrows.board[col][shift_row+1] = Arrows.board[col][shift_row+1], Arrows.board[col][shift_row]

    for col in range(5):
      for row in range(3, -1, -1):#같은것 합치기
        if Arrows.board[col][row] == Arrows.board[col][row+1] and Arrows.board[col][row+1] != 0 and merge_flag != row:#flag이면 스킵
          Arrows.board[col][row+1] *= 2
          Arrows.board[col][row] = 0
          merge_flag = row-1#flag를 다음것으로 바꿈
          for shift_row in range(row, 4, 1):
            Arrows.board[col][shift_row], Arrows.board[col][shift_row+1] = Arrows.board[col][shift_row+1], Arrows.board[col][shift_row]


  def Merge_right():#오른쪽으로 당기기
    merge_flag=-1
    for col in range(5):
      for row in range(1,5):#0당겨서 처리
        if Arrows.board[col][row] == 0 and Arrows.board[col][row-1] != 0:#0이있으면 한칸씩 당김
            for shift_row in range(row, 0, -1):
              Arrows.board[col][shift_row], Arrows.board[col][shift_row-1] = Arrows.board[col][shift_row-1], Arrows.board[col][shift_row]

    for col in range(5):
      for row in range(1,5):#같은것 합치기
        if Arrows.board[col][row] == Arrows.board[col][row-1] and Arrows.board[col][row-1] != 0 and merge_flag != row:#flag면 스킵
          Arrows.board[col][row-1] *= 2
          Arrows.board[col][row] = 0
          merge_flag = row+1#flag를 다음으로 바꿈
          for shift_row in range(row, 0, -1):
            Arrows.board[col][shift_row], Arrows.board[col][shift_row-1] = Arrows.board[col][shift_row-1], Arrows.board[col][shift_row]


  def Merge_up():#위로 당기기
    merge_flag=-1
    for row in range(5):
      for col in range(1,5):#0당겨서 처리
        if Arrows.board[col][row] == 0 and Arrows.board[col-1][row] != 0:#0이있으면 한칸씩 당김
            for shift_col in range(col, 0, -1):
              Arrows.board[shift_col][row], Arrows.board[shift_col-1][row] = Arrows.board[shift_col-1][row], Arrows.board[shift_col][row]

    for row in range(5):
      for col in range(1,5):#같은것 합치기
        if Arrows.board[col][row] == Arrows.board[col-1][row] and Arrows.board[col-1][row] != 0 and merge_flag != col:#flag면 스킵
          Arrows.board[col-1][row] *= 2
          Arrows.board[col][row] = 0
          merge_flag = col+1#flag를 다음으로 바꿈
          for shift_col in range(col, 0, -1):
            Arrows.board[shift_col][row], Arrows.board[shift_col-1][row] = Arrows.board[shift_col-1][row], Arrows.board[shift_col][row]


  def Merge_down():#밑으로 당기기
    merge_flag=-1
    for row in range(5):
      for col in range(3, -1, -1):#0당겨서 처리
        if Arrows.board[col][row] == 0 and Arrows.board[col+1][row] != 0:#0이있으면 한칸씩 당김
            for shift_col in range(col, 4, 1):
              Arrows.board[shift_col][row], Arrows.board[shift_col+1][row] = Arrows.board[shift_col+1][row], Arrows.board[shift_col][row]

    for row in range(5):
      for col in range(3, -1, -1):#같은것 합치기
        if Arrows.board[col][row] == Arrows.board[col+1][row] and Arrows.board[col+1][row] != 0 and merge_flag != col:#flag이면 스킵
          Arrows.board[col+1][row] *= 2
          Arrows.board[col][row] = 0
          merge_flag = col-1#flag를 다음것으로 바꿈
          for shift_col in range(col, 4, 1):
            Arrows.board[shift_col][row], Arrows.board[shift_col+1][row] = Arrows.board[shift_col+1][row], Arrows.board[shift_col][row]
