from typing import List
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        for i in range(n):
            for j in range(i, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        for i in range(n):
            matrix[i].reverse()

if __name__ == "__main__":
    solution = Solution()
    matrix1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    print(f"Input: {matrix1}")
    solution.rotate(matrix1)
    print(f"Output: {matrix1}\n")
    matrix2 = [[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]]
    print(f"Input: {matrix2}")
    solution.rotate(matrix2)
    print(f"Output: {matrix2}\n")
