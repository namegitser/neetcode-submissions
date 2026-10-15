from typing import List

class Solution:

    def encode(self, strs: List[str]) -> str:
        res = []
        for s in strs:
            res.append(str(len(s)))
            res.append('#')
            res.append(s)
        return "".join(res)


    def decode(self, s: str) -> List[str]:
        """
        EXAMPLE TRACE:
        If s = "4#neet5#co#de" (encoded from ["neet", "co#de"])
        
        --- ITERATION 1 ---
        i = 0, j = 0
        Inner while loop finds '#' at index 1 -> j becomes 1
        length = int(s[0:1]) -> 4
        i = 1 + 1 -> 2 (Points to 'n')
        j = 2 + 4 -> 6 (Points to '5')
        res.append(s[2:6]) -> Adds "neet" to res
        i = 6
        
        --- ITERATION 2 ---
        i = 6, j = 6
        Inner while loop finds '#' at index 7 -> j becomes 7
        length = int(s[6:7]) -> 5
        i = 7 + 1 -> 8 (Points to 'c')
        j = 8 + 5 -> 13 (Points to end of string)
        res.append(s[8:13]) -> Adds "co#de" to res (ignores the inner '#')
        i = 13 -> Loop terminates (13 < 13 is False)
        """
        res = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            # now my j is at the '#' character
            length = int(s[i:j])   # this gives len of the word decoded
            i = j + 1              # j+1 is word start
            j = i + length         # complete length of word
            res.append(s[i:j])
            i = j
        return res
