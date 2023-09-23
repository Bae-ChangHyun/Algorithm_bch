# 두 리스트의 정렬
n, m = 3, 4  # 배열의 길이 선언

# 정렬된 두 배열 선언
a = [1, 3, 5]
b = [2, 4, 6, 8]

# 최종 정렬된 배열을 저장할 배열
result = [0]*(m+n)

# i = 첫번쨰 리스트 인덱싱
# j = 두번째 리스트 인덱싱
# k = 최종 리스트 인덱싱

i, j, k = 0, 0, 0

while (i < n or j < m):
    # 두번쨰 리스트 b의 길이를 넘어섰거나, 리스트 a의 원소가 b의 원소보다 작을 때.
    if (j >= m or (i < n and a[i] <= b[j])):
        result[k] = a[i]
        i += 1
    # 첫번째 리스트 a의 길이를 넘어섰거나, 리스트 b의 원소가 a의 원소보다 작을 떄.
    else:
        result[k] = b[j]
        j += 1
    k += 1

for i in result:
    print(i, end="")
