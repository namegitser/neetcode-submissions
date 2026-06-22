class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t or not s:
            return ""
        target_map = {}
        window_map = {}
        l = 0
        need = 0
       

        for char in t:
            if char in target_map:
                target_map[char]+=1

            else:
                target_map[char] = 1
                need+=1

        have = 0
        res = [float("inf"), 0, 0] #tracker - win_len, left, right

        for r in range(len(s)):
            window_map[s[r]] = 1 + window_map.get(s[r], 0)

            if (s[r] in target_map) and window_map[s[r]] == target_map[s[r]]:
                have+=1

            while need == have:
                #we've got all t in s
                if (r-l+1) < res[0]:
                    res = [r-l+1, l, r]

                window_map[s[l]]-=1
                # if while shortening the window, we loose any of the t chars in s we decrease have
                if (s[l] in target_map) and window_map[s[l]] < target_map[s[l]]:
                    have-=1
                
                
                l+=1



        return s[res[1] : res[2]+1 ] if res[0]!=float("inf") else ""



