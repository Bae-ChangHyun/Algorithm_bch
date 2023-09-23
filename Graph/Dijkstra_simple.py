# 알고리즘: 다익스트라 최단 경로
# 시간복잡도 O(V^2)

import sys
input = sys.stdin.readline
INF = int(1e9)

n, m = map(int, input().split())
start = int(input())   # 시작 노드
graph = [[] for _ in range(n+1)]  # 전체 그래프 저장
visited = [0 for _ in range(n+1)]  # 방문 저장
distance = [INF for _ in range(n+1)]  # 비용 저장

for _ in range(m):
    a, b, c = map(int, input().split())  # a->b 가는 비용 c
    graph[a].append((b, c))            # 그래프 연결


def get_smallest_node():              # 최소비용 노드 탐색 함수
    min_value = INF
    idx = 0
    for i in range(1, n+1):
        # 아직 방문하지 않았고, 비용이 더 최소이면 갱신
        if ((distance[i] < min_value) and (visited[i] == 0)):
            min_value = distance[i]
            idx = i
    # 최소 비용 인덱스 갱신
    return idx


def dijkstra(start):
    distance[start] = 0
    visited[start] = 1  # 방문처리

    for j in graph[start]:
        # distance[x]는 start에서 x까지의 거리를 의미
        distance[j[0]] = j[1]

    for i in range(n-1):
        now = get_smallest_node()
        visited[now] = 1

        for j in graph[now]:
            cost = distance[now] + j[1]

            if (cost < distance[j[0]]):
                distance[j[0]] = cost


dijkstra(start)

for i in range(1, n+1):
    if (distance[i] == INF):
        print("INFINITY")
    else:
        print(distance[i])
