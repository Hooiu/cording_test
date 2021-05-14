# 카카오 인턴십 2021, 문제3

# 배열 같아 보이지만 리스트 문제
# n = 행 개수(리스트 원소 개수)
# cmd = ["D 2","C","U 3","C","D 4","C","U 2","Z","Z"] 이런 식으로 주어지며
#       "U X", "D X", "C", "Z" 네개
# 리스트에 숫자 n만큼 만들고
# cmd에서 D, U를 숫자와 문자로 분리 = [[D,2],[C',[U,3]....]]
# cmd에 따라 하나씩 수행 현재 위치는 k
# U : 위(왼쪽)로 가는 경우
# D : 아래(오른쪽)로 가는 경우
# C : 현재 선택된 행을 삭제한 후, 바로 아래 행을 선택합니다. 단, 삭제된 행이 가장 마지막 행인 경우 바로 윗 행을 선택합니다.
# Z : 가장 최근에 삭제된 행을 원래대로 복구합니다. 단, 현재 선택된 행은 바뀌지 않습니다.

#C 부분 위아래로 올라갈 때 X인 부분 뺴야 함!!!!!!!!!!!!!!!!!!!!!

n = 8 # 리스트 개수
k = 2 # 처음 위치
cmd = ["C","C","C","C","C","C"]

input_dic = {}
input_list = [i for i in range(n)]
for i in range(n):                          # Dictionary로 Input값 저장 = {0:"O", 1:"0"....}
    input_dic[i] = 'O'

new_cmd = []
temp_save = []
for value in cmd:                           # cmd에서 D, U를 숫자와 문자로 분리 = [[D,2],[C',[U,3]....]]
    new_cmd.append(value.split())

# print(new_cmd)
cnt = 0
up_qty = 0
down_qty = 0
deleted_qty = 0
for value in new_cmd:
    if value[0] == 'U':                     # U : 위(왼쪽)로 가는 경우
        for i in range(k-1,0,-1):     # X가 있는 경우는 회수에서 제외
            up_qty += 1
            if input_dic[i] == 'O':
                cnt+=1
            if cnt == int(value[1]):
                cnt = 0
                break
        k -= up_qty
        up_qty = 0
 
    elif value[0] =='D':
        for i in range(k+1,len(input_dic)):     # X가 있는 경우는 회수에서 제외
            down_qty += 1
            if input_dic[i] == 'O':
                cnt+=1
            if cnt == int(value[1]):
                cnt = 0
                break
        k += down_qty
        down_qty = 0
    elif value[0] =='C':

        temp_save.append([k,input_dic[k]])  # z를 위해 삭제되는 값 저장
        input_dic[k] = 'X'                  #C : 현재 선택된 행을 삭제
        if k+1 > len(input_dic):            #C : 끝에 있을 경우 
            k = 
        for i in range(k+1,len(input_dic)):
            deleted_qty += 1
            if input_dic[i] == 'O':
                cnt+=1
            if cnt == 1:
                cnt = 0
                break
        k += deleted_qty
        deleted_qty = 0                       # C: 삭제한 후, 바로 아래 행을 선택합니다
    elif value[0] == 'Z':                   #Z : 가장 최근에 삭제된 행을 원래대로 복구합니다. 단, 현재 선택된 행은 바뀌지 않습니다.
        input_dic[temp_save[-1][0]] = 'O'
        del temp_save[-1]
    # print(k)
    # print(input_dic)

result_list = [value for key, value in input_dic.items()]
print(''.join(result_list))
