from collections import deque
class Solution(object):
    def updateMatrix(self, mat):        
        m, n = len(mat), len(mat[0])
        dist = [[float('inf')] * n for _ in range(m)]
        queue = deque()
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    dist[i][j] = 0
                    queue.append((i, j))
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        while queue:
            x, y = queue.popleft()            
            for dx, dy in directions:
                new_x, new_y = x + dx, y + dy
                if 0 <= new_x < m and 0 <= new_y < n:                    
                    if dist[new_x][new_y] > dist[x][y] + 1:
                        dist[new_x][new_y] = dist[x][y] + 1
                        queue.append((new_x, new_y))        
        return dist
solution = Solution()
mat1 = [[0,0,0],[0,1,0],[0,0,0]]
mat2 = [[0,0,0],[0,1,0],[1,1,1]]
print(solution.updateMatrix(mat1))
print(solution.updateMatrix(mat2))
