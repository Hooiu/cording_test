# pattern이 몇개 포함되어 있는지
# S, 문자가 주어지고 길이는 1000이하
# pattern이 주어지고 길이는 8이하

#문제 풀이 방법은
# 1. pattern의 길이 만큼 잘라서 문자의 조합 찾기
# 2. 작은 문자의 모든 조합 찾기
# 3. 이중 pattern과 일치하는 경우 result += 1

import itertools

def check_patt (s, pattern):
    result = False
    all_cases = []
    all_cases = list(itertools.permutations(s,len(s)))
    if tuple(pattern) in all_cases:
        result = True
    return result


def solution(S, pattern):
    answer = 0
    for i in range(len(S)-len(pattern)+1):
        s = S[i:len(pattern)+i]
        if check_patt(s, pattern):
            answer += 1
    return answer

print(solution(str(input()),str(input())))