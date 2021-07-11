import random
board = [[0 for _ in range(5)] for _ in range(5)]#5X5 2048 Game Board
board[3][4], board[3][3], board[3][2], board[3][1], board[3][0]=0,32,0,16,16
board[4][0], board[3][0], board[2][0], board[1][0], board[0][0]=0,16,0,0,0
for n in range(4,-1,-1):
  for k in range(5):
    print(str(board[n][k]).rjust(4),end="|")
  print("")
print("\n")

  
#row행(가로), col열(세로)
def Merge_left():#왼쪽으로 당기기
  merge_flag=-1
  for col in range(5):
    for row in range(3, -1, -1):#0당겨서 처리
      if board[col][row] == 0 and board[col][row+1] != 0:#0이있으면 한칸씩 당김
          for shift_row in range(row, 4, 1):
            board[col][shift_row], board[col][shift_row+1] = board[col][shift_row+1], board[col][shift_row]

  for col in range(5):
    for row in range(3, -1, -1):#같은것 합치기
      if board[col][row] == board[col][row+1] and board[col][row+1] != 0 and merge_flag != row:#flag이면 스킵
        board[col][row+1] *= 2
        board[col][row] = 0
        merge_flag = row-1#flag를 다음것으로 바꿈
        for shift_row in range(row, 4, 1):
          board[col][shift_row], board[col][shift_row+1] = board[col][shift_row+1], board[col][shift_row]


def Merge_right():#오른쪽으로 당기기
  merge_flag=-1
  for col in range(5):
    for row in range(1,5):#0당겨서 처리
      if board[col][row] == 0 and board[col][row-1] != 0:#0이있으면 한칸씩 당김
          for shift_row in range(row, 0, -1):
            board[col][shift_row], board[col][shift_row-1] = board[col][shift_row-1], board[col][shift_row]

  for col in range(5):
    for row in range(1,5):#같은것 합치기
      if board[col][row] == board[col][row-1] and board[col][row-1] != 0 and merge_flag != row:#flag면 스킵
        board[col][row-1] *= 2
        board[col][row] = 0
        merge_flag = row+1#flag를 다음으로 바꿈
        for shift_row in range(row, 0, -1):
          board[col][shift_row], board[col][shift_row-1] = board[col][shift_row-1], board[col][shift_row]


def Merge_up():#위로 당기기
  merge_flag=-1
  for row in range(5):
    for col in range(1,5):#0당겨서 처리
      if board[col][row] == 0 and board[col-1][row] != 0:#0이있으면 한칸씩 당김
          for shift_col in range(col, 0, -1):
            board[shift_col][row], board[shift_col-1][row] = board[shift_col-1][row], board[shift_col][row]

  for row in range(5):
    for col in range(1,5):#같은것 합치기
      if board[col][row] == board[col-1][row] and board[col-1][row] != 0 and merge_flag != col:#flag면 스킵
        board[col-1][row] *= 2
        board[col][row] = 0
        merge_flag = col+1#flag를 다음으로 바꿈
        for shift_col in range(col, 0, -1):
          board[shift_col][row], board[shift_col-1][row] = board[shift_col-1][row], board[shift_col][row]


def Merge_down():#밑으로 당기기
  merge_flag=-1
  for row in range(5):
    for col in range(3, -1, -1):#0당겨서 처리
      if board[col][row] == 0 and board[col+1][row] != 0:#0이있으면 한칸씩 당김
          for shift_col in range(col, 4, 1):
            board[shift_col][row], board[shift_col+1][row] = board[shift_col+1][row], board[shift_col][row]

  for row in range(5):
    for col in range(3, -1, -1):#같은것 합치기
      if board[col][row] == board[col+1][row] and board[col+1][row] != 0 and merge_flag != col:#flag이면 스킵
        board[col+1][row] *= 2
        board[col][row] = 0
        merge_flag = col-1#flag를 다음것으로 바꿈
        for shift_col in range(col, 4, 1):
          board[shift_col][row], board[shift_col+1][row] = board[shift_col+1][row], board[shift_col][row]


def dodododown():
  for row in range(5):
    for col in range(4,0,-1):
      if board[col-1][row] == board[col][row] and board[col][row] != 0:
        board[col-1][row] *= 2
        board[col][row] = 0
      #0이있으면 이동
      elif board[col-1][row]==0 and board[col][row]!=0:
        board[col-1][row], board[col][row] = board[col][row], board[col-1][row]


Merge_down()
#Merge_left()

for n in range(4,-1,-1):
  for k in range(5):
    print(str(board[n][k]).rjust(4),end="|")
  print("")