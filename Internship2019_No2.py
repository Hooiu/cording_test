#어떤 집합의 튜플(?)을 찾아라
#1.중복되는 숫자들 제거 --> 튜플의 원소가 되고
#2.집합에서 각 숫자들의 수 --> 튜플의 원소 순서
import re # 정규식을 사용하기 위한 모듈

def solution(s):

    numbers = re.findall('\d+',s) # 한자리 숫자 단위

    unique_set = set(numbers) # 튜플의 원소

    unique_qty = {}
    for i in unique_set:
        unique_qty[i] = numbers.count(i) # 튜플의 원소 개수를 Dictionary에 저장

    unique_qty2 = sorted(unique_qty.items(), key=lambda t : t[1],reverse=True) #value 기준으로 내림차순 정렬
  
    result_list = [int(i[0]) for i in unique_qty2]

    return result_list
