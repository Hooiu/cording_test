#카카오 인턴십 2019, 문제 No.3, 제제 아이디 검토

# banned_id에 있는 값을 user_id에 하나씩 비교하여 일치할 경우 Dictionary에 넣기
#  1. 글자 길이가 일치하는 지
#  2. 각 글별로 비교. 단 *가 있는 경우 건너띄기
# Dictionary에 있는 값들로 경우에 수 찾기

user_id_list = ["frodo", "fradi", "crodo", "abc123", "frodoc"]
banned_id_list = ["fr*d*", "*rodo", "******", "******"]

import itertools

# 글자비교 함수

def comparison_str(str1, str2):
    str1 = str1.replace('!','') # 같은 이름이 있어 추가한 느낌표 제거
    str2 = str2.replace('!','')
    if len(str1) != len(str2):
        return False
    else:
        for i in range(len(str1)):
            if str1[i] == '*' or str2[i] =='*':
                continue
            elif str1[i] == str2[i]:
                continue
            else:
                return False
        return True

# print(comparison_str('frodo','fr*d*'))


# banned_id_list에 같은 값이 있는 경우 문자 변경(느낌표 추가)

for banned_id in banned_id_list:
    cnt = 1
    if banned_id_list.count(banned_id) != 1:
        banned_id_list[banned_id_list.index(banned_id)] = banned_id + '!'*cnt
        cnt += 1
print(banned_id_list)

#빈 Dictionary 만들기
result_dict = {}

#Dictionary안에 Key 별로 Value 넣기

for banned_id in banned_id_list:
    for user_id in user_id_list:
        if comparison_str(banned_id,user_id):
            if banned_id in result_dict:
                result_dict[banned_id].append(user_id)
            else:
                result_dict[banned_id] = [user_id]

# 각 Key 별로 user id 리스트 (ex. [frodo, fradi])

result_list = list(result_dict.values())

# result_list에서 뽑아낼 수 있는 모든 경우의 수를 answer_list에 저장

answer_list = list(itertools.product(*result_list))

#한 경우의 수 안에 같은 ID가 있는 경우 제거
answer_list2 = []
for answer in answer_list:
    if len(set(answer)) == len(answer):
        answer_list2.append(set(answer))

#순서만 다른 같은 경우의 수 제거
for answer in answer_list2:
    if answer_list2.count(answer) != 1:
        del answer_list2[answer_list2.index(answer)]

print(len(answer_list2))

