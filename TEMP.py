import sys
input = sys.stdin.readline
INF = int(1e9)

N, M, C = map(int, input().split())
visited = [0 for _ in range(N+1)]
graph = [[] for _ in range(N+1)]
distance = [INF for _ in range(N+1)]

# 그래프 입력받음
for i in range(M):
    a, b, c = map(int, input().split())
    graph[a].append([b, c])


def get_min(start):
    min_value = INF
    idx = 0
    for i in range(1, N+1):
        if ((distance[i] < min_value) and (visited[i] == 0)):
            min_value = distance[i]
            idx = i
    return idx


def dijkstra(start):
    distance[start] = 0
    visited[start] = 1

    for j in graph[start]:
        distance[j[0]] = j[1]

    for i in range(N-1):
        now = get_min(start)
        visited[now] = 1
        for j in graph[now]:
            cost = distance[now] + j[1]

            if (cost < distance[j[0]]):
                distance[j[0]] = cost


dijkstra(C)

print(distance[C])
