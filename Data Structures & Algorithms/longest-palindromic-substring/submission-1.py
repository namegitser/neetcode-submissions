class Solution:
    def longestPalindrome(self, s: str) -> str:
        index, Len = 0, 0
        for i in range(len(s)):

            l, r = i, i #ODD
            while l >= 0 and r < len(s) and  s[l] == s[r]:
                if (r-l+1) > Len:
                    index = l
                    Len = r-l+1
                l-=1
                r+=1

            l, r = i, i+1 #EVEN
            while l >= 0 and r < len(s) and  s[l] == s[r]:
                if (r-l+1) > Len:
                    index = l
                    Len = r-l+1
                l-=1
                r+=1

        return s[index : (index+Len)]


