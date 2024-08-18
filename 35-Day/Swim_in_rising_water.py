import heapq
class Solution(object):
    def swimInWater(self, grid):
        n,m= len(grid), len(grid[0])
        visited=set()
        dir=[[0,1],[0,-1],[-1,0],[1,0]]
        minh=[(grid[0][0],0,0)]
        while minh:
            height,r,c=heapq.heappop(minh)
            if r==n-1 and c==m-1:
                return height
            if (r,c) in visited:
                continue
            visited.add((r,c))
            for nr,nc in dir:
                R,C=r+nr, c+nc
                if R<0 or R>=n or C<0 or C>=m or (R,C) in visited:
                    continue
                #we are taking maximum height because we have to return maximum height along that path
                heapq.heappush(minh, (max(height,grid[R][C]),R,C))
                        
            