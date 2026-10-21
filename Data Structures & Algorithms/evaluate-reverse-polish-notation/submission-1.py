class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operands = []
        
        for token in tokens:
            if token == '+' or token == '-' or token == '*' or token == '/':
                second = operands.pop()
                first = operands.pop()
                if token == '+':
                    res = first + second
                    #print(f'computed for (+) {first}+{second} = {res}')
                    operands.append(res)

                if token == '-':
                    res = first - second
                    #print(f'computed for - {second} - {first} = {res}')
                    operands.append(res)

                if token == '*':
                    res = first*second
                    #print(f'computed for * {first}*{second} = {res}')
                    operands.append(res)

                if token == '/':
                    res = int(first/second)
                    #print(f'computed for / {second}/{first} = {res}')
                    operands.append(res)
            
            else:
                operands.append(int(token))
                #print(f'added {token} to operands')
            
        return int(operands[0])







