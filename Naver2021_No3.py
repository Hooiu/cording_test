# 주어진 문자(letter)에서 숫자(k) 만큼 뽑았을 때 가장 사전적으로 뒤에 오는 단어
# 단 letter에서 단어의 순서는 유지할 것

#문제풀이!
# 문자 길이 - k 까지 중에 가장 늦은 알파벳 찾을 것!
# 가장 늦은 
# 재귀함수로 풀이

import string

result = []

def solution2(letter, k):
    alphabets = list(string.ascii_lowercase)
    alphabets.reverse()
    naljibreak = True
    if len(letter) == 0:
        return ("".join(result))
    else:
        for alpha in alphabets:
            for i in range(len(letter)-k+1):
                if letter[i] == alpha:
                    temp_letter = letter[i+1:]
                    result.append(letter[i])
                    # print(temp_letter)
                    naljibreak = False
                    break
            if (naljibreak == False):
                break
        solution2(temp_letter,k-1)     
    return result

def solution(letters, k):
    answer = ''.join(solution2(letters,k))
    return answer

print(solution("zbgaj",3))

