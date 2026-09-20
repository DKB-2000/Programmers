from collections import deque

def solution(n):
    dx = [1,0,-1,0]
    dy = [0,1,0,-1]
    
    answer = [[0 for _ in range(n)] for _ in range(n)]
    q = deque()
    q.append((0,0))
    answer[0][0] = 1
    cnt = 1
    
    t = 0
    while q:
        
        x,y = q.popleft()
        
         
        if cnt == n * n:
            break
            
            
        nx = x + dx[t]
        ny = y + dy[t]

        if (nx < 0 or nx >= n or ny < 0 or ny >= n or answer[ny][nx] != 0):
            t = (t + 1) % 4
            nx = x + dx[t]
            ny = y + dy[t]
            
        q.append((nx, ny))

        cnt += 1
        answer[ny][nx] = cnt
            
    print(answer)

    return answer