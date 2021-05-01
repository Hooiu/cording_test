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

A = 2.0
B = 2

print(type(A), type(B))
if A == B:
    print("int와 float 비교 가능하네!")