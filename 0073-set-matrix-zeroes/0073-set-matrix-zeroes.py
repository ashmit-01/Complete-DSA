class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        n = len(matrix)   # Row
        m = len(matrix[0])  # Col
        
        # The extra space we using to avoid collision
        col0 = 1

        for i in range(n):
            for j in range(m):
                if matrix[i][j] == 0:
                    # mark the First row as 0
                    matrix[i][0] = 0
                    # mark the first col as 0
                    if j != 0:
                        matrix[0][j] = 0
                    else:
                        col0 = 0    

        # Now for the inside matrix ie from i+1 and j+1

        for i in range(1,n):
            for j in range(1,m):
                # check if the element is 0 or not if not then check if the first row or column is 0 or not if that is 0 then chnge it to 0

                if matrix[i][j] != 0:
                    # check for 1 row and col
                    if matrix[0][j] == 0 or matrix[i][0] == 0:
                        matrix[i][j] = 0

        # Now the third step for the first row and col
        if matrix[0][0] == 0:
            for j in range(m):
                matrix[0][j] = 0
        if col0 == 0:
            for i in range(n):
                matrix[i][0] = 0

        return matrix                                
        