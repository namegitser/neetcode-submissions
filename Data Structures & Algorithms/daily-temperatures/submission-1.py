class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = [] # we insert pairs (temp, index)
        
        for i, t in enumerate(temperatures):
            #we loop through all pairs (index, temp) and while there is something in stack and the current temp is greater than top of stack we pop and add in res (it's kind of keep adding pairs until we encounter any temp that is greater that top of stack)
            while stack and t > stack[-1][0]:
                stackT, stackInd = stack.pop()
                #print(f'popping {stackT}, index - {stackInd}')
                #print(f'adding {i-stackInd} at res[{stackInd}]')
                res[stackInd] = i - stackInd
            stack.append((t,i))
            #print(f'added{(t,i)}')
                        
        return res