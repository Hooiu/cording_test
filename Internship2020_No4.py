#배열 함수가 주어짐. 이때 1은 벽을 의미함
board = [[0,0,0,0,0,0],
        [0,1,1,1,1,0],
        [0,0,1,0,0,0],
        [1,0,0,1,0,1],
        [0,1,0,0,0,1],
        [0,0,0,0,0,0]]

# board[0][0] 부터 시작
# 갈 수 있는 방향 -> 오른쪽 | 아래 | 위 | 왼쪽
# 단, 벽이 있거나, 0보다 작거나, 이전에 온 곳으로는 가지 않음.
# cur_location = board[0][0]
# board[0][0] = 'Build'
# case 오른쪽 : board[0][0+1]
# case 아래 : board[0+1][0]
# case 위 : board[0-1][0]
# case 왼쪽 : board[0][0-1]

low = 0
column = 0

while low == len(board) and column == len(board[-1]):
    
    