class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # 1. Create a list of indices: [0, 1, 2, ..., n-1]
        # 2. Sort the indices based on their corresponding values in position (descending)
        sorted_indices = sorted(range(len(position)), key=lambda i: position[i], reverse=True)
        #print(sorted_indices)
        fleets = 0
        max_time = 0.0
        
        # 3. Iterate through the sorted indices
        for i in sorted_indices:
            # We look up position and speed using the sorted index `i`
            time = (target - position[i]) / speed[i]
            
            if time > max_time:
                fleets += 1
                max_time = time
                
        return fleets
