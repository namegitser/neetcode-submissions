class Solution:
    def calPoints(self, operations: List[str]) -> int:
        res = []
        for ops in operations:
            
            if ops != '+' and ops != 'C' and ops!= 'D':
                res.append(int(ops))

            elif ops == '+':
                s = res[len(res)-1]
                f = res[len(res)-2]
                res.append(f+s)


            elif ops == 'C':
                res.pop()
            
            elif ops == 'D':
                l = res[len(res)-1]*2
                res.append(l)
             

        add = 0
        for r in res:
            add+=r

        return add


                

