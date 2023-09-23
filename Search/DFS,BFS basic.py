# 백준: https://www.acmicpc.net/problem/2606
# 풀이: https://changsroad.tistory.com/265
# 알고리즘: bfs, dfs

# 예제 입력
#---------------------------
# 7
# 6
# 1 2
# 2 3
# 1 5
# 5 2
# 5 6
# 4 7
#---------------------------
# 예제 출력
#---------------------------
# 4

import sys
from collections import deque
input= sys.stdin.readline

def dfs(connect):
    visited[connect]=1 # 현재 노드 방문처리
    for nx in graph[connect]:
        if visited[nx]==0: # 아직 방문하지 않았으면, 
            dfs(nx) # 재귀로 호출 
    return 0

def bfs(connect):
    visited[connect]=1 # 현재 노드 방문처리
    Q=deque([connect]) # 첫번째 노드 Q에 삽입
    while Q:           # Q가 빌 때까지 반복
        c=Q.popleft()  # 선입선출 
        for nx in graph[c]:
            if visited[nx]==0: # 방문하지 않았다면,
                Q.append(nx)   # Q에 삽입
                visited[nx]=1  # 방문처리
    return 0

n=int(input()) # 컴퓨터 개수
connect=int(input()) # 연결선 개수
graph = [[] for i in range(n+1)] # 그래프 초기화
visited=[0 for i in range(n+1)]

for i in range(connect): # 그래프 생성
    a,b=map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

dfs(1)
bfs(1)

print(sum(visited)-1)