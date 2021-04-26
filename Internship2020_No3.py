# 문제풀이 아이디어
# 투포인터 문제 // set to list를 이용한 중복값 제거
# 1. Input T에서 set함수를 이용해 배열에 몇개의 값이 있는지 확인
# 2. 0,0부터 시작. 왼쪽 포인터를 start / 오른쪽 포인터를 end로 지정
# 3. len(set(T)) == len(set(T[start:end]))이면 조건 만족 --> start, end 기록
#    --> start += 1
# 4. len(set(T)) > len(set(T[start:end]))이면 end += 1
# 5. len(set(T)) < len(set(T[start:end])) 이경우는 없음!!!
# 6. if end > len(T) | start > len(T)이면 끝!!

T = ["DIA", "DIA", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE","HANA","HOON"]
def solution(gems):
    start = 0
    end = 0
    result_list = []
    diff_list = []

    while start <= len(T) and end <= len(T):
        if len(set(T)) == len(set(T[start:end+1])):
            result_list.append([start+1,end+1])
            start += 1
        else:
            end += 1

    for i in result_list:
        diff_list.append(i[1]-i[0])

    return(result_list[diff_list.index(min(diff_list))])    

print(solution(T))
