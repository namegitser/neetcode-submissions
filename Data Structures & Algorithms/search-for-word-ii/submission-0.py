class TrieNode:
    def __init__(self):
            self.children = {}
            self.isword = False

    def buildTrie(self,word):
        curr = self
        for char in word:
            if char not in curr.children:
                curr.children[char] = TrieNode()
            curr = curr.children[char]
        curr.isword = True


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        
        root = TrieNode()
        #Build Trie
        for word in words:
            root.buildTrie(word)


        #Search in grid (dfs) and keep changing moving down to trie if found the char of word
        ROWS, COLS = len(board), len(board[0])
        res = set()
        visit = set()

        def dfs(r, c, node, word):
            if (r >= ROWS or c >= COLS or r < 0 or c < 0 or board[r][c] not in node.children or (r,c) in visit ):
                return


            visit.add((r,c))
            node = node.children[board[r][c]]
            word += board[r][c] #add matching chars

            if node.isword:
                res.add(word) #if found a word (isword = T) then add
            
            dfs(r+1, c, node, word)
            dfs(r-1, c, node, word)
            dfs(r, c+1, node, word)
            dfs(r, c-1, node, word)

            visit.remove((r,c))
            # we add and remove this from visit so that we do not run in infinite loop of going back to same chat again and again and to use the tile board[r][c] for completely different word in backtracking

        for r in range(ROWS):
            for c in range(COLS):
                dfs(r, c, root, "")

        return list(res)

            


        

            