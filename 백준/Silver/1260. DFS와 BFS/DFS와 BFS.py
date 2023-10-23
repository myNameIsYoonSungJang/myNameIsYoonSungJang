# import sys
# sys.stdin = open("input.txt", "r")

def dfs(n):
    ans_dfs.append(n)
    v[n] = 1
    
    for i in adj[n]:
        if not v[i]:
            dfs(i)
            
def bfs(s):
    q = []
    q.append(s)
    ans_bfs.append(s)
    v[s] = 1
    
    while q:
        c = q.pop(0)
        for n in adj[c]:
            if not v[n]:
                q.append(n)
                ans_bfs.append(n)
                v[n] = 1

N, M, V = map(int, input().split())
# N, M, V = map(int, sys.stdin.readline().split())
adj = [[] for _ in range(N+1)]
for i in range(M):
    s, e = map(int, input().split())
    # s, e = map(int, sys.stdin.readline().split())
    adj[s].append(e)
    adj[e].append(s)
    
for i in range(1,N+1):
    adj[i].sort()

v = [0] * (N+1)
ans_dfs = []
dfs(V)

v = [0] * (N+1)
ans_bfs = []
bfs(V)

print(*ans_dfs)
print(*ans_bfs)