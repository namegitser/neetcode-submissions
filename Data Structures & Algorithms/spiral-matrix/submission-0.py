class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix or not matrix[0]:
            return []
        
        res = []
        top, bottom = 0, len(matrix) - 1
        left, right = 0, len(matrix[0]) - 1
        
        while left <= right and top <= bottom:
            # 1. Move right across the top row
            for col in range(left, right + 1):
                res.append(matrix[top][col])
            top += 1
            
            # 2. Move down the rightmost column
            for row in range(top, bottom + 1):
                res.append(matrix[row][right]) # Fixed: changed 'top' to 'right'
            right -= 1
            
            # 3. Move left across the bottom row (check if row still exists)
            if top <= bottom:
                for col in range(right, left - 1, -1):
                    res.append(matrix[bottom][col])
                bottom -= 1
            
            # 4. Move up the leftmost column (check if column still exists)
            if left <= right:
                for row in range(bottom, top - 1, -1):
                    res.append(matrix[row][left])
                left += 1 # Fixed: changed left -= 1 to left += 1 to move boundary inward
                
        return res
