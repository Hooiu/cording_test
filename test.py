# gems = {'Ruby':[3,2],'Dia':2}
# print(len(gems))
# # gems['Ruby'] += 1
# print(gems)
# print(gems['Ruby'][0])

# num = map(str, [1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5])
# left_fixed =['1','4','7']
# right_fixed = map(str,[3,6,9])
# main_hand = 'right'
# cur_left = '*'
# cur_right = '#'
# result_list = []

# for i in num:
#     if i in left_fixed:
#         result_list.append(cur_left)
#         cur_left = i

# print(result_list)

# A = 2.0
# B = 2

# print(type(A), type(B))
# if A == B:
#     print("int와 float 비교 가능하네!")


# print([i for i in range(3)])


def solution(v):
    answer = []
    x_list = []
    y_list = []
    x = 0
    y = 0
    for i in v:
        x_list.append(i[0])
        y_list.append(i[1])
    if x[0] == x[1]:
        x = x[2]
    elif x[0] == x[2]:
        x = x[1]
    elif x[1] == x[2]:
        x = x[0]
    
    if y[0] == y[1]:
        y = y[2]
    elif y[0] == y[2]:
        y = y[1]
    elif y[1] == y[2]:
        y = y[0]
    
    answer = [x,y]

    return answer

print(solution([[1, 4], [3, 4], [3, 10]]))