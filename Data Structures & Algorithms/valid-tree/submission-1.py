class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n-1: #valid tree has n-1 edges
            return False

        graph = {}
        for i in range(n):
            graph[i] = []

        for node, neigh in edges:
            graph[node].append(neigh)
            graph[neigh].append(node)
        
        visit = set()
        #print(graph)
        def dfs(node, parent):
            # print(f'node{node}')
            if node in visit:
                return False

            visit.add(node)
            # print(visit)
            for neighbor in graph[node]:
                if neighbor == parent:
                    continue 
                 
                #early exit
                if not dfs(neighbor, node):
                    return False

            return True
        
        if not dfs(0,-1):
            #print('cycle')
            return False

        if len(visit) != n:
            return False
            
        return True