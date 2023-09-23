# 백준: https://www.acmicpc.net/problem/1929
# 풀이: https://changsroad.tistory.com/69
# 알고리즘: 에라토스테네스의 체

# 예제 입력
# ---------------------------
# 3 16
# ---------------------------
# 예제 출력
# ---------------------------
# 3
# 5
# 7
# 11
# 13

import math

n = 1000  # 2~n까지 모든 수에 대하여 소수 판별
array = [1 for i in range(n+1)]  # 0,1을 제외하고 모두 소수(1)로 초기화

for i in range(2, int(math.sqrt(n))+1):  # 제곱근까지만 보면 됨. 짝지어지기 때문
    if (array[i] == 1):
        j = 2
        while (i*j <= n):
            array[i*j] = 0  # 소수의 배수를 모두 제거
            j += 1          # 소수만 남김(ex. i=2일 때, 2를 제외한 2의 배수를 모두 제거)
for i in range(2, n+1):
    if (array[i] == 1):
        print(i, end="")  # 2~n까지중의 소수를 출력
