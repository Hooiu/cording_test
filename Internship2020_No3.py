# 문제풀이 아이디어
# 투포인터 문제 // set to list를 이용한 중복값 제거
# 1. Input T에서 set함수를 이용해 배열에 몇개의 값이 있는지 확인
# 2. 0,0부터 시작. 왼쪽 포인터를 start / 오른쪽 포인터를 end로 지정
# 3(x). len(set(T)) == len(set(T[start:end]))이면 조건 만족 --> start, end 기록
#    --> start += 1
# 3. 위에서 지속적으로 len(set...)을 이용하게 되면 유효성 검사를 통과할 수 없음.... 따라서 Dictionary를 이용한 길이 비교가 필요
# 4. gems[0] 값을 먼저 Dictionary에 저장(보석종류: 개수) cur_gems = {T[0]:1}
# 5. 보석의 종류(길이)를 변수에 저장 gems_unique = len(set(T))
# 6. if gems_unique == cur_gems 두 값이 같으면 임시 결과에 저장 후 start =+1
# 6-1. start를 오른쪽으로 옮길 때에는 항상 기존 값을 삭제한다. cur_gems[T[start]] -= 1 또는 del cur_gems[T[start]]
# 7. 6번의 두 값이 같지 않으면 end += 1 후 cur_gems[T[end]] += 1 또는 cur_gems[T[end]] = 1
# 7-1 여기서 주의할 점은 end += 1 전에 out of range 가 될 수 있으므로 조건문 if end == len(T)-1: break 삽입
# 8 처음 찾은 임시 정답 값보다 길이가 긴 값은 찾을 필요가 없으므로 temp_len = end - start 보다 클 경우 바로 start를 한칸 오른쪽으로 옮긴다

T = ["AA", "AB", "AC", "AA", "AC"]
def solution(T):
    start = 0
    end = 0
    temp_len = len(T)
    result_list = []
    diff_list = []
    gems_unique = len(set(T))
    cur_gems = {T[0]:1}

    while start <= len(T)-1 and end <= len(T)-1:
        if gems_unique == len(cur_gems):
            result_list.append([start+1,end+1])
            if cur_gems[T[start]] > 1:
                cur_gems[T[start]] -= 1
            else:
                del cur_gems[T[start]]
            start += 1
            # 아래는 8번 항목을 위해 작성된 코드
            temp_len = end - start
        else:
            if end == len(T)-1: break
            end += 1
            if T[end] in cur_gems:
                cur_gems[T[end]] += 1
            else:
                cur_gems[T[end]] = 1
            
            # 아래는 8번 항목을 위해 작성된 코드
            if temp_len <= end - start:
                if cur_gems[T[start]] > 1:
                    cur_gems[T[start]] -= 1
                else:
                    del cur_gems[T[start]]
                start += 1

    return(result_list[-1])    

print(solution(T))
