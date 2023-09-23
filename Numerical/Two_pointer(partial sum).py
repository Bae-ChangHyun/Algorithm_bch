n = 5  # 데이터의 개수
m = 5  # 찾고자 하는 부분 합
data = [1, 2, 3, 2, 5]  # 수열

count = 0
interval_sum = 0
end = 0

for start in range(n):
    while (interval_sum < m and end < n):  # 부분합이 목표값보다 작으면 계속 end를 늘림
        interval_sum += data[end]        # end를 이동함에 따라 부분합이 증가됨
        end += 1
    if (interval_sum == m):  # 현재 부분합이 찾고자 하는 부분합이면
        count += 1         # 카운트를 올림
    interval_sum -= data[start]  # 여기까지 왔다는 것은 부분합이 목표값보다 크기 때문에 구간을 줄임.
print(count)  # answer = 3
