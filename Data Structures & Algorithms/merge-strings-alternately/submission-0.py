class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        s = ""
        for w1, w2 in zip(word1,word2):
            s+=w1
            s+=w2
        
        w1, w2 = len(word1), len(word2)
        if w1>w2:
            s+=word1[w2:]
        
        else:
            s+=word2[w1:] 
        return s