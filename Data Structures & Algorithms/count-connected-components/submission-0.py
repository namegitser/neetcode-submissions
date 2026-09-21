class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = {}
        n_component = 0
        visit = set()
        
        for i in range(n):
            graph[i] = []

        for node, neigh in edges:
            graph[node].append(neigh)
            graph[neigh].append(node)

        # print(graph)
        def dfs(node):
            # print(f'in {node}')
            if node in visit:
                return
            
            visit.add(node)

            for neighbor in graph[node]:
                dfs(neighbor)
            

        for i in range(n):
            if i not in visit: #will only go inside for another disconnected component as previous dfs will add all in the visit set
                n_component+=1
                dfs(i)

        return n_component
        
