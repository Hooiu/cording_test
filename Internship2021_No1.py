# 카카오 인턴십 2021, 문제1
# 풀이 아이디어
# 1. 문자와 숫자가 섞인 str 이 주어짐
# 2. 문자를 숫자로 변경
# "one4seveneight"--> 1478
# replace를 이용하여 for문 작성


# text = "one4seveneight"
# 0 zero
# 1 one
# 2 two
# 3 three
# 4 four
# 5 five
# 6 six
# 7 seven
# 8 eight
# 9 nine


# 어떻게 문자를 나눌까???
# 일단 숫자는 정규식을 이용해서 나눠볼까?
# text에서 하나씩 받아와서
#  1. if text_value in numbers_arabia:
#        result_list.append(text_value) #숫자일 경우 저장
#  2. 숫자가 아닐 경우
#      temp_text += text_value #계속 문자를 더하고
#      if temp_text in numbers # 딕셔너리에 있으면 저장
def solution(text):

    numbers_alpha = {'zero':'0','one':'1','two':'2','three':'3','four':'4','five':'5','six':'6','seven':'7','eight':'8','nine':'9'}
    numbers_arabia = ['0','1','2','3','4','5','6','7','8','9']

    result_list = []
    temp_text = ''
    for text_value in text:
        if text_value in numbers_arabia:
            result_list.append(text_value) #숫자일 경우
        else:                               #숫자가 아닐경우
            temp_text += text_value        #한글자씩 문자를 더하고
            if temp_text in numbers_alpha:
                result_list.append(numbers_alpha[temp_text])
                temp_text = ''

    result = int(''.join(result_list))
    return result
