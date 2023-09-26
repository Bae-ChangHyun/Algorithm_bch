# 알고리즘: 다익스트라 최단 경로
# 시간복잡도 O(ElogV) --v:노드의개수, E:간선의개수

import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

n, m = map(int, input().split())
start = int(input())   # 시작 노드
graph = [[] for _ in range(n+1)]  # 전체 그래프 저장
distance = [INF for _ in range(n+1)]  # 비용 저장

for _ in range(m):
    a, b, c = map(int, input().split())  # a->b 가는 비용 c
    graph[a].append((b, c))            # 그래프 연결


def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)
        if (distance[now] < dist):
            continue
        for j in graph[now]:
            cost = distance[now] + j[1]
            if (cost < distance[j[0]]):
                distance[j[0]] = cost
                heapq.heappush(q, (cost, j[0]))


dijkstra(start)

for i in range(1, n+1):
    if (distance[i] == INF):
        print("INFINITY")
    else:
        print(distance[i])
