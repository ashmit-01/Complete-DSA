class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
       # BRUTE
        # n = len(matrix)
        # rotated = [[0] * n for _ in range(n)] 
        # for i in range(n):
        #     for j in range(n):
        #         rotated[j][n - i - 1] = matrix[i][j]
        # for i in range(n):

        #     for j in range(n):

        #         matrix[i][j] = rotated[i][j]

        """
        Do not return anything, modify matrix in-place instead.
        """
    
    # Optimal

        for i in range(len(matrix)):
            for j in range(i+1,len(matrix)):
                matrix[i][j],matrix[j][i] = matrix[j][i],matrix[i][j]

        for i in range(len(matrix)):
            matrix[i].reverse()        
        