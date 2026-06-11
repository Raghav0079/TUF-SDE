class Solution:
    # Function to solve the problem using space optimization
    def func(self, m, n):
        """ Create a list to represent
        the previous row of the grid"""
        prev = [0] * n
        
        # Iterate through the rows of the grid
        for i in range(m):
            """ Create a temporary list 
            to represent the current row"""
            temp = [0] * n
            
            for j in range(n):
                # Base case
                if i == 0 and j == 0:
                    temp[j] = 1
                    continue
                
                """ Initialize variables to store the number 
                of ways from the cell above (up) and left (left)"""
                up = prev[j] if i > 0 else 0
                left = temp[j - 1] if j > 0 else 0
                
                """ Calculate the number of ways to reach 
                the current cell by adding 'up' and 'left'"""
                temp[j] = up + left
            
            """ Update the previous list with 
            values calculated for the current row"""
            prev = temp
        
        """ The result is stored in the last
        cell of the previous row (n-1)"""
        return prev[-1]
    
    """ Function to count the total ways 
    to reach (0,0) from (m-1,n-1)"""
    def uniquePaths(self, m, n):
        # Return the total count (0-based indexing)
        return self.func(m, n)

