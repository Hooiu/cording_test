#A, E, I, O, U 순서의 알파벳이 있고
# 이를 통해 만들 수 있는 단어들이 있다
# 어떤 단어가 주어졌을 때 이게 몇번째 존재하는 단어인지 Return

# 전체 경우의 수를 만들고
# 1단어, 2단어....
# 리스트에서 탐색

import itertools

list_iter1 = list(itertools.product('AEIOU',repeat=1))
list_iter2 = list(itertools.product('AEIOU',repeat=2))
list_iter3 = list(itertools.product('AEIOU',repeat=3))
list_iter4 = list(itertools.product('AEIOU',repeat=4))
list_iter5 = list(itertools.product('AEIOU',repeat=5))

list_iter = list_iter1 + list_iter2 + list_iter3 + list_iter4 + list_iter5
cnt = 0
for i in list_iter:
    if word != i:
        cnt += 1
    else:
        break


# def solution(word):
    
