class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_s = ''.join(char.lower() for char in s if char.isalnum())
        first, last = 0, len(new_s)-1
        while first<last:
            if new_s[first]!=new_s[last]:
                return False
            first+=1
            last-=1

        return True