import random
import os
class Arrows:
  def __init__(self):
    self.result = 0
    self.board = [[0 for _ in range(5)] for _ in range(5)]
    self.board_temp = [[0 for _ in range(5)] for _ in range(5)]
    self.key = 0
    self.quit_key = 0
  
#print('\033[31m \033[43m' + '글자와 배경 변경' + '\033[0m') 
  def screen(self):
    for n in range(4,-1,-1):
      for k in range(5):
        if self.board[n][k]==0:
          print("|" + str(self.board[n][k]).rjust(4),end="| ")
        else:
          print("|" + '\033[96m' + str(self.board[n][k]).rjust(4) + '\033[0m',end="| ")
      print("")
    print("\n")

  def clear(self):
    os.system('clear')


  def create(self):#빈칸에서 숫자 스폰
    zerosum = []
    num, zero_choice, number = 0, -1, -1
    for col in range(5):
      for row in range(5):
        if self.board[col][row] == 0:
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
    self.board[zero_choice[0]][zero_choice[1]] = number

      
  def quit(self):#게임오버
    print(" GAME OVER ")
    global quit_key
    quit_key=1

    
  #row행(가로), col열(세로)
  def Merge_left(self):#왼쪽으로 당기기
    merge_flag=-1
    for col in range(5):
      for row in range(3, -1, -1):#0당겨서 처리
        if self.board[col][row] == 0 and self.board[col][row+1] != 0:#0이있으면 한칸씩 당김
            for shift_row in range(row, 4, 1):
              self.board[col][shift_row], self.board[col][shift_row+1] = self.board[col][shift_row+1], self.board[col][shift_row]

    for col in range(5):
      for row in range(3, -1, -1):#같은것 합치기
        if self.board[col][row] == self.board[col][row+1] and self.board[col][row+1] != 0 and merge_flag != row:#flag이면 스킵
          self.board[col][row+1] *= 2
          self.board[col][row] = 0
          merge_flag = row-1#flag를 다음것으로 바꿈
          for shift_row in range(row, 4, 1):
            self.board[col][shift_row], self.board[col][shift_row+1] = self.board[col][shift_row+1], self.board[col][shift_row]


  def Merge_right(self):#오른쪽으로 당기기
    merge_flag=-1
    for col in range(5):
      for row in range(1,5):#0당겨서 처리
        if self.board[col][row] == 0 and self.board[col][row-1] != 0:#0이있으면 한칸씩 당김
            for shift_row in range(row, 0, -1):
              self.board[col][shift_row], self.board[col][shift_row-1] = self.board[col][shift_row-1], self.board[col][shift_row]

    for col in range(5):
      for row in range(1,5):#같은것 합치기
        if self.board[col][row] == self.board[col][row-1] and self.board[col][row-1] != 0 and merge_flag != row:#flag면 스킵
          self.board[col][row-1] *= 2
          self.board[col][row] = 0
          merge_flag = row+1#flag를 다음으로 바꿈
          for shift_row in range(row, 0, -1):
            self.board[col][shift_row], self.board[col][shift_row-1] = self.board[col][shift_row-1], self.board[col][shift_row]


  def Merge_up(self):#위로 당기기
    merge_flag=-1
    for row in range(5):
      for col in range(1,5):#0당겨서 처리
        if self.board[col][row] == 0 and self.board[col-1][row] != 0:#0이있으면 한칸씩 당김
            for shift_col in range(col, 0, -1):
              self.board[shift_col][row], self.board[shift_col-1][row] = self.board[shift_col-1][row], self.board[shift_col][row]

    for row in range(5):
      for col in range(1,5):#같은것 합치기
        if self.board[col][row] == self.board[col-1][row] and self.board[col-1][row] != 0 and merge_flag != col:#flag면 스킵
          self.board[col-1][row] *= 2
          self.board[col][row] = 0
          merge_flag = col+1#flag를 다음으로 바꿈
          for shift_col in range(col, 0, -1):
            self.board[shift_col][row], self.board[shift_col-1][row] = self.board[shift_col-1][row], self.board[shift_col][row]


  def Merge_down(self):#밑으로 당기기
    merge_flag=-1
    for row in range(5):
      for col in range(3, -1, -1):#0당겨서 처리
        if self.board[col][row] == 0 and self.board[col+1][row] != 0:#0이있으면 한칸씩 당김
            for shift_col in range(col, 4, 1):
              self.board[shift_col][row], self.board[shift_col+1][row] = self.board[shift_col+1][row], self.board[shift_col][row]

    for row in range(5):
      for col in range(3, -1, -1):#같은것 합치기
        if self.board[col][row] == self.board[col+1][row] and self.board[col+1][row] != 0 and merge_flag != col:#flag이면 스킵
          self.board[col+1][row] *= 2
          self.board[col][row] = 0
          merge_flag = col-1#flag를 다음것으로 바꿈
          for shift_col in range(col, 4, 1):
            self.board[shift_col][row], self.board[shift_col+1][row] = self.board[shift_col+1][row], self.board[shift_col][row]
