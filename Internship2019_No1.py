#카카오 인턴십 2019 겨울, 문제 No.1, 크레인

#1. 배열로 표시
#2. 열순서대로 List에 담기
#3. 연속으로 같은 숫자 발견시 cnt +=1

board = [[0,0,0,0,0],
         [0,0,1,0,3],
         [0,2,5,0,1],
         [4,2,4,4,2],
         [3,5,1,3,1]]
moves = [1,5,3,5,1,2,1,4]

# 예상결과 = [4, 3, 1, 1, 3, 2, 4]
def solution(board, moves):
    answer = 0
    result_list = [0]
    cnt = 0
    for move_loc in moves:
        for row in range(len(board)):
            if board[row][move_loc-1] == 0:
                continue
            else:
                if board[row][move_loc-1] != result_list[-1]:
                    result_list.append(board[row][move_loc-1])
                else:
                    del result_list[-1]
                    cnt += 1
                board[row][move_loc-1] = 0
                break

    return cnt*2

print(solution(board, moves))
# print(result_list)
