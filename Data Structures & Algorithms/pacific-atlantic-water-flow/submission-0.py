class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])
        pacific_set = set() #Fill ocean water in the island from pacific
        atlantic_set = set() #Fill the ocean water in the island form atlantic

        def dfs(r, c, prev_height, reach_set):


            if (r < 0 or c < 0 or r >= ROWS or c >= COLS or heights[r][c]<prev_height or (r,c) in reach_set):
                return
            
            reach_set.add((r,c))
            dfs(r+1, c, heights[r][c], reach_set)
            dfs(r-1, c, heights[r][c], reach_set)
            dfs(r, c+1, heights[r][c], reach_set)
            dfs(r, c-1, heights[r][c], reach_set)
        
        for r in range(ROWS):
            dfs(r, 0, heights[r][0], pacific_set)
            dfs(r, COLS-1, heights[r][COLS-1], atlantic_set)

        for c in range(COLS):
            dfs(0, c, heights[0][c], pacific_set)
            dfs(ROWS-1, c, heights[ROWS-1][c], atlantic_set)

        #Now both of my set are filled
        res = []
        for r in range(ROWS):
            for c in range(COLS):
                if (r,c) in pacific_set and (r,c) in atlantic_set:
                    res.append((r,c)) #if water can be filled from both oceans then can be poured too

        return res

