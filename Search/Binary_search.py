# 백준: https://www.acmicpc.net/problem/2805
# 풀이: https://changsroad.tistory.com/287
# 알고리즘: binary search

# 예제 입력
# ---------------------------
# 4 7
# 20 15 10 17
# ---------------------------
# 예제 출력
# ---------------------------
# 15
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
tree = list(map(int, input().split()))
start, end = 1, max(tree)  # 이분탐색 검색 범위 설정

while start <= end:  # 적절한 벌목 높이를 찾는 알고리즘
    mid = (start+end) // 2

    log = sum([i-mid for i in tree if i > mid])

    # 벌목 높이를 이분탐색
    if log >= M:
        start = mid + 1
    else:
        end = mid - 1
print(end)
