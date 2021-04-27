#키패드를 누르는 규칙
#1,4,7 : 왼손 // 3,6,9 : 오른손 // 2,5,8,0 : 두 손 중 가까운 쪽(같을 경우 주 사용 손잡이에 따라)
#시작은 각각 *과 #


#좌표로 저장 points = {'*':[0,0],'0':[0,1],'#':[0,2],'7':[1,0],'8':[1,1],'9':[1,2],'4':[2,0],'5':[2,1],'6':[2,2],'1':[3,0],'2':[3,1],'3':[3,2]}
#손가락의 최근 위치를 지정 left, right



def solution(numbers, hand):

    num = list(map(str, numbers))
    left_fixed = ['1','4','7']
    right_fixed = ['3','6','9']
    cur_left = '*'
    cur_right = '#'
    result_list = []

    points = {'*':[0,0],'0':[0,1],'#':[0,2],'7':[1,0],'8':[1,1],'9':[1,2],'4':[2,0],'5':[2,1],'6':[2,2],'1':[3,0],'2':[3,1],'3':[3,2]}
    #현재 양손가락과 첫번째 값의 거리 비교

    for i in num:
        if i in left_fixed:
            result_list.append('L')
            cur_left = i
        elif i in right_fixed:
            result_list.append('R')
            cur_right = i
        else:
            left_dist = abs(points[i][0]-points[cur_left][0]) + abs(points[i][1]-points[cur_left][1])
            right_dist = abs(points[i][0]-points[cur_right][0]) + abs(points[i][1]-points[cur_right][1])
            if left_dist == right_dist:
                if hand == 'right':
                    cur_right = i
                    result_list.append('R')
                elif hand == 'left':
                    cur_left = i
                    result_list.append('L')
            elif left_dist > right_dist:
                cur_right = str(i)
                result_list.append('R')
            elif left_dist < right_dist:
                cur_left = str(i)
                result_list.append('L')
        print([cur_left,cur_right])
    answer = ''.join(result_list)

    return answer

print(solution([7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2], 'left'))
