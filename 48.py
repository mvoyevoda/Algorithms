class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        for ring in range(n//2):
            for pixel in range(ring, n-ring-1):
                top = matrix[ring][pixel]
                right = matrix[pixel][n-ring-1]
                bottom = matrix[n-ring-1][n-pixel-1]
                left = matrix[n-pixel-1][ring]
                matrix[ring][pixel] = left
                matrix[pixel][n-ring-1] = top
                matrix[n-ring-1][n-pixel-1] = right
                matrix[n-pixel-1][ring] = bottom                