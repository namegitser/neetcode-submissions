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
        
        seen = set()
        
        queue = deque([(0,-1)])
        seen.add(0)

        while queue:
            node, parent = queue.popleft()

            for neighbor in graph[node]:
                if neighbor == parent:
                    continue
                
                if neighbor in seen:
                    return False #cycle
                
                seen.add(neighbor)
                queue.append((neighbor, node))
        

        return len(seen) == n

