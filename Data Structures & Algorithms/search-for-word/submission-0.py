class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])
        path_set = set()

        def dfs(r, c, word_index):
            if word_index == len(word):
                return True

            if (min(r, c) < 0 or r == ROWS or c == COLS or (r,c) in path_set
            or board[r][c]!=word[word_index]):
                return False

            path_set.add((r,c))

            res = (dfs(r-1, c, word_index+1) or
            dfs(r+1, c, word_index+1) or
            dfs(r, c-1, word_index+1) or
            dfs(r, c+1, word_index+1))
            

            path_set.remove((r,c))

            return res

        for r in range(ROWS):
            for c in range(COLS):
                if dfs(r,c,0):
                    return True

        return False

        
        
        

            
        

        
        
        