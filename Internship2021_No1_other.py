# 카카오 인턴십 2021, 문제1

# 다른 사람 풀이

numbers_alpha = {'zero':'0','one':'1','two':'2','three':'3','four':'4','five':'5','six':'6','seven':'7','eight':'8','nine':'9'}


def solution(s):

    answer = s
    for key, value in numbers_alpha.items():
        answer = answer.replace(key,value)

    return int(answer)
