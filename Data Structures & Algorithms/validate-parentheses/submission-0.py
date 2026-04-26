class Solution:
    def isValid(self, s: str) -> bool:
        stk = []
        mapper = {  ')': '(',
                   ']':'[',
                   '}': '{' }
        
        for char in s:
            if char in mapper: # checking if char = close parantheses
                if stk and stk[-1] == mapper[char]:
                    stk.pop()
                
                else:
                    return False
            
            else:
                stk.append(char) #adding all the open parantheses

        return True if not stk else False
                 

