class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        #for all char(maintianing set) 
        graph = {c:set() for w in words for c in w}
        
        for i in range(len(words)-1):
            w1, w2 = words[i], words[i+1]
            minLen = min(len(w1), len(w2))
            if len(w1) > len(w2) and w1[:minLen] == w2[:minLen]: #['abc', 'ab']
                return ""

            for j in range(minLen):
                if w1[j] != w2[j]:
                    graph[w1[j]].add(w2[j])
                    break

        print(graph) #graph filled. we'll use this graph to make something

        #now startd dfs
        visit = {} #False - visited, #True - visited & currpath
        res = []

        def dfs(c):
            if c in visit:
                return visit[c]

            visit[c] = True #visited and in current path
            for nei in graph[c]:
                if dfs(nei): #if it is True means we've got a cycle
                    return True #detected loop

            visit[c] = False #Removed from curr path 
            res.append(c)

        for c in graph:
            if dfs(c):
                return "" #cycle detected our dictionary is not valid

        res.reverse()
        return "".join(res)




            





            