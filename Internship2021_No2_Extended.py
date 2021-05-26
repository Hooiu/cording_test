# 카카오 인턴십 2021, 문제2
# 배열 문제 (5x5)
# 하나씩 P인 것을 골라 맨하튼 거리 2까지 검토 (3x3)
# 일단 배열로 바꾸자

places = [["POOOP","OXXOX","OPXPX","OOXOX","POXXP"],
 ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"],
 ["PXOPX", "OXOXP", "OXPXX", "OXXXP", "POOXX"],
 ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"],
 ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]

import numpy as np

def extend_arr(arr):
    upper_lower_row = np.array([['O','O','O','O','O'],['O','O','O','O','O']])
    place_extended = np.vstack((upper_lower_row,arr,upper_lower_row))
    right_left_column = np.array([['O','O'],['O','O'],['O','O'],['O','O'],['O','O'],['O','O'],['O','O'],['O','O'],['O','O']])
    place_extended = np.hstack((right_left_column,place_extended,right_left_column))

    return(place_extended)


def distance_decision(place_list):
    for row in range(9):
        for column in range(9):
            if place_list[row][column] =='O' or place_list[row][column] =='X':  #사람이 아닌경우 다음으로
                continue
            else:
                if place_list[row-1][column]=='P': return False #위
                if place_list[row+1][column]=='P': return False   #아래
                if place_list[row][column-1]=='P': return False    #왼
                if place_list[row][column+1]=='P': return False   #오른
                if place_list[row-2][column] == 'P' and place_list[row-1][column] != 'X': return False      # 위 두칸
                if place_list[row+2][column] == 'P' and place_list[row+1][column] != 'X': return False      # 아래 두칸
                if place_list[row][column-2] == 'P' and place_list[row][column-1] != 'X': return False      # 왼쪽 두칸
                if place_list[row][column+2] == 'P' and place_list[row][column+1] != 'X': return False      # 오른쪽 두칸
                if place_list[row-1][column-1] == 'P':                   # 왼쪽-위 대각선(두칸)
                    if place_list[row-1][column] == 'O' or place_list[row][column-1] == 'O' : return False
                if place_list[row-1][column+1] == 'P':                   # 오른쪽-위 대각선(두칸)
                    if place_list[row-1][column] == 'O' or place_list[row][column+1] == 'O' : return False
                if place_list[row+1][column-1] == 'P':                    # 왼쪽-아래 대각선(두칸)
                    if place_list[row+1][column] == 'O' or place_list[row][column-1] == 'O' : return False
                if place_list[row+1][column-1] == 'P':                    # 왼쪽-아래 대각선(두칸)
                    if place_list[row+1][column] == 'O' or place_list[row][column-1] == 'O' : return False    
    return True

def solution(places):
    result = []
    for list_place in places:
        place = np.array(list(map(list,list_place)), dtype=str)
        if distance_decision(extend_arr(place)):
            result.append(1)
        else:
            result.append(0)
    return result
print(solution(places))
