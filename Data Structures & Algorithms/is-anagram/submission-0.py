class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!= len(t):
            return False
        s_list, t_list = list(s), list(t)
        s_mapper, t_mapper = {}, {}
        for s in s_list:
            if ord(s) in s_mapper:
                s_mapper[ord(s)]+=1
            else:
                s_mapper[ord(s)]=1
        
        for t in t_list:
            if ord(t) in t_mapper:
                t_mapper[ord(t)]+=1
            else:
                t_mapper[ord(t)]=1

        return s_mapper == t_mapper

