class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        word_set = set(wordDict) #Create a set
        memo = {}

        def dfs(start):
            
            if start == len(s):
                return True

            if start in memo:
                return memo[start]

            
            for end in range(start+1, len(s)+1):
                curr = s[start:end]
                # print(curr)
                if curr in word_set and dfs(end):
                    memo[start] = True
                    return True

            memo[start] = False
            return False

        return dfs(0)


