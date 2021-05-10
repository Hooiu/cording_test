# 카카오 인턴십 2021, 문제2
# 배열 문제 (5x5)
# 하나씩 P인 것을 골라 맨하튼 거리 2까지 검토 (3x3)
# 일단 배열로 바꾸자

places = [["POOOP",
  "OXXOX",
  "OPXPX",
  "OOXOX",
  "POXXP"],
 ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"],
 ["PXOPX", "OXOXP", "OXPXX", "OXXXP", "POOXX"],
 ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"],
 ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]

import numpy as np

place0 = np.array(list(map(list,places[0])), dtype=str)
place1 = np.array(list(map(list,places[1])), dtype=str)
place2 = places[2]
place3 = places[3]
place4 = places[4]

print(place1)




def distance_decision (place_list):
    for row in range(5):
        for column in range(5):
            if place_list[row][column] =='O' or place_list[row][column] =='X':  #사람이 아닌경우 다음으로
                continue
            else:                           # 사람인 경우
                # 위/아래/왼/오 한칸씩
                if row-1 >= 0:
                    if place_list[row-1][column]=='P': return False #위
                if row+1 <= 4:
                    if place_list[row+1][column]=='P': return False   #아래
                if column-1 >= 0:
                    if place_list[row][column-1]=='P': return False    #왼
                if column+1 <= 4:
                    if place_list[row][column+1]=='P': return False   #오른

                # 위/아래/왼/오 두칸씩
                if row-2 >= 0:
                    if place_list[row-2][column] == 'P' and place_list[row-1][column] != 'X': return False      # 위 두칸
                if row+2 <= 4:
                    if place_list[row+2][column] == 'P' and place_list[row+1][column] != 'X': return False      # 아래 두칸
                if column-2 >= 0:
                    if place_list[row][column-2] == 'P' and place_list[row][column-1] != 'X': return False      # 왼쪽 두칸
                if column+2 <= 4:
                    if place_list[row][column+2] == 'P' and place_list[row][column+1] != 'X': return False      # 오른쪽 두칸


                # 대각선
                if row-1 >=0 and column-1>=0:
                    if place_list[row-1][column-1] == 'P':                   # 왼쪽-위 대각선(두칸)
                        if place_list[row-1][column] == 'O' or place_list[row][column-1] == 'O' : return False
                if row-1>=0 and column+1<=4:
                    if place_list[row-1][column+1] == 'P':                   # 오른쪽-위 대각선(두칸)
                        if place_list[row-1][column] == 'O' or place_list[row][column+1] == 'O' : return False
                if row+1<=4 and column-1>=0:
                    if place_list[row+1][column-1] == 'P':                    # 왼쪽-아래 대각선(두칸)
                        if place_list[row+1][column] == 'O' or place_list[row][column-1] == 'O' : return False
                if row+1<=4 and column-1>=0:
                    if place_list[row+1][column-1] == 'P':                    # 왼쪽-아래 대각선(두칸)
                        if place_list[row+1][column] == 'O' or place_list[row][column-1] == 'O' : return False       


    return True

def solution(places):
    place0 = list(map(list,places[0]))
    place1 = list(map(list,places[1]))
    place2 = list(map(list,places[2]))
    place3 = list(map(list,places[3]))
    place4 = list(map(list,places[4]))
    places_new = [place0, place1, place2, place3, place4]
    result=[]
    for place in places_new:
        if distance_decision(place):
            result.append(1)
        else:
            result.append(0)
    return result

print(solution(places))
