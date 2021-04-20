#문제 풀이 아이디어
# 1. Split함수를 이용하여 숫자만 리스트에 저장
#2. 사칙연산을 순서대로 리스트에 따로 저장
#3. 사칙연산 우선순위의 경우 수만큼 연산후 비교


#수 나누기 함수 & 사친역산을 순서대로 리스트에 저장

import re
from itertools import permutations

def sep_nos(A):
    ex = re.split(r'(\D)',A)
    three_cals = ['*','+','-']
    no_list = []
    cal_list = []
    for i in ex:
        if i not in three_cals: no_list.append(i)
        elif i in three_cals: cal_list.append(i)
    return(no_list, cal_list)


# 만약에 * 우선 순위라면

def calculation (operator, no_list, cal_list):
    for j in range(len(cal_list)):
        temp_no = 0
        if cal_list[j] == operator:
            temp_no = eval(str(no_list[j])+operator+str(no_list[j+1]))
            del no_list[j:j+2]
            del cal_list[j]
            no_list.insert(j,temp_no)
            break
    return (no_list, cal_list)

def solution(N):
    answer = 0
    operators = [list(y) for y in permutations(['*','+','-'])]
    result = []

    for value in operators:
        test_no_list, test_cal_list = sep_nos(N)
        for x in value:
            for y in range(len(test_cal_list)):
                test_no_list1, test_cal_list1 = calculation(x,test_no_list,test_cal_list)
        result.append(test_no_list1[0])

    result = list(map(abs,result))
    answer = max(result)
    return answer

N = "100-200*300-500+20"
print(solution(N))