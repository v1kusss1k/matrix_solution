#rows - кол-во строк                    
#d_row - сдвиг по строкам
#colums - кол-во столбцов 
#d_col - cдвиг по стобцам

class Solution:
    def longestIncreasingPath(self, matrix):
        if not matrix or not matrix[0]:
            return 0

        rows = len(matrix)
        columns = len(matrix[0])

        dp = [[0] * columns for _ in range(rows)]
        steps = [(1, 0), (-1, 0), (0, 1), (0, -1)]     #вниз, вверх, вправо, влево

        def dfs(row, col):
            if dp[row][col] != 0:
                return dp[row][col]

            max_len = 1

            for d_row, d_col in steps:
                new_row = row + d_row
                new_col = col + d_col
                if 0 <= new_row < rows and 0 <= new_col < columns:
                    if matrix[new_row][new_col] > matrix[row][col]:
                        max_len = max(max_len, 1 + dfs(new_row, new_col))

            dp[row][col] = max_len
            return max_len

        result = 0
        for row in range(rows):
            for col in range(columns):
                result = max(result, dfs(row, col))

        return result
