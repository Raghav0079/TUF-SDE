class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows == 0:
            return []
            
        # Initialize the triangle with the first row
        triangle = [[1]]
        
        for r in range(1, numRows):
            row = [1] # Every row starts with 1
            prev_row = triangle[r - 1]
            
            # Fill in the middle elements of the row
            for c in range(1, r):
                row.append(prev_row[c - 1] + prev_row[c])
                
            row.append(1) # Every row ends with 1
            triangle.append(row)
            
        return triangle